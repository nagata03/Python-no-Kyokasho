##### 繰り返し坪を平方メートルに変換するプログラム #####

while True:
    tsubo_input = input("坪数は？＞＞")
    if (tsubo_input == "") or (tsubo_input == "q"):
        print("プログラムを終了します。")
        break
    tsubo = float(tsubo_input)
    m2 = tsubo * 3.31
    desc = "{0}坪は{1}平方メートルです。".format(tsubo, m2)
    print(desc)
