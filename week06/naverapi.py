# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = '1muCmJeI4Ctd8uQEVZeo'
client_secret = 'qUut4pYmqh'

def main():

    node = 'news'                   # 크롤링할 대상
    srcText = input('검색어를 입력하세요: ')    

    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)    #[CODE 2
    total = jsonResponse['total']

def getNaverSearch(node, srcText, page_start, display):

def getRequestUrl(url):
    req = urllib.request.Request(url)

def getPostData(post, jsonResult, cnt): #[CODE 3]