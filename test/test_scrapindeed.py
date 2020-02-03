# coding: utf-8

""
import sys
sys.path.append("..")

""
from Jobtimize.scrapindeed import IndeedScrap, scrapIndeedID, dicoFromScrap
import pytest

""
class TestIndeed:
    searchList = ["Data Analyst nantes"]
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
    
    def test_scraped_prox(self):
        try:
            scraped_Prox = IndeedScrap(["Data Analyst nantes"], ["FR"], prox = True)
        except:
            assert False
        else:
            assert True