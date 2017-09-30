##### ジェネレータを使って奇数を返すイテレータを作る #####
# 30以下の奇数を返すイテレータ
def genOdd():
    i = 1
    while i <= 30:
        yield i
        i += 2

# イテレータを得る
it = genOdd()

for i in it: print(i, end=", ")