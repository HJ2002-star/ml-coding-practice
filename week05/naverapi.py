# -*- coding: uft-8 -*-
import urllib.request
import datetime
import json

client_id = '1muCmJeI4Ctd8uQEVZeo'
client_secret = 'qUut4pYmqh'

def main():

    node = 'news'
    srcText = input('검색어를 입력하세요: ')

    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch()