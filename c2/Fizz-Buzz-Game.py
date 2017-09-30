##### FizzBuzzゲームのプログラム #####
for i in range(1,51):
    if (i % 3 == 0) and (i % 5 == 0):
        print("i=",i,"：FizzBuzz")
        continue
    if i % 3 == 0:
        print("i=",i,"：Fizz")
        continue
    if i % 5 == 0:
        print("i=",i,"：Buzz")
        continue
    print("i=",i)
