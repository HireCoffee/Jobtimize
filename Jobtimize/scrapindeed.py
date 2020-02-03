#!/usr/bin/env python
# coding: utf-8

__author__ = 'Lrakotoson'
__copyright__ = 'Copyright 2020, Jobtimize'
__license__ = 'MIT'
__version__ = '0.1.0'
__maintainer__ = 'Loïc Rakotoson'
__email__ = 'contact@loicrakotoson.com'
__status__ = 'planning'
__all__ = ['IndeedScrap']

""
from .rotateproxies import RotateProxies
from requests import get, Timeout
from requests.exceptions import HTTPError, ProxyError
from concurrent.futures import ThreadPoolExecutor
from itertools import islice
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import re
""
def scrapPage(url, proxy=None):
    """
    Scrap an html document from the URL
    :url: page url
    :proxy: dict of proxy
    :return: html page, BeautifulSoup object
    """
    with get(url, proxies=proxy) as response:
        page = BeautifulSoup(response.text, 'html.parser')
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
def scrapIndeedID(searchList, countryList, prox=False):
    """
    Extract jobIDs from the search results provided by Indeed
    :searchList: list of jobs or keywords to search
    :country: list of countries in 2-letter code
    :prox: bool, default False
    :return: set of tuples, country and ID
    """
    setID = set()
    for search in searchList:
        search = search.replace(" ", "+")
        if prox: proxies = RotateProxies()
        proxy = None
        for country_general in countryList:
            country = country_general.lower()
            if country == "us": country = "www"  #"us" note redirected
            listID = set()
            limit = 50
            start = repage = count = 0
            match = None
            while (repage <= 101 or len(listID) < match):
                url = "https://{}.indeed.com/jobs?q={}&limit={}&start={}".format(
                    country, search, limit, start)
                if count % 50 == 0 and prox: proxy = proxies.next()
                try:
                    page = scrapPage(url, proxy)
                except (Timeout, ProxyError):
                    if prox:
                        proxy = proxies.next()
                        continue
                    else:
                        break
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
def dicoFromScrap(args):
    """
    Normalize the data of the request response
    :args: tuple of tupleID and proxy
    :tupleID: tuple of country code and Indeed job ID
    :proxy: dict of proxy
    :return: standard dictionary of useful elements
    """
    tupleID, proxy = args
    dico = {}
    url = "https://www.indeed.com/viewjob?jk={}".format(tupleID[1])
    try:
        page = scrapPage(url, proxy)
    except HTTPError:
        return dico

    def postedDate(page):
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
        try:
            name = page.find("div", {"class": "icl-u-lg-mr--sm"}).text
        except AttributeError:
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
def IndeedScrap(searchList, countryList, prox=False):
    """
    Extract and normalizes data from the search results
    :searchList: list of jobs or keywords to search
    :country: list of countries in 2-letter code
    :prox: bool, default False
    :return: list of standard dictionaries
    """
    scraped = list()
    setID = scrapIndeedID(searchList, countryList, prox)

    if len(setID) < 20:
        workers = len(setID)
    else:
        workers = len(setID) // 5

    if prox:
        proxies = list(islice(RotateProxies().proxies, workers)) * len(setID)
    else:
        proxies = [None] * len(setID)

    with ThreadPoolExecutor(workers) as executor:
        try:
            for result in executor.map(dicoFromScrap, zip(setID, proxies)):
                scraped.append(result)
        except:
            pass
    return scraped