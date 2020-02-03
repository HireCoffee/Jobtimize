#!/usr/bin/env python
# coding: utf-8

__author__ = 'Lrakotoson'
__copyright__ = 'Copyright 2019, Jobtimize'
__license__ = 'MIT'
__version__ = '0.1.1'
__maintainer__ = 'Loïc Rakotoson'
__email__ = 'contact@loicrakotoson.com'
__status__ = 'planning'
__all__ = ['MonsterScrap']

""
from .rotateproxies import RotateProxies
from requests import get, Timeout
from requests.exceptions import HTTPError, ProxyError
from concurrent.futures import ThreadPoolExecutor
from itertools import islice
from bs4 import BeautifulSoup
from unicodedata import normalize
from json import loads
import re
""
def scrapBody(url, proxy = None):
    """
    Take the body part of an html document from the URL
    :url: page url
    :proxy: dict of one proxy, default None
    :return: html body, BeautifulSoup object
    """
    with get(url, proxies = proxy) as response:
        body = BeautifulSoup(response.text, 'html.parser').body
    return body

""
def idFromLink(link):
    """
    Extract the job ID from the monster url
    :link: Monster job url
    :return: job ID, str
    """
    if ".aspx" in link:
        jobID = link[-14:-5]
    elif "/monster/" in link:
        jobID = re.findall(r'monster/.+?\?', link)[0][8:-1]
    else:
        jobID = link[link.rfind('/')+1:]
    return jobID

""
def scrapMonsterID(searchList, countryList, prox = False):
    """
    Extract jobIDs from the search results provided by Monster
    :searchList: list of jobs or keywords to search
    :country: list of countries in 2-letter code
    :prox: if True use proxy, default False
    :return: list of jobIDs
    """
    setID = set()
    for search in searchList:
        search = search.replace(" ","+")
        if prox: proxies = RotateProxies()
        proxy = None
        for country in countryList:
            match = 5001
            error = 0
            listID = set()
            page = 1
            while True:
                url = "https://www.monster.co.uk/medley?q={}&fq=countryabbrev_s%3A{}&pg={}".format(
                    search, country, page)
                if page % 50 == 0 and prox: proxy = proxies.next()
                try:
                    body = scrapBody(url, proxy)
                except HTTPError:
                    break
                else:
                    if body.find(id="resultCountLabel") is None:
                        if len(listID) == 0:
                            break
                        else:
                            error += 1
                            if len(listID) >= (match - 20 * error):
                                break
                            else:
                                page += 1
                                continue
                    else:
                        match = int(
                            re.sub(
                                "\D", "",
                                body.find(
                                    id="resultCountLabel").text.split()[-1]))
                        links = [
                            link.a.attrs['href']
                            for link in body.find_all("div", class_="jobTitle")
                        ]
                        listID = {idFromLink(link) for link in links}
                        page += 1
                setID = setID.union(listID)
    return setID
""
def dicoFromJson(args):
    """
    Normalize the data of the request response
    :args: tuple of jobID and proxy
    :jobID: Monster job ID
    :proxy: dict of one proxy or None
    :return: standard dictionary of useful elements
    """
    jobID, proxy = args
    url = "https://job-openings.monster.com/v2/job/pure-json-view?jobid={}".format(
        jobID)
    try:
        query = get(url, proxy).text
    except HTTPError:
        return {}
    dico = json.loads(
        normalize('NFKD', query).encode('ascii', 'ignore'))

    general = (("description", "jobDescription"),
               ("country", "jobLocationCountry"),
               ("city", "jobLocationCity"),
               ("posted", "postedDate"))
    company = (("header", "companyHeader"),
               ("company", "name"))
    tracks = (("type", "eVar33"),
              ("category", "eVar28"))

    ginfo, cinfo, tinfo = {}, {}, {}
    for g in general:
        try:
            ginfo[g[0]] = normalize(
                "NFKD",
                " ".join(BeautifulSoup(dico[g[1]], 'lxml').get_text().split()))
        except KeyError:
            ginfo[g[0]] = ""
    for c in company:
        try:
            cinfo[c[0]] = BeautifulSoup(dico["companyInfo"][c[1]],
                                        'lxml').get_text().rstrip()
        except KeyError:
            cinfo[c[0]] = ""
    for t in tracks:
        try:
            tinfo[t[0]] = BeautifulSoup(dico["adobeTrackingProperties"][t[1]],
                                        'lxml').get_text().rstrip()
        except KeyError:
            tinfo[t[0]] = ""
    
    dico = {**ginfo, **cinfo, **tinfo}
    dico["url"] = "https://job-openings.monster.co.uk/monster/{}".format(jobID)
    return dico

""
def MonsterScrap(searchList, countryList, prox = False):
    """
    Extract and normalizes data from the search results
    :searchList: list of jobs or keywords to search
    :country: list of countries in 2-letter code
    :prox: if True use proxy, default False
    :return: list of standard dictionaries
    """
    scraped = list()
    setID = scrapMonsterID(searchList, countryList, prox)
    if len(setID) < 20:
        workers = len(setID)
    else:
        workers = len(setID) // 5
    
    if prox:
        proxies = list(islice(RotateProxies().proxies, workers)) * len(setID)
    else:
        proxies = [None] * len(setID)
    
    with ThreadPoolExecutor(workers) as executor:
        for result in executor.map(dicoFromJson, zip(setID, proxies)):
            scraped.append(result)
    return scraped