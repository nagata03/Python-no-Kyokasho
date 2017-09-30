##### 辞書とfor文の練習 #####
fruits = {
    "バナナ":300,
    "りんご":100,
    "みかん":120,
    "マンゴー":400
}

# 辞書型のデータ一覧を表示
for name in fruits.keys():
    # 値段を得る
    price = fruits[name]
    # 画面に出力
    s = "{0}は{1}円です。".format(name, price)
    print(s)

for name, price in fruits.items():
    s = "{0}は{1}円です。".format(name, price)
    print(s)
