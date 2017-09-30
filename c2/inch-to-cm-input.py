# 1インチは2.54センチ
per_inch = 2.54

# 案内文
print("「インチ」を「センチ」に変換します。")

# インチを入力
inch = input("インチを入力してください。＞＞")

# インチをセンチに変換
cm = float(inch) * per_inch

# 結果を出力
desc = "{0}インチ = {1}センチ".format(inch, cm)
print(desc)
# print(inch+"インチは"+str(cm)+"センチです。")
