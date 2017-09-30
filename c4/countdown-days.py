import datetime

# 東京オリンピックの日付
t1 = datetime.date(2020, 7, 24)

# 今日との日数差を計算
t2 = datetime.date.today() # 本日の日付を取得
diff = t1 - t2

# 結果を表示
print("今日：", t2.strftime("%Y/%m/%d"))
print("東京オリンピックまであと", diff.days, "日")
