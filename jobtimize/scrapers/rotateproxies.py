#!/usr/bin/env python
# coding: utf-8

__author__ = 'Lrakotoson'
__copyright__ = 'Copyright 2020, Jobtimize'
__license__ = 'MIT'
__version__ = '0.0.2'
__maintainer__ = 'Loïc Rakotoson'
__email__ = 'contact@loicrakotoson.com'
__status__ = 'planning'
__all__ = ['RotateProxies']

""
from bs4 import BeautifulSoup
from itertools import cycle
from requests import get
""
class RotateProxies:
    """
    Allows a rotation of proxies, to be used in HTTPS queries.
    """
    def __init__(self):
        self.proxies = self.collectProxies()
    
    def collectProxies(self):
        """
        Collects proxies (IP:Port)
        :return: cyclic iterator of dict
        """
        url = "https://free-proxy-list.net/"
        table = BeautifulSoup(get(url).text, 'html.parser').find(
            'table', attrs={'id': 'proxylisttable'})

        proxies = cycle([{
            "https":
            "{}:{}".format(
                row.find_all('td')[0].string,
                row.find_all('td')[1].string)
        } for row in table.find_all('tr') if len(row.find_all('td')) > 1
                         and row.find_all('td')[6].string == "yes"])

        return proxies
    
    def next(self):
        """
        Iterator protocol
        :return: dict of one proxy
        """
        test_url = 'https://httpbin.org/ip'
        proxy = None
        while True:
            proxy = next(self.proxies)
            try:
                test = get(test_url, proxies = proxy)
            except:
                continue
            else:
                break
        return proxy