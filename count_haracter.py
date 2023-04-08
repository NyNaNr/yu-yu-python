import pprint


def count_chatacter(message):
    print('================================')
    count = {}

    for character in message:
        count.setdefault(character, 0)  # 初期値を0で代入してるから、一行下で+1ができる。
        count[character] += 1

    pprint.pprint(count)
    print(len(count))
    print('================================')


count_chatacter('The sun slowly sets behind the distant mountains, casting a warm orange glow across the tranquil sea. The waves gently lap at the shore, creating a soothing melody that fills the air. A lone seagull flies overhead, its wings gracefully slicing through the sky. The salty air fills your lungs as you take a deep breath, feeling a sense of peace and calm wash over you. The sound of children playing in the sand and the distant chatter of families enjoying their vacation drifts towards you, a reminder that life is full of joy and beauty. As the stars begin to twinkle in the clear night sky, you close your eyes and let the rhythm of the ocean lull you into a deep and restful sleep.')
count_chatacter('遠くの山の陰で夕日がゆっくりと沈み、穏やかな海に暖かいオレンジ色の輝きを投げかけます。波が優しく浜辺に打ち寄せ、心地よいメロディを奏でています。孤独なカモメが上空を飛び、優雅に羽を広げて空気を切り裂いています。塩気のある空気が肺に入り、深呼吸をすると、平和と静けさがあなたを包みます。砂浜で遊ぶ子供たちの声や、バカンスを楽しむ家族たちの遠くのおしゃべりが聞こえてきます。人生は喜びと美しさで溢れていることを思い出させてくれます。星が輝き始め、澄み切った夜空に浮かぶその音に耳を傾け、目を閉じて海のリズムに身を任せ、深く安らかな眠りにつくのでした。')
