##### 画面に赤と青の線を交互に100本引く #####

# グラフィックライブラリを取り込む
from tkinter import *

# 画面の初期化
w = Canvas(Tk(), width=900, height=400)
# 描画画面を配置する
w.pack()

# 線をたくさん引く
for i in range(100):
    x = i * 9
    if i % 2 == 0:
        col = "#ff0000"
    else:
        col = "#0000FF"
    w.create_line(x, 0, x, 400, fill=col)

# 画面を表示して待機
mainloop()
