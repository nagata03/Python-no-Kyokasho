# Scikit Learnのデータセットを取り込む
from sklearn import datasets, cross_validation, svm, metrics

# 手描き数字データを読み込む
digits = datasets.load_digits()

# 訓練用データとテスト用データに分ける
# 手描き画像データ(digits.data)とラベルデータ(digits.target)を入力し、
# 訓練用の画像データ(data_train)、テスト用の画像データ(data_test)、訓練用のラベル(label_train)、テスト用のラベル(label_test)の
# ４つを出力する。
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(digits.data, digits.target)

# SVMアルゴリズムを利用してモデルを構築する
clf = svm.SVC(gamma=0.001)

# fitメソッドで学習する
# 第１引数は訓練用の画像データ、第２引数は訓練用のラベルを指定
clf.fit(data_train, label_train)

# テストデータでの分類結果を予測してみる
# predictメソッドは学習済みのモデルを元に、テスト用画像データの分類を予測する
predict = clf.predict(data_test)

# 結果を表示する
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("分類器の情報＝", clf)
print("正解率＝", ac_score)
print("レポート＝\n", cl_report)
