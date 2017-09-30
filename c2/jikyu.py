# 給料計算プログラム

# 時給の入力
jikyu_input = input("時給を入力してください。＞＞")
jikyu = float(jikyu_input)

# 労働時間の入力
jikan_input = input("労働時間（単位は時間）を入力してください。＞＞")
jikan = float(jikan_input)

# 給料の計算
kyuryo = jikyu * jikan

# 結果の出力
# desc = "給料は{0}円です。".format(kyuryo)
fmt = """
時給{0}円で
{1}時間働いたので、
給料は{2}円です。
"""
desc = fmt.format(jikyu, jikan, kyuryo)
print(desc)
