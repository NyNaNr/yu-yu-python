import sys


def collatz():
    print()
    try:
        number = int(input('数字を入力してください：'))
        print(number)
    except ValueError:
        print("エラー：数字以外の文字を入力しないでください。")
        sys.exit()

    while (number > 1):
        if number % 2 == 0:
            number = int(number/2)

        else:
            number = int(number * 3 + 1)

        print(' →', number, end='')


collatz()
