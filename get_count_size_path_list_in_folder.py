import os

''' 

指定のフォルダ内のファイルの絶対パスをリスト化し、合計ファイル数・ファイルサイズを示す。


'''

print('カレントフォルダ',  os.getcwd())
folder = os.getcwd()

# for foldername, subfolders, filenames in os.walk(folder):
#     print('========================')
#     print('現在のディレクトリ：', foldername)
#     print('内包するディレクトリ：', subfolders)
#     print('内包するファイル：', filenames)


# print('=====================================')

# 以下自分で考えたクソコード 敗因は、絶対パスの作り方がくそ。実際にないパスを書きだす。 気づかずに１時間以上無駄に

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


file_count = 0
file_size = 0


# 特定のフォルダのパスを指定する
folder_path = r"C:\Users\yu_yu\OneDrive\デスクトップ\Git"

# フォルダ内のすべてのファイルの絶対パスを取得する
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)

for file_path in file_paths:
    print(file_path)
    file_count += 1
    file_size += os.path.getsize(file_path)

# byte => MB & round
file_size /= (1024*1024)
file_size = round(file_size, 2)

print('=====================================')
print('ファイル数', str(file_count))
print('ファイル合計サイズ:', file_size, 'MB')
