##### 関数の引数に関数を指定する例のプログラム #####
# 関数の定義
#def mul_func(a, b):
#    return a * b
 
#def add_func(a, b):
#    return a + b

def calc_5and3(func):
    return func(5, 3)

# 関数を実行
#print(calc_5and3(mul_func))
#print(calc_5and3(add_func))
# 無名関数を使用
print(calc_5and3(lambda a, b : a * b))
print(calc_5and3(lambda a, b : a + b))
