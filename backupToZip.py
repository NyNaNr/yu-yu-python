# ディレクトリ全体を連番付きのZIPファイルにコピーする

'''
バックアップを作成するフォルダに連番がないか調べ、あれば続きを。なければ、1を作成。
新規zipファイルをwで作成。この時の名前は、上で決めたやつ
os.walk ですべてのファイルのパスを取得

さっき取得したファイルパスをアペンド
'''

import os
import zipfile


def backup_to_zip(folder):
    folder = os.path.abspath(folder)  # 絶対パス化＆パスオブジェクト化

    # 既存のファイルからファイル名を決める
    number = 1
    while True:
        zip_filename = f'{os.path.basename(folder)}_{number}.zip'
        # zip_filename が存在しなければ、その名前で確定。break!
        if not os.path.exists(zip_filename):
            break
        number += 1

    # zipファイルを作成
    print(f'Creating {zip_filename}')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # ディレクトリのツリーを渡り歩いてその中のファイルを圧縮する。

    new_base = os.path.basename(folder) + '_'
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # 現在のディレクトリをZIPファイルに追加
        backup_zip.write(foldername)

        # 現在のディレクトリないの全ファイルをZIPに追加
        for filename in filenames:
            if filename.startswith(new_base) and filename.endswith('zip'):
                continue  # バックアップ用のZIPはバックアップに含めない
            backup_zip.write(os.path.join(foldername, filename))

    backup_zip.close()
    print('Done')


backup_to_zip(r'C:\Users\~~~~')
