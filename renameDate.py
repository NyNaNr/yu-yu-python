# renameDate.py 米国式日付(MM-DD-YYYY)を欧州式日付(DD-MM-YYYY)に変換

import shutil, os, re

#米国式日付のファイル名にマッチする正規表現を作る。

date_pattern_america = re.compile(r'''
^(.*?) # 日付の前の全テキスト
((1|0)?\d)-  #月を表す1,2桁の数字
((0|1|2|3)?\d)-   #日付を表す1,2桁の数字
((19|20)\d{2})
(.*?)$
''', re.VERBOSE)

# カレントディレクトリを示す
print(os.getcwd())

# カレントディレクトリの全ファイルをループする。
for america_filename in os.listdir('.'):
    mo = date_pattern_america.search(america_filename)
    
    # 日付のないファイルはスキップ
    if mo == None:
        continue

    #ファイル名を分解

    before_part = mo.group(1)
    month_part = mo.group(2)
    date_part = mo.group(3)
    year_part = mo.group(4)
    after_part = mo.group(5)

    # 欧州式の日付のファイル名を作る。
    euro_filename = before_part + date_part + '-' + month_part + '-' + year_part + after_part

    # ファイル名を変更する。
    print('Renaming "{}" to "{}" ...'.format(america_filename, euro_filename))
    # shutil.move(america_filename, euro_filename) #テスト後にコメントアウト

