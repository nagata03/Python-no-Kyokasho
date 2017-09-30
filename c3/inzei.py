##### 印税を計算するプログラム #####
#
# （参考）印税 ＝ 定価 × 発行部数 × 印税率
#

# 関数の定義
def calc_inzei(price, sales, per):
    '''印税（定価×発行部数×印税率）を求める関数'''
    rate = per / 100
    return int(price * sales * rate)

# ユーザから情報を入力してもらう
i = input("定価（円）を入力してください。＞＞")
price = int(i)

i = input("発行部数（部）を入力してください。＞＞")
sales = int(i)

i = input("印税率（％）を入力してください。＞＞")
per = float(i)

# 関数を利用して印税を計算する
inzei = calc_inzei(price, sales, per)
print("印税は{0}円です。".format(inzei))

help(calc_inzei)