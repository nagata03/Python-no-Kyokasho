##### 生徒の点数リストから赤点を抽出する #####
points = [80, 40, 23, 14, 29, 58]

akaten = []
for i in points:
    if i < 30:
        akaten.append(i)

print(akaten)
