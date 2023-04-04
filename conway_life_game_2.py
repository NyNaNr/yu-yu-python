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
        num_neighbors = 0
        if current_cells[left_coord][above_coord] == '#':
            num_neighbors += 1  # 左上が生きたセル
        if current_cells[x][above_coord] == '#':
            num_neighbors += 1  # 上が生きたセル
        if current_cells[right_coord][above_coord] == '#':
            num_neighbors += 1  # 右上が生きたセル
        if current_cells[left_coord][y] == '#':
            num_neighbors += 1  # 左が生きたセル
        if current_cells[right_coord][y] == '#':
            num_neighbors += 1  # 右が生きたセル
        if current_cells[left_coord][below_coord] == '#':
            num_neighbors += 1  # 左下が生きたセル
        if current_cells[x][below_coord] == '#':
            num_neighbors += 1  # 下が生きたセル
        if current_cells[right_coord][below_coord] == '#':
            num_neighbors += 1  # 右下が生きたセル

        # TODO: #conwayのライフゲームのルールに基づきセルを設定
