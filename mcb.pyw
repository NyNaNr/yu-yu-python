#! python3
# クリップボードのテキストの保存・復元
# How to use
# py.exe mcb.pyw save <keyword> クリップボードにキーワードを紐づけてコピー
# py.exe mcb.pyw delete <keyword> キーワードと紐づけされた値を削除
# py.exe mcb.pyw <keyword> キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb.pyw list 全キーワードをクリップボードにコピー

import shelve
import pyperclip
import sys

mcb_shelve = shelve.open('mcb')

# クリップボードに内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelve[sys.argv[2]] = pyperclip.paste()
    print(f'{sys.argv[2]}の内容を保存しました。')
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    try:
        del mcb_shelve[sys.argv[2]]
        print(f'{sys.argv[2]}の内容を削除しました。')
    except KeyError:
        print(f'{sys.argv[2]}はありません。')
elif len(sys.argv) == 2:
    # キーワード一覧と内容の読み込み
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelve.keys())))
        print('クリップボードに全キーワードをコピーしました。')
    elif sys.argv[1] in mcb_shelve:
        pyperclip.copy(mcb_shelve[sys.argv[1]])
        print(f'クリップボードに{sys.argv[1]}をコピーしました。')
    else:
        print(
            f'{sys.argv[1]}は保存されていません。 コマンドライン上でsave {sys.argv[1]} をしてください。')
mcb_shelve.close()


'''
反省
if sys.argv[1].lower() == 'list':である必要があるのに
間違えてif sys.argv[1].lower == list:
としてしまっていた。
lowerの後ろに()がないと動かないし、'list'と引用府で囲わないと、文字として扱われない。
'''
