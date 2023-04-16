'''
1人1人にランダムな問題と解答を！！

1.35通りの問題集を作成する。
2.問題集は都道府県を網羅する47問の4択とし、問題の順番はランダムとする。
3.各問題の選択肢は、正解1つと、ランダムな誤答が3つあり、順番はランダムとする。
4.問題集は、35個のテキストファイルに書き出す。
5.怪盗集も35個のテキストファイルに書き出す。

以上のことからコードは次のように動作する必要があります。
1.県と県庁所在地を辞書に記述する。
2.open(),write(),close()を呼び出し問題集と解答集を作成する。
3.random.shuffle()を用いて、問題や選択肢をランダムに並び替える。
'''