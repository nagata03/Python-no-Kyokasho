##### タプルのリストをソートする #####
# 辞書型で 動物:最高時速 を定義
animal_dict = {
    "ライオン":58,
    "チーター":110,
    "シマウマ":60,
    "トナカイ":80
}

# 足の速い順に並び替える
li = sorted(animal_dict.items(), key = lambda x : x[1], reverse = True)

# 結果を表示
for name, speed in li: print(name, speed)