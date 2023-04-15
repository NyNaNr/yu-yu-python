# 日付の検出正規表現

import re

w = '今日の日付は26/04/2023です'

date_regex = re.compile(r'''(
    (0?[1-9]|[12][0-9]|3[01]) #dd
    /
    (0?[1-9]|1[0-2]) # mm
    /
    ([12]d{3}) # yyyy


)''', re.VERBOSE)

mo = date_regex.search(w)
if mo:
    print(mo.group())
else:
    print('マッチする日付は見つかりませんでした。')


'''
正規表現を数字且つスラッシュでdate形式を検知するのみとするよって、
1,任意の二桁の数字を入力させる。00/00/0000~99/99/9999
が正規表現にマッチする。
以下、条件式を用い、日付としての絞り込みをし、該当しない場合えらーを返す。
yyyyは1000以上2999以下
mm は01以上12以下 
mmとyyyyによってdayのmaxを条件分岐
1うるう年の場合の2月=>29 うるう年以外の2月=>28
(うるう年は(yyyy%4=0 and yyyy%100 !=0)or yyyy%4000 ==0)
2 (4,6,9,11)月の場合=>30
もしいずれかにマッチしなった（存在しない日付）の場合、「不正な月です」と返す。
「もし存在したらdd/mm/yyyyは正しい日付です」と返す。
'''


def detect_date_DIY(a):
    date_regex_diy = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    for day, month, year in date_regex_diy.findall(a):
        day = int(day)
        month = int(month)
        year = int(year)

    if 1000 > year or 2999 < year:
        print(f'{year}は不正な年です。')

    if 0 > month or month > 13:
        print(f'{month}は不正な月です。')

    # うるう年の篩
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28

    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        max_day = 31

    # month dayの判定
    if 0 > day or day > max_day:
        print(f'{month}月{day}日は不正な日付です。')
    else:
        print(f'{year}年{month}月{day}日は正しい日付です。')


detect_date_DIY('29/02/2013')
detect_date_DIY('29/02/2012')

"""
    反省 正規表現の\d{2}のdの前に\を入れ忘れてた。
    プログラムを書き出す前に、必ず全体の設計をする。
    """


# 強いパスワードの検出
'''
強いパスワードとは、8文字以上、大文字小文字を含み、1つ以上の数字を含むものらしい。
正規表現で、強いパスワードを検出するプログラムを作る。

設計
正規表現をつくる。len() >= 8 ,[a-z], [A-Z], \d{} <= バラバラで一つずつの正規表現を作って、すべてtrueならＯＫ？
当てはまる場合、print(強い！)
当てはまらないprint(yowai)

'''
print()


def detect_strong_password(sp):
    number_in_pass_regex = re.compile(r'\d')
    upper_in_pass_regex = re.compile(r'[A-Z]')
    lower_in_pass_regex = re.compile(r'[a-z]')

    if len(sp) < 8:
        print('8文字以上にしてください。')

    if number_in_pass_regex.search(sp) == None:
        print('数字を1文字以上含んでください。')
    if upper_in_pass_regex.search(sp) == None:
        print('大文字を1文字以上含んでください。')
    if lower_in_pass_regex.search(sp) == None:
        print('小文字を1文字以上含んでください。')

    if (number_in_pass_regex.search(sp)) and (upper_in_pass_regex.search(sp)) and (lower_in_pass_regex.search(sp)) and (len(sp) > 7):
        print('強いパスワードです。')
    else:
        print('弱いパスワードです。')


detect_strong_password('552HGhg55')

'''
反省。自分でできた！
number_in_pass_regex = re.compile(r'\d') を間違えてnumber_in_pass_regex = re.compile(r'\d{}')としていた。 これではエラーが出る。\d{3}数字が三回出現するように、{}には数字を入れる。
'''
