# Scikit Learnのデータセットを取り込む
from sklearn import cross_validation, svm, metrics

# ワインデータを取り込む
wine_csv = []
with open("winequality-white.csv", "r", encoding="utf-8") as fp:
    no = 0
    for line in fp:
        line = line.strip() # １行ずつ読み込む
        cols = line.split(";")
        wine_csv.append(cols)   # colsをリスト(wine_csv)に追加する。

# １行目はヘッダなので削除
wine_csv = wine_csv[1:]

# csvの各データを数値に変換
labels = []
data = []
for cols in wine_csv:
    cols = list(map(lambda n: float(n), cols))  # map関数によりすべての値に対して関数(lambda)を適用する → 値を数値に変換
    # ワインのグレードを調整
    grade = int(cols[11])   # 末尾のデータがワインのグレード
    if 9 <= grade: grade = 8    # 少なすぎるサンプルを調整
    if grade <= 4: grade = 5
    labels.append(grade)    # ラベルデータ(ワインのグレード)
    data.append(cols[0:11]) # ワインの成分データ

# 訓練用データとテスト用データに分ける
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(data, labels)

# SVMのアルゴリズムを利用して学習
#clf = svm.SVC()
# ランダムフォレストのアルゴリズムを利用して学習
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()

clf.fit(data_train, label_train)

# 予測してみる
predict = clf.predict(data_test)
total = ok = 0
for idx, pre in enumerate(predict):
    pre = predict[idx]
    answer = label_test[idx]
    total += 1
    # ほぼ正解なら正解とみなす
    if (pre - 1) <= answer <= (pre + 1):
        ok += 1
print("正解率＝", ok, "/", total, "=", ok/total)

# 結果を表示する
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("正解率＝", ac_score)
print("レポート＝\n", cl_report)
