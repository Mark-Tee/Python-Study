i = 1
j = 1
while i <= 9:
    while j <= i:
        print(f"{i}*{j}={i*j}\t", end="")
        j += 1
    print()  # 换行
    i += 1
    j = 1  # 重置内循环计数器