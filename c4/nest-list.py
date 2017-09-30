# 1から3のすべての組み合わせをつくる
base = [1, 2, 3]
result = [(x, y) for x in base for y in base]
print(result)

# xとyが同じ値の組み合わせは除外する
base = [1, 2, 3]
result = [(x, y) for x in base for y in base if x != y]
print(result)
