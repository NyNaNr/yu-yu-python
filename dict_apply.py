all_guest = {'Alice': {'りんご': 5, 'プレッツェル': 12},
             'Bob': {'ハムサンド': 3, 'りんご': 2},
             'Carol': {'コップ': 3, 'アップルパイ': 1}}


def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought


print('持ち物の数：')
print('りんご' + str(total_brought(all_guest, 'りんご')))
print('コップ' + str(total_brought(all_guest, 'コップ')))
print('ケーキ' + str(total_brought(all_guest, 'ケーキ')))
print('ハムサンド' + str(total_brought(all_guest, 'ハムサンド')))
print('アップルパイ' + str(total_brought(all_guest, 'アップルパイ')))
