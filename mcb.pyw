#! python3
# クリップボードのテキストの保存・復元
# How to use
# py.exe mcb.pyw save <keyword> クリップボードにキーワードを紐づけてコピー
# py.exe mcb.pyw <keyword> キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb.pyw list 全キーワードをクリップボードにコピー

import shelve
import pyperclip
import sys

mcb_shelve = shelve.open('mcb')

# クリップボードに内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # キーワード一覧と内容の読み込み
    if sys.argv[1].lower == list:
        pyperclip.copy(str(list(mcb_shelve.keys())))
    elif sys.argv[1] in mcb_shelve:
        pyperclip.copy(mcb_shelve[sys.argv[1]])


mcb_shelve.close()
