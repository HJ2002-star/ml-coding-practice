# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

ServiceKey = "e1d1d77bd869d9672ca4771cd945b558e0d3541f7810715ba8ed6d2c83dd13f4"

"""### [CODE 0]"""

def main():
    jsonResult = []
    result = []

""" [CODE 3]"""

def getTourusmStatsService(nat_cd, ed_ed, nStartYear, nEndYear):
    jsonResult = []
    result = []

""" [CODE 2]"""

def getTourusmStatsItem(yyymm, nat_cd, ed_cd):
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"