# renameDate.py 米国式日付(MM-DD-YYYY)を日本式日付yyyy年mm月dd日に変換

import shutil
import os
import re

# 米国式日付のファイル名にマッチする正規表現を作る。

date_pattern_america = re.compile(r'''
^(.*?) # 日付の前の全テキスト
([1-9]|1[0-2])-  #月を表す1,2桁の数字 
([1-9]|[012]\d|3[01])-   #日付を表す1,2桁の数字　(0|1|2|3)?\d
((19|20)\d\d)  #西暦
(.*?)$        #あとのテキストと拡張子
''', re.VERBOSE)

# カレントディレクトリを示す
print(os.getcwd())

# カレントディレクトリの全ファイルをループする。
for america_filename in os.listdir('.'):
    mo = date_pattern_america.search(america_filename)

    # 日付のないファイルはスキップ
    if mo == None:
        continue

    # ファイル名を分解

    before_part = mo.group(1)
    month_part = mo.group(2)
    date_part = mo.group(3)
    year_part = mo.group(4)
    trash = mo.group(5)     # 正規表現　((19|20)\d\d)  #西暦　の(19|20)がグループ5にあたる
    after_part = mo.group(6)

    # 日本式の日付を作る。
    japan_filename = before_part + year_part + '年' + \
        month_part + '月' + date_part + '日' + after_part

    # ファイル名を変更する。
    print('Renaming "{}" to "{}" ...'.format(america_filename, japan_filename))
    shutil.move(america_filename, japan_filename)  # テスト後にコメントアウト
