# -*- coding: utf-8 -*-


import csv
import math
import sys
import re
from urllib.parse import urlparse
import pandas as pd

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

    # 書き込みcsvのヘッダーとなる値
    FIELD_NAMES = ["Word_1", "Word_2", "NGD_Value"]

    def get_response_body_text(self, query:str) -> str:
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

    def extract_result_stats_by_word(self, word:str) -> str:
        """
        検索単語によって取得したレスポンスボディのテキストから「検索結果の件数」を抽出し、返却する

        Args:
            word (str): 検索単語

        Returns:
            str: 検索結果件数（例.39800000）
        """
        response_text = self.get_response_body_text(word)
        soup = bs4.BeautifulSoup(response_text, self.PARSER_SETTING)
        try:
            result_stats = soup.find("div", {"id": "result-stats"}).text
        except AttributeError as e:
            print(e)

        # 正規表現により数値情報を抽出する
        result = re.match('約 (.+) 件', result_stats).groups()[0]
        result = result.replace(',', '')
        print(result)
        result = int(result)

        return result

    # NGDの値を返す
    def calculate_ngd(self, fx_value:int, fy_value:int, fxy_value:int) -> float:
        """
        NGDの値を計算し、返却する

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

    def read_csv_to_list(self, r_path:str) -> list:
        """
        CSVを読み込み、リスト化して返却する
        例えばCSVの中身が
            apple,banana
            wakayama,osaka
        だった場合、下記のようなリストが生成される
            [
                ['apple','banana'],
                ['wakayama','osaka']
            ]

        Args:
            r_path (str): 読み込むcsvファイルのパス

        Returns:
            list: 2次元リスト
        """
        df = pd.read_csv(r_path, header=None)
        result = df.values.tolist()

        return result

    def execute(self, r_path:str, w_path:str):
        """
        <メインの実行処理>
        ①検索に使用する単語データの読み込み
        ②検索単語を用いて検索結果件数の取得
        ③NGDの算出
        ④結果の書き込み
        ⑤検索単語の組み合わせ分、②〜④を繰り返す

        Args:
            r_path (str): 読み込み先のCSVのファイルパス
            w_path (str): 書き込み先のCSVのファイルパス
        """
        word_list = self.read_csv_to_list(r_path)
        with open(w_path, "w", encoding="utf-8") as w_file:
            writer = csv.DictWriter(w_file, fieldnames=self.FIELD_NAMES)
            writer.writeheader()
            for wl in word_list:
                # 検索する2単語
                word_1, word_2 = wl[0], wl[1]

                # word_1、word_2、word_1+word_2の3種類それぞれで検索した場合の検索結果件数を取得
                fx_value = self.extract_result_stats_by_word(word_1)
                fy_value = self.extract_result_stats_by_word(word_2)
                fxy_value = self.extract_result_stats_by_word(word_1 + "+" + word_2)

                # NGDの算出
                ngd_result = self.calculate_ngd(fx_value, fy_value, fxy_value)

                # 結果の書き込み
                writer.writerow(
                    {
                        self.FIELD_NAMES[0]: word_1
                        , self.FIELD_NAMES[1]: word_2
                        , self.FIELD_NAMES[2]: str(ngd_result)
                    }
                )


if __name__ == '__main__':
    ngd_processor = NgdProcessor()
    ngd_processor.execute(
        r_path="test.csv",           # 読み込み先のCSVのファイルパス
        w_path="test_result.csv"     # 書き込み先のCSVのファイルパス
    )

