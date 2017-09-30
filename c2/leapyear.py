##### うるう年を判定するプログラム #####

### 年（西暦）を入力
year = int(input("年（西暦）を入力してください。＞＞"))

### うるう年かどうかを判定
#if (year % 4 == 0):
#    if (year % 100 == 0):
#        if (year % 400 == 0):
#            cmt = "うるう年です。"
#        else:
#            cmt = "うるう年ではありません。"
#    else:
#        cmt = "うるう年です。"
#else:
#    cmt = "うるう年ではありません。"

#is_leap = False
#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            is_leap = True
#    else:
#        is_leap = True

#if year % 400 == 0:
#    is_leap = True
#elif year % 4 == 0:
#    is_leap = True

is_leap = (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

### 結果を出力
#fmt = """
#西暦{0}年は{1}
#"""
#desc = fmt.format(year, cmt)
#print(desc)

if is_leap:
    print("うるう年です。")
else:
    print("うるう年ではありません。")

