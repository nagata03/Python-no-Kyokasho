##### 引数の名前を指定して関数を呼び出すプログラム #####
# 距離と速さから時間を求める関数
def calc_time(dist, speed):
    time = dist / speed
    time = round(time, 1)
    return time

# 関数を実行
print(calc_time(500, 100))
print(calc_time(dist=500, speed=100))
print(calc_time(speed=100, dist=500))
