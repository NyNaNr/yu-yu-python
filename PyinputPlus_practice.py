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
        self.type_of_bread = {'小麦パン': 0, '白パン': 20, 'サワー種': 60}
        self.type_of_protain = {'チキン': 100, 'ターキー': 150, 'ハム': 120, '豆腐': 50}
        self.type_of_cheese = {'チェダー': 100, 'スイス': 200, 'モッツアレラ': 300}
        self.type_of_topping = {'マヨネーズ': 20, 'からし': 50, 'レタス': 80, 'トマト': 100}
        # self.type_of_bread_list =[]
        # self.type_of_protain_list = []
        # self.type_of_cheese_list =[]
        # self.type_of_topping_list =[]
        self.ask_list = [self.type_of_bread, self.type_of_protain,
                         self.type_of_cheese, self.type_of_topping]

    def user_input(self, list_name):
        decided_bread = pyip.inputMenu(list_name)

    def make_key_list(self):
        for each_type in self.ask_list:
            list_name = str(each_type) + '_list'
            list_name = []
            for key in each_type.keys():
                list_name.append(key)
            return list_name


sandwichshop = SandwichShop()
sandwichshop.make_key_list()
