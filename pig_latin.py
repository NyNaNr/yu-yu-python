# 英語からピッグラテンに変換
# TODO: テキストファイルで読み書き出来たら便利

while True:
    print('Enter the Engkish message to translate into Pig Latin:')
    message = input()
    if message == '':
        print('１文字以上入力してください。')
    else:
        break


VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = []  # ピッグラテンの単語リスト

words = message.split()
word_count = len(words)


for i, word in enumerate(message.split(), 1):
    print(f'{round(i/word_count*100,2)} % 完了')

    # wordの先頭の英字でないものを分離
    prefix_non_letter = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letter += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letter)
        continue

    # word の末尾が英字でないものを分離する
    suffix_non_letter = ''
    while not word[-1].isalpha():
        suffix_non_letter += word[-1]
        word = word[:-1]

    # word がすべて大文字か、先頭のみ大文字か覚えておく
    was_upper = word.isupper()
    was_title = word.istitle()
    word = word.lower()

    # wordの先頭の子音を分離する
    prefix_consonants = ''
    while len(word) > 0 and word[0] not in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # wordにピッグラテンの語尾をつける
        # wordの先頭が子音で始まる場合
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'

        # wordの先頭が母音で始まる場合
    else:
        word += 'yay'

    # 必要な場合wordをすべて大文字か先頭のみ大文字に戻す
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # wordの先頭と末尾にあった英字でない文字を元に戻す
    pig_latin.append(prefix_non_letter + word + suffix_non_letter)


# 単語リストを1つの文字列に連結して表示する
print(' '.join(pig_latin))
