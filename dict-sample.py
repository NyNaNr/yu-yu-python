# birthdayDict を作成

name_birth_day = {}
print('友人の誕生日を表示します。')

while True:
    print('友人の名前を入力してください \n終了するにはEnterキーだけ押してください')

    name = input()

    if name == '':
        break
    if name in name_birth_day:
        print(f'{name}さんの誕生日は{name_birth_day[name]}です。')
    else:
        while True:
            input_date = input(f'{name}さんは未登録です。{name}さんの誕生日を教えてください。')
            if input_date:
                break
            print('入力が空です。もう一度入力してください。')
        name_birth_day[name] = input_date
        print(f'{name}さんの誕生日は{name_birth_day[name]}です。')

print('誕生日リストです。')
for name, date in name_birth_day.items():
    print(f'{name}さん {date}')
