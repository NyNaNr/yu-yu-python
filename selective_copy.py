# ディレクトリ全体を連番付きのZIPファイルにコピーする

'''
コピー先のフォルダを作成。日付と、フォルダ名と、拡張子からなる　例　2023-04-18_foldername_txt
新フォルダをwで作成。この時の名前は、上で決めたやつ
os.walk ですべてのファイルのパスを取得。この時特定の拡張子のみリストに追加する。
リストを元にファイルをコピー。コピー先は、最初に作ったやつ

'''

import os
from pathlib import Path
import datetime
import pyinputplus as pyip
import sys
import shutil

today = datetime.date.today()
print(today)
# 第一引数は、検索したいフォルダパス。第二引数は、拡張子。
# コピー先は、ホームディレクトリ（ユーザー）に


def selective_copy(folder, ext):
    folder = os.path.abspath(folder)  # 絶対パス化＆パスオブジェクト化

    # 本日の日付、フォルダ名からフォルダ名を決める

    selective_foldername = f'{today}_{os.path.basename(folder)}_{ext}_selection'
    # コピー先のフォルダを作成
    print(f'Creating {selective_foldername}')
    DESTINATION_FOLDER_PATH = os.path.join(Path.home(), selective_foldername)

    if os.path.exists(DESTINATION_FOLDER_PATH):
        if (pyip.inputYesNo(prompt=f'{selective_foldername}は既に存在しています。上書きしますか？:Yes or No:')) == 'no':
            print('プログラムを終了しました。')
            sys.exit()

    os.makedirs(DESTINATION_FOLDER_PATH, exist_ok=True)
    print(f'{DESTINATION_FOLDER_PATH}にフォルダを作成しました。')

    # ディレクトリのツリーを渡り歩いてextを含むファイルをDESTINATIONにコピー
    for foldername, subfolders, filenames in os.walk(folder):
        # 現在のディレクトリないの全ファイルをZIPに追加

        for filename in filenames:
            # ファイルの絶対パスを取得
            SOURCE_FILE_PATH = os.path.join(foldername, filename)
            # 拡張子の検査
            if not '.' in ext:  # py => .py になる。　もしこれがないと、.pypyもOKになってしまう
                ext = '.'+ext[:]

            if filename.endswith(ext):
                shutil.copy(SOURCE_FILE_PATH, DESTINATION_FOLDER_PATH)
                print(SOURCE_FILE_PATH)

    print('Done')


selective_copy(r'C:\Users\yu_yu\OneDrive\デスクトップ\Git', 'py')
