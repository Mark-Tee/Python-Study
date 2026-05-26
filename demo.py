i = 1
j = 1
while i<=3:
    print(f"内循环{i}次")
    i +=1
    while j<=5: 
        print(f"这是第{j}次内循环")
        j +=1
    j = 1  # 重置内循环计数器
