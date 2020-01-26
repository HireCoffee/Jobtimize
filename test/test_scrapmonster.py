# coding: utf-8

""
import sys
sys.path.append("..")

""
from Jobtimize.scrapmonster import MonsterScrap, scrapMonsterID, dicoFromJson
import pytest

""
class TestMonster:
    searchList = ["Data Analyst nantes"]
    countryList = ["FR"]
    
    monsterID = scrapMonsterID(searchList, countryList)
    dicojson = dicoFromJson(list(monsterID)[0])
    scraped = MonsterScrap(searchList, countryList)
    
    def test_scrapID(self):
        assert isinstance(self.monsterID, (set, list))
        
    def test_dicojson(self):
        assert len(self.dicojson) == 9
    
    def test_scraped_len(self):
        assert len(self.monsterID) == len(self.scraped)