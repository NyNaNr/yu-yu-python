# -*- coding: utf-8 -*-

import csv
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
    N = 25270000000000  # インデックス数(任意の値で)
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


def csvAutoLoader(readCsvFile, resultCsvFile):
    # 書き込み専用のCSVファイル
    with open(resultCsvFile, "w", encoding="utf-8") as write_file:
        # 書き込みにあたってのheader宣言
        fieldnames = ["Word_1", "Word_2", "NGD_Value"]
        writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        writer.writeheader()
        count_row = 0
        # 読み込み専用のCSVファイル
        with open(readCsvFile, encoding="utf-8") as read_file:
            for row in read_file:
                count_row += 1
                searchCounts = []
                words = row.rstrip().split(",")
                for word in words:
                    searchCounts.append(getSearchCount(word))
                searchCounts.append(getSearchCount(words[0] + " " + words[1]))
                ngd = str(ngdCalculator(searchCounts))
                print(str(count_row) + "行目完了")
                writer.writerow(
                    {"Word_1": words[0], "Word_2": words[1], "NGD_Value": ngd}
                )


# 第一引数に調べたいファイル. 第二引数に結果として出力する際のファイル名を入れてください.
csvAutoLoader("test.csv", "test_result.csv")
