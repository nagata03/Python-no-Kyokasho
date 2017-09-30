##### 適当な個数の値の合計を求めるプログラム #####
# 引数の合計を求める関数
def sumArgs(*args):
    v = 0
    for i in args:
        v += i
    return v

# 関数を実行
print(sumArgs(500, 100))
print(sumArgs(1,2,3,4))
print(sumArgs(1,2,3,4,5,6,7,8,9,10))
