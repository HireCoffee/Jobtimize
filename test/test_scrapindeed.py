# coding: utf-8

""
import sys
sys.path.append("..")

""
from jobtimize.scrapers.scrapindeed import IndeedScrap, scrapIndeedID, dicoFromScrap
import pytest

""
class TestIndeed:
    searchList = ["Data Analyst"]
    countryList = ["FR"]
    
    
    indeedID = scrapIndeedID(searchList, countryList)
    dicoscrap = dicoFromScrap((list(indeedID)[0], None))
    scraped = IndeedScrap(searchList, countryList)
    
    def test_scrapID(self):
        assert isinstance(self.indeedID, (set, list))
        
    def test_dicoscrap(self):
        assert len(self.dicoscrap) == 9
    
    def test_scraped_len(self):
        assert len(self.indeedID) == len(self.scraped)