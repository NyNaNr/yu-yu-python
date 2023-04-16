'''
1人1人にランダムな問題と解答を！！

1.35通りの問題集を作成する。
2.問題集は都道府県を網羅する47問の4択とし、問題の順番はランダムとする。
3.各問題の選択肢は、正解1つと、ランダムな誤答が3つあり、順番はランダムとする。
4.問題集は、35個のテキストファイルに書き出す。
5.怪盗集も35個のテキストファイルに書き出す。

以上のことからコードは次のように動作する必要があります。
1.県と県庁所在地を辞書に記述する。
2.open(),write(),close()を呼び出し問題集と解答集を作成する。
3.random.shuffle()を用いて、問題や選択肢をランダムに並び替える。
'''

import random
from pathlib import Path

capitals = {
    "北海道": "札幌市",
    "青森県": "青森市",
    "岩手県": "盛岡市",
    "宮城県": "仙台市",
    "秋田県": "秋田市",
    "山形県": "山形市",
    "福島県": "福島市",
    "茨城県": "水戸市",
    "栃木県": "宇都宮市",
    "群馬県": "前橋市",
    "埼玉県": "さいたま市",
    "千葉県": "千葉市",
    "東京都": "東京都",
    "神奈川県": "横浜市",
    "新潟県": "新潟市",
    "富山県": "富山市",
    "石川県": "金沢市",
    "福井県": "福井市",
    "山梨県": "甲府市",
    "長野県": "長野市",
    "岐阜県": "岐阜市",
    "静岡県": "静岡市",
    "愛知県": "名古屋市",
    "三重県": "津市",
    "滋賀県": "大津市",
    "京都府": "京都市",
    "大阪府": "大阪市",
    "兵庫県": "神戸市",
    "奈良県": "奈良市",
    "和歌山県": "和歌山市",
    "鳥取県": "鳥取市",
    "島根県": "松江市",
    "岡山県": "岡山市",
    "広島県": "広島市",
    "山口県": "山口市",
    "徳島県": "徳島市",
    "香川県": "高松市",
    "愛媛県": "松山市",
    "高知県": "高知市",
    "福岡県": "福岡市",
    "佐賀県": "佐賀市",
    "長崎県": "長崎市",
    "熊本県": "熊本市",
    "大分県": "大分市",
    "宮崎県": "宮崎市",
    "鹿児島県": "鹿児島市",
    "沖縄県": "那覇市"
}

# 人数分の問題集を作成する。

for quiz_num in range(35):
    # 問題集と解答集のファイルを作成
    quiz_file = open(Path.cwd() / 'randomQuizGenerator' /
                     f'capitalsquiz{quiz_num + 1:02}.txt', 'w', encoding='utf-8')
    answer_key_file = open(Path.cwd() / 'randomQuizGenerator' /
                           f'capitalsquiz_answer{quiz_num + 1:02}.txt', 'w', encoding='utf-8')

    # 問題集のヘッダーを書く
    quiz_file.write('名前：\n\n日付:\n\n学期:\n\n')
    quiz_file.write((' ')*20 + f'都道府県県庁所在地クイズ（問題番号{quiz_num+1}）')
    quiz_file.write('\n\n')
    answer_key_file.write((' ')*20 + f'都道府県県庁所在地クイズ（問題番号{quiz_num+1}）')
    answer_key_file.write('\n\n')

    # 都道府県の順番をシャッフル
    prefectures = list(capitals.keys())
    random.shuffle(prefectures)

    # 47都道府県をループして、それぞれ問題を作成する。
    for question_num in range(len(prefectures)):
        # 正解と誤答を取得
        # さっきrandom.shuffleした都道府県リストをキー(正解の都道府県）に対応する値を取得。
        correct_answer = capitals[prefectures[question_num]]
        wrong_answers = list(capitals.values())  # 　不正解の県庁所在地を作成（この中には、正解も含む）
        del wrong_answers[wrong_answers.index(
            correct_answer)]  # 不正解県庁所在地リストから正解のみ削除
        wrong_answers = random.sample(
            wrong_answers, 3)         # 不正解県庁所在地リストから3つだけ取得
        answer_options = [correct_answer] + \
            wrong_answers   # 正解1つと不正解3つで四択を作成
        # 四択の順番をシャッフル。（シャッフルしないと、答えが常に最初）
        random.shuffle(answer_options)

        # 問題文と解答選択肢を問題ファイルに書き込む
        quiz_file.write(
            f'{question_num + 1}.{prefectures[question_num]}の都道府県庁所在地は？\n')
        for i in range(4):
            quiz_file.write(f'{"ABCD"[i]}. {answer_options[i]}\n')
        quiz_file.write('\n')

        # 答えの選択肢を解答ファイルに書き込む
        answer_key_file.write(
            f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}")
        answer_key_file.write('\n')

    quiz_file.close()
    answer_key_file.close()
