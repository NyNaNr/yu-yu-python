# サンドイッチメーカー 様々な選択肢のインプットを保証しつつ、適当な値段をつけ、合計金額を表示
import pyinputplus as pyip

"""
    設計
    メニューの辞書をそれぞれの選択項目ごとに作成。
    その辞書のキーのみ取り出しpyipに必要なリストに変換
    ユーザーの選択したキーを元にバリューを取り出し、足していく。
    """
# TODO: このままじゃ、トッピングのオプションが複数選べない。一つ一つ選べるようにする。


class SandwichShop:
    # menu
    def __init__(self):
        self.type_of_bread = {'小麦パン': 100, '白パン': 200, 'サワー種': 300}
        self.type_of_protain = {'チキン': 100, 'ターキー': 150, 'ハム': 120, '豆腐': 50}
        self.type_of_cheese = {'チェダー': 100, 'スイス': 200, 'モッツアレラ': 300}
        self.type_of_topping = {'マヨネーズ': 20, 'からし': 50, 'レタス': 80, 'トマト': 100}
        self.main_list = [self.type_of_bread, self.type_of_protain]
        self.optional_list = [self.type_of_cheese, self.type_of_topping]

    def main_list_input(self):
        # 辞書からキーだけを取り出してpyipに適したリストを作成。
        main_sum = 0  # main_sum = 0 はfor文の外に書かないと回るたびにmain_sumに0が代入される。
        for each_type in self.main_list:
            list_name = []

            for key in each_type.keys():
                list_name.append(key)
            # for文で作成したリストと、辞書名を回しつつ、ユーザーに入力を求める。
            value = each_type.get(pyip.inputMenu(list_name))
            print(f'{value}円です')
            main_sum += value

        return main_sum

    def optional_list_input(self):
        # 辞書からキーだけを取り出してpyipに適したリストを作成。
        optional_sum = 0  # optional_sum = 0 はfor文の外に書かないと回るたびにoptinal_sumに0が代入される。
        for each_type in self.optional_list:
            list_name = []
            for key in each_type.keys():
                list_name.append(key)
            # ユーザーにオプションを提示し、必要か問う
            if (pyip.inputYesNo(f'{str(each_type)}は必要ですか？yesかnoでお答えください。')) == 'yes':
                # for文で作成したリストと、辞書名を回しつつ、ユーザーに入力を求める。
                value = each_type.get(pyip.inputMenu(list_name))
                print(f'{value}円です')
                optional_sum += value
        return optional_sum

    def sum_two(self, main_sum, optional_sum):
        JAPAN_TAX_RATE = 1.08

        total_price = (main_sum + optional_sum)*JAPAN_TAX_RATE
        total_price = round(total_price)
        print(f'小計は税込み{total_price}円です。')
        return total_price

    def how_many(self, total_price):

        count = pyip.inputInt('何個入りますか？', min=1)
        total_price = round(total_price * count)

        print(f'支払い金額は税込み{total_price}円です。')

    def execute(self):
        main_sum = self.main_list_input()
        optional_sum = self.optional_list_input()
        total_price = self.sum_two(main_sum, optional_sum)
        self.how_many(total_price)


sandwichshop = SandwichShop()
sandwichshop.execute()
