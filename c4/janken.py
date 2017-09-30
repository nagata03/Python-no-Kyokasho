# じゃんけんゲーム
import random

# 手をリストで表現
hand = ["グー", "チョキ", "パー", "ゲーム終了"]

print("===== じゃんけんしましょう！ =====")
while True:
    # コンピュータの手を決定
    com = random.randint(0,2)

    # ユーザの手を入力してもらう
    for i, desc in enumerate(hand): # enumerate関数でリストのインデックス番号と要素の値を取得
        print(i, ":", desc)
    
    you = int(input("出す手を数値で入力してください："))
    if you == 3: break
    if you < 0 or 3 < you:
        print("0から3の間で入力してね！")
        continue

    # 手を表示
    print("-----")
    print("あなた　　　：", hand[you])
    print("コンピュータ：", hand[com])
    print("-----")
    
    # じゃんけんの勝敗を判定する
    j = (you - com + 3) % 3
    if j == 0:
        print("あいこ")
    elif j == 1:
        print("コンピュータの勝ち！")
    elif j == 2:
        print("あなたの勝ち！")
    print("==========")

    
        