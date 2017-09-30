# 生徒クラスの定義
class Student:
    def __init__(self, id, name, score=0):
        '''コンストラクタ'''
        self.id = id
        self.name = name
        self.score = score

    def getID(self):
        '''IDを取得するメソッド'''
        return self.id

    def getName(self):
        '''名前を取得するメソッド'''
        return self.name

    def setScore(self, score):
        '''得点を設定するメソッド'''
        self.score = score

    def getScore(self):
        '''得点を取得するメソッド'''
        return self.score

# 点数を計算するクラス
class CalcScore:
    def __init__(self):
        '''コンストラクタ'''
        self.students = []

    def addStudent(self, student):
        '''学生を追加するメソッド'''
        self.students.append(student)

    def ave(self):
        '''設定した生徒全員の平均を求めるメソッド'''
        v = 0
        for i in self.students:
            v += i.getScore()

        ave_v = v / len(self.students)
        return ave_v

# 学生を表すインスタンスを生成
p1 = Student(id=10, name="佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score=79)
p3 = Student(12, "佐々木", score=84)
p4 = Student(13, "井上", score=77)

# 平均点を計算
calc = CalcScore()
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print("平均点＝", calc.ave())
