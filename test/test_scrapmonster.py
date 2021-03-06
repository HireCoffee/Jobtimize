# coding: utf-8

""
import sys
sys.path.append("..")

""
from jobtimize.scrapers.scrapmonster import MonsterScrap, scrapMonsterID, dicoFromJson
import pytest

""
class TestMonster:
    searchList = ["Data Analyst"]
    countryList = ["FR"]
    
    monsterID = scrapMonsterID(searchList, countryList)
    scraped = MonsterScrap(searchList, countryList)

    dicojson = {
        'country': str(),
        'url': str(),
        'description': str(),
        'header': str(),
        'city': str(),
        'company': str(),
        'type': str(),
        'category': str(),
        'posted': str()
    }
    if len(list(monsterID)) > 0:
        dicojson = dicoFromJson((list(monsterID)[0], None))
    
    def test_scrapID(self):
        assert isinstance(self.monsterID, (set, list))
        
    def test_dicojson(self):
        assert len(self.dicojson) == 9
    
    # def test_scraped_len(self):
    #     assert len(self.monsterID) == len(self.scraped)