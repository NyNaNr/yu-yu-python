import os

file_count = 0
folder_count = 0
for foldername, subfolders, filenames in os.walk(r'C:\Users\yu_yu\OneDrive\デスクトップ\Git'):
    print(f'現在のディレクトリは{foldername}')

    for subfolder in subfolders:
        print(f'{foldername}のサブディレクトリ：{subfolder}')
        folder_count += 1

    for filename in filenames:
        print(f'{foldername}内のファイル{filename}')
        file_count += 1

print(f'ファイルの数は{file_count}')
print(f'フォルダの数は{folder_count}')
