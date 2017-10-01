# 旧暦の月名を返すクラスを定義
class Tsukimei:
    tsuki = ["睦月", "如月", "弥生", "卯月", "皐月", "水無月",
        "文月", "葉月", "長月", "神無月", "霜月", "師走"]

    def __getitem__(self, key):
        if 1 <= key <= 12:
            i = int(key)
            return self.tsuki[i-1]  # インデックス番号(i-1)と月を一致させる
        else:
            return "Error：1〜12を指定してください。"

    def __setitem__(self, key, value):
        i = int(key)
        self.tsuki[i-1] = value

# 添え字アクセスしてみる
t = Tsukimei()
print(t[1])
print(t[3])
print(t[4])
print(t[13])

t[10] = "神在月"
print(t[10])
print(t[12])
