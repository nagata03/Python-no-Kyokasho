##### 動物ごとに東京から各都市までの所要時間を計算するプログラム #####
### 辞書型を定義
# 動物の速さ（km/h）
speed_dict = {
    "チーター":110, "トナカイ":80,
    "シマウマ":60, "ライオン":58,
    "キ リ ン":50, "ラ ク ダ":30
}

# 東京から各都市までの距離（km）
dist_dict = {
    "静　岡":183.7,
    "名古屋":350.6,
    "大　阪":507.5
}


### 関数を定義
# 距離と速さから時間を計算する関数
def calc_time(dist, speed):
    time = dist / speed
    time = round(time, 1)
    return time

# 動物ごとに各都市までの時間を計算する関数
def calc_animal(animal, speed):
    res = "|" + animal
    
    for dist in dist_dict.values():
        time = calc_time(dist, speed)
        res += "|{0:>6}".format(time)
    
    return res + "|"


### メイン処理
# 出力表のヘッダ
print("+--------+------+------+------+")
print("|動 物 名", end="")   # 「end=""」は改行しないという指定

for city in dist_dict.keys():
    print("|" + city, end="")

print("|")
print("+--------+------+------+------+")

# 動物ごとに結果を求めて表示
for animal, speed in speed_dict.items():
    time = calc_animal(animal, speed)
    print(time)
    
print("+--------+------+------+------+")