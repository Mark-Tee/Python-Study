i = 1
while i <= 10:
    print(f"小明吃了{i}个苹果")
    if i == 5:
        print("小明吃饱了，不吃了")
        i = 1
        break
    i += 1
while i <= 10:
    print(f"小明吃了{i}个苹果")
    if i == 5:
        print(f"第{i}个苹果，小明吃到虫子了")
        i += 1
        continue
    i += 1