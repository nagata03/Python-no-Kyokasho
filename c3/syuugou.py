##### 集合の使い方 #####
colors = {"red", "green", "blue"}
print(colors)

e = set()
fruits = set({"Apple", "Banana", "Lemon"})
print(fruits)


box1 = {"ハンマー", "釘", "ペンチ"}
box2 = {"釘", "ペンチ"}
print(box1 - box2)
print("ペンチ" in box2)
print("ハンマー" in box2)
print(box1 & box2)


