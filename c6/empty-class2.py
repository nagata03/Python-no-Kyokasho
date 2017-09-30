# 空のクラスを定義
class Empty: pass

# 空のクラスのインスタンスを作成
o = Empty()
# 動的にメソッドを追加
o.x2 = lambda x: x * 2
o.x3 = lambda x: x * 3

# 追加したメソッドを使ってみる
print(o.x2(8))
print(o.x3(4))
