class Hoge:
    # 静的メソッドを定義
    @staticmethod
    def introduce():    # 引数にselfを指定する必要はない
        print("Hoge")

# インスタンスを作成せずにメソッドを利用する
Hoge.introduce()
