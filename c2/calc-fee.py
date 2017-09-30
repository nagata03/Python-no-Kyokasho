# チケット売り場のレジシステム

# 金額設定
child_fee = 500
adult_fee = 1000
senior_fee = 700

# 人数を入力
child_num = int(input("子供（13才未満）は何人ですか？＞＞"))
adult_num = int(input("大人（13才以上65才未満）は何人ですか？＞＞"))
senior_num = int(input("高齢者（65才以上）は何人ですか？＞＞"))
sum_num = child_num + adult_num + senior_num

# チケット代金（割引なし）を計算
fee = child_fee * child_num + adult_fee * adult_num + senior_fee * senior_num

# 合計人数が10人以上の場合は団体割引（2割引）を適用
if sum_num >= 10:
    fee = fee * 0.8
    cmt = "対象"
else:
    cmt = "対象外"

# 結果を出力
fmt = """
子供人数は{0}人、
大人人数は{1}人、
高齢者人数は{2}人、
合計人数は{3}人で団体割引{4}となり、
チケット代金は合計{5}円です。"""
desc = fmt.format(child_num, adult_num, senior_num, sum_num, cmt, fee)
print(desc)