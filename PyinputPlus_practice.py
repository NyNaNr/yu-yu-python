# サンドイッチメーカー 様々な選択肢のインプットを保証しつつ、適当な値段をつけ、合計金額を表示
import pyinputplus as pyip

"""
    設計
    メニューの辞書をそれぞれ作成
    入力＝＞辞書から値段を取得　入力関数と、値取得関数を分ける。
    計算
    """


class SandwichShop:
    # menu
    def __init__(self):
        self.type_of_bread = {'小麦パン': 100, '白パン': 200, 'サワー種': 300}
        self.type_of_protain = {'チキン': 100, 'ターキー': 150, 'ハム': 120, '豆腐': 50}
        self.type_of_cheese = {'チェダー': 100, 'スイス': 200, 'モッツアレラ': 300}
        self.type_of_topping = {'マヨネーズ': 20, 'からし': 50, 'レタス': 80, 'トマト': 100}
        self.ask_list = [self.type_of_bread, self.type_of_protain,
                         self.type_of_cheese, self.type_of_topping]

    def make_key_list_and_input(self):
        # 辞書からキーだけを取り出してpyipに適したリストを作成。
        sum = 0  # sum = 0 はfor文の外に書かないと回るたびにsumに0が代入される。
        for each_type in self.ask_list:
            list_name = []

            for key in each_type.keys():
                list_name.append(key)
            # for文で作成したリストと、辞書名を回しつつ、ユーザーに入力を求める。
            value = each_type.get(pyip.inputMenu(list_name))
            print(f'{value}円です')
            sum += value

        print(f'支払い金額は{sum}円です。')


sandwichshop = SandwichShop()
sandwichshop.make_key_list_and_input()
