# -*- coding: utf-8 -*-

import math
import sys
import time

import bs4
import requests


# 検索ヒット数を返す
def getSearchCount(searchWord):
    res = requests.get("https://www.google.co.jp/search?q=" + searchWord)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    searchCount = soup.find(
        id="resultStats"
    ).string  # 例."約 39,800,000 件"という結果で得られる
    number = searchCount.split(" ")[1]
    number = number.replace(",", "")
    return int(number)


# NGDの値を返す
def ngdCalculator(searchCount):
    N = 8058044651  # インデックス数(任意の値で)
    logfx = math.log(searchCount[0])
    logfy = math.log(searchCount[1])
    logfxy = math.log(searchCount[2])
    logN = math.log(N)
    NGD = 0
    max = 0
    min = 0

    if logfx > logfy:
        max = logfx
        min = logfy
    else:
        max = logfy
        min = logfx

    NGD = (max - logfxy) / (logN - min)

    return round(NGD, 2)


# 以下メインの処理
args = sys.argv  # 引数受け取り
words = []
searchCounts = []

# 引数に2単語設定しておかないとエラーを吐くようにする
if len(args) != 3:
    print("調べたい2単語を引数に指定してください")
else:
    flag = False
    for arg in args:
        if flag == False:
            flag = True
            continue
        words.append(arg)
    words.append(words[0] + " " + words[1])
    # 検索ヒット数をsearchCountsに記録する
    for word in words:
        searchCounts.append(getSearchCount(word))

    print(str(ngdCalculator(searchCounts)))
