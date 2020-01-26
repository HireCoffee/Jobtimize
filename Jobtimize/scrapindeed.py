#!/usr/bin/env python
# coding: utf-8

__author__ = 'Lrakotoson'
__copyright__ = 'Copyright 2020, Jobtimize'
__license__ = 'MIT'
__version__ = '0.0.2'
__maintainer__ = 'Loïc Rakotoson'
__email__ = 'contact@loicrakotoson.com'
__status__ = 'planning'
__all__ = ['IndeedScrap']

""
from urllib.request import urlopen, HTTPError
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import re
""
def scrapPage(url):
    """
    Scrap an html document from the URL
    :url: page url
    :return: html page, BeautifulSoup object
    """
    with urlopen(url) as response:
        page = BeautifulSoup(response.read(), 'html.parser')
    return page

""
def scrapID(page):
    """
    Collect the IDs of the job ads published on the active page
    :page: html page, BeautifulSoup object
    :return: set of IDs
    """
    resultCol = page.find(id="resultsCol")
    setID = {
        jobcard["data-jk"]
        for jobcard in resultCol.findAll("div",
                                         {"class": "jobsearch-SerpJobCard"})
    }
    return setID

""
def stripmatch(page):
    """
    Get the number of pages visited and match for the current search
    :page: html page, BeautifulSoup object
    :return: tuple
    """
    try:
        text = page.find(id="searchCountPages").text.strip()
    except AttributeError:
        repage = match = None
    else:
        numlist = [num for num in re.findall(r'-?\d+\.?\d*', text)]
        repage = int(numlist[0])
        if len(numlist) == 2:
            match = int(numlist[1])
        else:
            match = int(''.join(numlist[1:]))
    return repage, match

""
def scrapIndeedID(searchList, countryList):
    """
    Extract jobIDs from the search results provided by Indeed
    :searchList: list of jobs or keywords to search
    :country: list of countries in 2-letter code
    :return: set of tuples, country and ID
    """
    setID = set()
    for search in searchList:
        search = search.replace(" ", "+")
        for country_general in countryList:
            country = country_general.lower()
            if country == "us": country = "www" #"us" note redirected
            listID = set()
            limit = 50
            start = repage = count = 0
            match = None
            while (repage <= 101 or len(listID) < match):
                url = "https://{}.indeed.com/jobs?q={}&limit={}&start={}".format(
                    country, search, limit, start)
                try:
                    page = scrapPage(url)
                except HTTPError:
                    break
                else:
                    repage, match = stripmatch(page)
                    count += 1
                    if (match is None or repage < count):
                        break
                    else:
                    
                        listID = listID.union({(country_general, jobID)
                                               for jobID in list(scrapID(page))
                                               })
                        start += limit
            setID = setID.union(listID)
    return setID

""
def dicoFromScrap(tupleID):
    """
    Normalize the data of the request response
    :tupleID: tuple of country code and Indeed job ID
    :return: standard dictionary of useful elements
    """
    dico = {}
    url = "https://www.indeed.com/viewjob?jk={}".format(tupleID[1])
    try:
        page = scrapPage(url)
    except HTTPError:
        return dico

    def postedDate(page):
        """
        Extract the posting date in isoformat
        :page: html page
        :return: str, isoformat date
        """
        try:
            date = int(
                re.findall(
                    r'-?\d+\.?\d*',
                    page.find("div", {
                        "class": "jobsearch-JobMetadataFooter"
                    }).text)[0])
        except IndexError:
            posted = datetime.now().isoformat(timespec='seconds')
        else:
            posted = (datetime.now() +
                      timedelta(days=-date)).isoformat(timespec='seconds')
            if date == 30: posted = "+ " + posted
        return posted

    def companyName(page):
        """
        Extract the company name
        :page: html page
        :return: str
        """
        try:
            name = page.find("div", {"class": "icl-u-lg-mr--sm"}).text
        except AttributeError:
            try:
                name = page.find("span", {
                    "class": "icl-u-textColor--success"
                }).text
            except:
                name = ""
        return name

    dico["country"] = tupleID[0].upper()
    dico["url"] = url
    dico["description"] = page.find(id="jobDescriptionText").text
    dico["header"], dico["city"], *_ = page.head.title.text.split(" - ")
    dico["company"] = companyName(page)
    dico["type"] = dico["category"] = ""
    dico["posted"] = postedDate(page)

    return dico

""
def IndeedScrap(searchList, countryList):
    """
    Extract and normalizes data from the search results
    :searchList: list of jobs or keywords to search
    :country: list of countries in 2-letter code
    :return: list of standard dictionaries
    """
    scraped = list()
    setID = scrapIndeedID(searchList, countryList)
    if len(setID) < 20:
        workers = len(setID)
    else:
        workers = len(setID) / 5
    with ThreadPoolExecutor(workers) as executor:
        for result in executor.map(dicoFromScrap, setID):
            scraped.append(result)
    return scraped