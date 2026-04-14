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
    nStartYear = int(input('데이터를 몇 년부터 수집할까요? : '))
    eEndYear = int(input('데이터를 몇 년까지 수집할까요? : '))
    ed_cd = "E" #E: 방한외래관광객, D: 해외 출국

    jsonResult, result, natName, dataEND = getTourusmStatsService(nat_cd, ed_ed, nStartYear) #[CODE 3]

    #파일저장 :  csv 파일
    columns = ["입국자국가", "국가코드", "입국연월", "입국자 수"]
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