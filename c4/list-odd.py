# 10以下の奇数を持つリストを作る

# 方法１
data = [i*2-1 for i in range(1,6)]
print(data)

# 方法２（rangeを工夫）
data = [i for i in range(1, 11, 2)]
print(data)

# 方法３（内包表記でforとifを組み合わせる）
data = [i for i in range(1, 11) if i % 2 == 1]
print(data)
