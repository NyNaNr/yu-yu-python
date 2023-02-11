# -*- coding: utf-8 -*-


import csv
import math
import sys
import re
from urllib.parse import urlparse

import bs4
import requests  # urlを読み込むためrequestsをインポート


class NgdProcessor:
    """
    NGDに関する処理を行うクラス
    """

    # Google検索時のURL
    BASE_URL = "https://www.google.com/search?q="

    # ヘッダー情報
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    # パーサー設定
    PARSER_SETTING = "html.parser"

    # インデックスの設定値（任意の値）
    INDEX_VALUE = 25270000000000

    def getResponseBodyText(self, query:str) -> str:
        """
        引数のqueryを検索ワードに設定後、Google検索を行い、レスポンスボディの結果をテキストとして返却する。

        Args:
            query (str): 検索クエリ

        Returns:
            str: レスポンスボディのテキスト
        """
        try:
            response = requests.get(
                url = self.BASE_URL + str(query)
                , headers = self.HEADERS
            )
            # HTTPステータスコードを確認し、200番台以外の場合のみ、例外を発生させる
            response.raise_for_status

            return response.text
        except requests.exceptions.RequestException as e:
            print(e)

    def extractResultStats(self, response_text:str) -> str:
        """
        レスポンスボディのテキストから「検索結果の件数」を抽出し、返却する

        Args:
            response_text (str): 検索結果のレスポンスボディ内容（テキスト）

        Returns:
            str: 検索結果件数（例.39800000）
        """
        soup = bs4.BeautifulSoup(response_text, self.PARSER_SETTING)
        try:
            result_stats = soup.find("div", {"id": "result-stats"}).text
        except AttributeError as e:
            print(e)

        # 正規表現により数値情報を抽出する
        result = re.match('約 (.+) 件', result_stats).groups()[0]
        result = result.replace(',', '')
        result = int(result)

        return result

    # NGDの値を返す
    def calculateNgd(self, fx_value:int, fy_value:int, fxy_value:int) -> float:
        """NGDの値を計算し、返却する

        Args:
            fx_value (int): fx値
            fy_value (int): fy値
            fxy_value (int): fxy値

        Returns:
            float: NGD値
        """
        logfx = math.log(fx_value)
        logfy = math.log(fy_value)
        logfxy = math.log(fxy_value)
        logN = math.log(self.INDEX_VALUE)
 
        if logfx > logfy:
            max, min = logfx, logfy
        else:
            max, min = logfy, logfx

        # 0除算回避
        try:
            result = (max - logfxy) / (logN - min)
            result = round(result, 2)
        except ZeroDivisionError:
            result = 0

        return result

    # TODO:あとで直す
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
                    searchCounts.append(getSearchCount(words[0] + "+" + words[1]))
                    ngd = str(ngdCalculator(searchCounts))
                    print(str(count_row) + "行目完了")
                    writer.writerow(
                        {"Word_1": words[0], "Word_2": words[1], "NGD_Value": ngd}
                    )

# TODO:あとで直す
# 第一引数に調べたいファイル. 第二引数に結果として出力する際のファイル名を入れてください.
csvAutoLoader("test.csv", "test_result.csv")


# getSearchCount()
# print('NGD:',ngdCalculator(searchCountlist))
