# サンドイッチメーカー 様々な選択肢のインプットを保証しつつ、適当な値段をつけ、合計金額を表示

"""
    設計
    # 前回
    メニューの辞書をそれぞれの選択項目ごとに作成。
    その辞書のキーのみ取り出しpyipに必要なリストに変換
    ユーザーの選択したキーを元にバリューを取り出し、足していく。

    # 今回
    全メニューをまとめて一つの辞書で管理
    pyipでリストを手書きで入力し、ユーザーに選んでもらう
    選んでもらったものを変数に保存（後で、それをキーとして、バリュー取得
    パン、プロテインの小計をだす
    オプションは、そのオプションごとに必要か聞く。オプションは、pyipのyesnoで入力させ、 =='yes'でTrueを変数に保存
    必要な個数を聞く。

    すべての個別の料金を出す。（オプションについては、Trueのもののみ計算＆表示）
    
    合計を聞く
    """

import pyinputplus as pyip

PRICES = {
    '小麦パン': 100,
    '白パン': 110,
    'サワー種': 120,
    'チキン': 200,
    'ターキー': 250,
    'ハム': 300,
    '豆腐': 280,
    'チェダー': 100,
    'スイス': 150,
    'モッツアレラ': 180,
    'マヨネーズ': 10,
    'マスタード': 10,
    'レタス': 50,
    'トマト': 30,
}


def sandwich_maker():
    bread = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'],
                           prompt='パンを選んでください。', numbered=True)
    meat = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'],
                          prompt='お肉を選んでください。', numbered=True)

    is_cheese = pyip.inputYesNo('cheeseは必要ですか？ YesかNoでお答えください。')
    if is_cheese == 'yes':
        cheese = pyip.inputMenu(
            ['チェダー', 'スイス', 'モッツアレラ'], prompt='cheeseの種類を選んでください。', numbered=True)

    # is_~には、真偽値が入る
    is_mayo = pyip.inputYesNo('マヨネーズは必要ですか？Yes or No:') == 'yes'
    is_mastard = pyip.inputYesNo('マスタードは必要ですか？Yes or No:') == 'yes'
    is_lettuce = pyip.inputYesNo('レタスは必要ですか？Yes or No:') == 'yes'
    is_tomato = pyip.inputYesNo('トマトは必要ですか？Yes or No:') == 'yes'

    # 値段の表示
    sum_price = 0
    bread_price = PRICES.get(bread, 0)
    sum_price += bread_price
    print(f'パンの値段は{bread_price}円です。')

    meat_price = PRICES.get(meat, 0)
    sum_price += meat_price
    print(f'お肉の値段は{meat_price}円です。')

    cheese_price = 0
    if is_cheese == 'yes':
        cheese_price = PRICES.get(cheese, 0)
        sum_price += cheese_price
        print(f'チーズの値段は{cheese_price}円です。')

    if is_mayo:
        mayo_price = PRICES.get('マヨネーズ', 0)
        sum_price += mayo_price
        print(f'マヨネーズの値段は{mayo_price}円です。')

    if is_mastard:
        mastard_price = PRICES.get('マスタード', 0)
        sum_price += mastard_price
        print(f'マスタードの値段は{mastard_price}円です。')

    if is_lettuce:
        lettuce_price = PRICES.get('レタス', 0)
        sum_price += lettuce_price
        print(f'レタスの値段は{lettuce_price}円です。')

    if is_tomato:
        tomato_price = PRICES.get('トマト', 0)
        sum_price += tomato_price
        print(f'トマトの値段は{tomato_price}円です。')

    JAPAN_TAX_RATE = 1.08
    sum_price = round(sum_price * JAPAN_TAX_RATE)
    print(f'小計は税込み{sum_price}円です')

    count = 0
    count = pyip.inputInt(prompt='何個購入されますか？', min=1)
    print(f'合計は{sum_price*count}円です。')


sandwich_maker()
