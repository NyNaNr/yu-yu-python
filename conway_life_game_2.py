import random
import time
import copy
WIDTH = 60
HEIGHT = 20

# セルを格納するリストのリストを作成
next_cells = []
for x in range(WIDTH):
    column = []  # 新しい列を作成
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # 生きたセルを追加
        else:
            column.append(' ')  # 死んだセルを追加
    next_cells.append(column)  # next_cells は列のリストのリスト

while True:  # メインプログラム
    print('\n\n\n\n\n')  # ステップ間を開業で分ける
    current_cells = copy.deepcopy(next_cells)

    # current_cellsを表示
    for y in range(HEIGHT):
        # 隣接座標を取得
        # '% WIDTH'により、left_coord を0とWIDTH　- 1 の値にする
        left_coord = (x - 1) % WIDTH
        right_coord = (x + 1) % WIDTH
        above_coord = (y - 1) % HEIGHT
        below_coord = (y + 1) % HEIGHT

        # 生きた隣接セルの数をカウント
