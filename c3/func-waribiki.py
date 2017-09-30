##### 割引額を求めるプログラム #####
# 関数を定義
def cal_waribiki(time, number, price):
    if (time == 14) & (number >= 3):
        price *= 0.9
        info = "1割引"
    elif (time == 15) & (number >= 5):
        price *= 0.8
        info = "2割引"
    else:
        info = "無割引"
    
    print("{0}で{1}円です。".format(info, int(price)))


# ユーザに情報を入力してもらう
i = input("何時に買い物しましたか？＞＞")
time = int(i)

i = input("商品をいくつ買いましたか？＞＞")
number = int(i)

i = input("何円分の買い物をしましたか？＞＞")
price = int(i)

# 関数を呼び出す
cal_waribiki(time, number, price)