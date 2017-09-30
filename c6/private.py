# 非公開属性にアクセスできないことを確かめるプログラム
# そのため、エラーが出ます
# ---クラス定義
class Game:
    def __goal(self):
        print("非公開のメソッド")

    def play(self):
        print("公開のメソッド")

# ---クラスの利用
game = Game()
game.play()
#game._Game__goal()
game.__goal()   # ここでエラーになる
