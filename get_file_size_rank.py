import os
import time
import pprint

''' 

指定のフォルダ内のファイルの絶対パスをリスト化し、合計ファイル数・ファイルサイズを示す。
実行環境（OS）を問わず実行できる

'''


# フォルダないのファイルを調べる
# フォルダ内のファイルを合計
# 　辞書にフォルダパスとサイズを記録　　並行してファイルのパスとサイズを辞書に保管
# 　ソートする。

print('カレントフォルダ',  os.getcwd())
folder = os.getcwd()

# for foldername, subfolders, filenames in os.walk(folder):
#     print('========================')
#     print('現在のディレクトリ：', foldername)
#     print('内包するディレクトリ：', subfolders)
#     print('内包するファイル：', filenames)


# print('=====================================')

# 以下自分で考えたクソコード 敗因は、絶対パスの作り方がくそ。実際にないパスを書きだす。 気づかずに時間が無駄に

# for foldername, subfolders, filenames in os.walk(folder):
#     for filename in filenames:
#         for subfolder in subfolders:
#             file_abs_path = os.path.join(folder, subfolder, filename)　　# ここの行がクソofクソ　存在しないパスを作り出す。
#             # print(file_abs_path)
#             file_count += 1
#             try:
#                 file_size += os.path.getsize(file_abs_path)
#             except FileNotFoundError:
#                 pass

def get_file_info(folder_path):

    start_time = time.time()
    file_count = 0
    file_size = 0
    each_file_path = {}

    # フォルダ内のすべてのファイルの絶対パスを取得する
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    for file_path in file_paths:
        # print(file_path)
        file_count += 1
        each_file_path[file_path] = str(
            round(int(os.path.getsize(file_path)) / (1024*1024), 2)
        ) + 'MB'

        file_size += os.path.getsize(file_path)

    # byte => MB & round
    file_size /= (1024*1024)
    file_size = round(file_size, 2)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print('=====================================')
    print('ファイル数', str(file_count))
    print('ファイル合計サイズ:', file_size, 'MB')
    print("実行時間（秒）:", round(elapsed_time, 2), '(s)')

    # 辞書を値でソートする
    sorted_dict = sorted(each_file_path.items(),
                         key=lambda x: x[1],)

    pprint.pprint(sorted_dict)


# 調べたいフォルダのパスを入力
while True:
    path = input('調べたいフォルダのパスを入力してください: ')
    if os.path.exists(path):
        path = os.path.normpath(path)
        break
    else:
        print('入力されたパスが存在しません。もう一度入力してください。')

get_file_info(path)
