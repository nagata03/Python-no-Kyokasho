##### 英単語の出現回数を数えるプログラム #####
# 単語の出現回数をカウント
text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 単語を区切る
text = text.replace(";", "")    # 「;」を削除
text = text.replace(",", "")    # 「,」を削除
text = text.replace(".", "")    # 「.」を削除
words = text.split()    # 空白で区切ってリスト型を作成

# 単語を数える
counter = {}    # counterというからの辞書型を作成
for w in words:
    ws = w.lower()  # 小文字に変換
    if ws in counter:   # もし辞書型にすでにキー（単語）があれば値を1加算
        counter[ws] += 1
    else:   # もし辞書型にキー（単語）がなければ値を1とする
        counter[ws] = 1

# 結果を表示
for k, v in sorted(counter.items()):
    if v >=3:
        print(k, v)

