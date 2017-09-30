##### 素数を返すイテレータ #####
# イテレータを定義
def genPrime(maxnum):
    num = 2
    while (num <= maxnum):
        is_Prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_Prime = False
                break
        if is_Prime: yield num
        num += 1

# イテレータオブジェクトを得る
it = genPrime(50)

# for文で繰り返し表示
for i in it: print(i, end=",")