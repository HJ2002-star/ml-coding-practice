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

    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    nat_cd = int(input('국가 코드를 입력하세요(중국: 112 / 일본: 130 / 미국: 275) :'))
""" [CODE 3]"""

def getTourusmStatsService(nat_cd, ed_ed, nStartYear, nEndYear):
    jsonResult = []
    result = []

""" [CODE 2]"""

def getTourusmStatsItem(yyymm, nat_cd, ed_cd):
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

""" [CODE 1]"""

def getRequestUrl(url1): #[CODE 1]
    req = urllib.request.Request(url)

main()