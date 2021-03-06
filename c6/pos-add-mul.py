class Pos:
    """座標を表すクラス"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """「+」演算子の振る舞いを定義
            selfとotherの要素を足した
            新しいインスタンスを返す"""
        x2 = self.x + other.x
        y2 = self.y + other.y
        return Pos(x2, y2)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            """変数(other)がint型かfloat型の場合に流れるルート"""
            x2 = self.x * other
            y2 = self.y * other
            return Pos(x2, y2)
        else:
            raise TypeError

    def __str__(self):
        """文字列として取得する際の振る舞いを定義"""
        return "({0}, {1})".format(self.x, self.y)

# 座標p1とp2を作成
p1 = Pos(10, 20)
p2 = Pos(30, 40)

# 演算子「+」を使ってみる
p3 = p1 + p2
print(p3)

# 演算子「*」を使ってみる
p4 = p1 * 2
print(p4)
