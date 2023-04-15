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


def detect_date(s):
    date_regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    for day, month, year in date_regex.findall(s):
        day = int(day)
        month = int(month)
        year = int(year)

        if year < 1000 or year > 2999:
            print(f'不正な年です {year}')
            return None

        if month < 1 or month > 12:
            print(f'不正な月です {month}')
            return None

        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                max_day = 29
            else:
                max_day = 28
        elif month in (4, 6, 9, 11):
            max_day = 30
        else:
            max_day = 31
        if day < 1 or day > max_day:
            print(f'不正な日です {day}')
            return None
        return day, month, year
    return None


if __name__ == '__main__':
    assert detect_date('Today is 15/08/1945.') == (15, 8, 1945)
    assert detect_date('There is no 31/02/2020.') == None
    assert detect_date('There is no 31/04/2021.') == None
    assert detect_date('There is no 15/00/1945.') == None
    assert detect_date('There is no 15/13/1945.') == None
    assert detect_date('There is no 00/08/1945.') == None
    assert detect_date('There is no 32/18/1945.') == None
    assert detect_date('There is no 01/08/9999.') == None
    assert detect_date('Bad format: 1945/08/15.') == None
