import os
import time
import pprint

''' 

指定のフォルダ内のファイルの絶対パスをリスト化し、合計ファイル数・ファイルサイズを取得
ファイルサイズ順にTOP20を示す
実行環境（OS）を問わず実行できる

'''

# TODO: 型ヒントをつける


class get_file_info:

    def ask_for_folder_path(self):
        while True:
            path = input('調べたいフォルダのパスを入力してください: ')
            if os.path.exists(path):
                folder_path = os.path.normpath(path)
                break
            else:
                print('入力されたパスが存在しません。もう一度入力してください。')
        start_time = time.time()
        return start_time, folder_path

    def get_list_of_all_file_path(self, folder_path):  # フォルダ内のすべてのファイルの絶対パスを取得する
        file_paths = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
        return file_paths

    def make_dict_filepath_and_size(self, file_paths):
        each_file_path = {}
        file_size = 0
        file_count = 0
        for file_path in file_paths:
            file_count += 1
            each_file_path[file_path] = str(
                round(int(os.path.getsize(file_path)) / (1024*1024), 2)
            ) + 'MB'
            file_size += os.path.getsize(file_path)
        return each_file_path, file_size, file_count

    def convert_to_byte_to_mb(self, file_size):
        # byte => MB & round
        file_size /= (1024*1024)
        file_size = round(file_size, 2)
        return file_size

    def measure_processing_time(self, start_time):
        end_time = time.time()
        elapsed_time = end_time - start_time
        return elapsed_time

    def sort_dict_by_size_and_get_top_20(self, each_file_path):
        # 辞書を値をサイズ順にソートする
        sorted_dict = sorted(each_file_path.items(),
                             key=lambda x: x[1], reverse=True)
        # トップ20を取得する
        top20_dict = dict(sorted_dict[:20])
        return top20_dict

    def print_results(self, file_count, file_size, elapsed_time, top20_dict):
        print('=====================================')
        print('ファイル数', str(file_count))
        print('ファイル合計サイズ:', file_size, 'MB')
        print("実行時間（s）:", round(elapsed_time, 2), '(s)')
        print('=====================================')
        pprint.pprint(top20_dict)

    def execute(self):
        start_time, folder_path = self.ask_for_folder_path()
        file_paths = self.get_list_of_all_file_path(folder_path)
        each_file_path, file_size, file_count = self.make_dict_filepath_and_size(
            file_paths)
        file_size = self.convert_to_byte_to_mb(file_size)
        elapsed_time = self.measure_processing_time(start_time)
        top20_dict = self.sort_dict_by_size_and_get_top_20(each_file_path)
        self.print_results(file_count, file_size, elapsed_time, top20_dict)


if __name__ == '__main__':
    get_file_info = get_file_info()
    get_file_info.execute()
