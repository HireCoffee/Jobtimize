#!/usr/bin/env python
# coding: utf-8

"""
Jobtimize main functions.
Use:
>>> from Jobtimize import jobscrap
"""

__author__ = 'Lrakotoson'
__copyright__ = 'Copyright 2020, Jobtimize'
__license__ = 'MIT'
__version__ = '0.1.1'
__maintainer__ = 'Loïc Rakotoson'
__email__ = 'contact@loicrakotoson.com'
__status__ = 'planning'
__all__ = ['jobscrap']

""
from .scrapindeed import IndeedScrap
from .scrapmonster import MonsterScrap
import pandas as pd
import warnings
""
def jobscrap(searchList, countryList, prox = False):
    """
    Extract and normalizes data from the search results
    :searchList: list of jobs or keywords to search
    :country: list of countries in 2-letter code
    :prox: if True use proxy, default False
    :return: pandas dataframe
    """
    if prox:
        warnings.warn("Using a proxy extends execution time", UserWarning)
        
    countries = [
        'AE', 'AR', 'AT', 'AU', 'BE', 'BH', 'BR', 'CA', 'CH', 'CL', 'CN', 'CO',
        'CZ', 'DE', 'DK', 'ES', 'FI', 'FR', 'GB', 'GR', 'HK', 'HU', 'ID', 'IE',
        'IL', 'IN', 'IT', 'JP', 'KR', 'KW', 'LU', 'MX', 'MY', 'NL', 'NO', 'NZ',
        'OM', 'PE', 'PH', 'PK', 'PL', 'PT', 'QT', 'RO', 'RU', 'SA', 'SE', 'SG',
        'TH', 'TR', 'TW', 'US', 'VE', 'VN', 'ZA'
    ]
    countryList = [country for country in countryList if country in countries]

    indeed = IndeedScrap(searchList, countryList, prox)
    monster = MonsterScrap(searchList, countryList, prox)
    # add here other sites in the same format

    jobData = pd.DataFrame(indeed + monster,
                           columns = [
                               "header", "company", "city", "country",
                               "posted", "description", "type", "category",
                               "url"
                           ])
    return jobData