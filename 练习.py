#1、输出：你好，Python！我正在学习编程，并让两句不换行。
# print("你好，Python!", end="")
# print("我正在学习编程")

#2、用input输入姓名、年龄、身高，然后用f-string格式化输出：我叫XX，今年XX岁，身高XX米。
# name = input("输入姓名")
# age = input("输入年龄")
# high = input("输入身高")
# print(f"我叫{name}，今年{age}岁，身高{high}米")

#3、输入两个数字，输出：和、差、积、普通除法、整除、余数、平方
# a = int(input("请输入第一个值"))
# b = int(input("请输入第二个值"))
# print(f"两数字的\n和是{a+b}\n差是{a-b}\n积是{a*b}\n普通除法{a/b}\n整除{a//b}\n取余{a%b}\n平方{a**b}")

#4、输入商品原价，输入折扣（如 85 表示 85 折），计算折后价，保留2 位小数并输出XX元
# price = int(input("请输入商品原价"))
# discount = int(input("请输入折扣"))*0.01
# print(f"折扣价{price*discount:.2f}")

#5、输入年龄：<18 → 未成年人 18~60 → 成年人 60 → 老年人
# age = int(input("请输入年龄"))
# if age <18 :
#     print("未成年人")
# elif age <=60 and age >=18:
#     print("成年人")
# else :
#     print("老年人")

#6、输入分数（0-100）：90+ → A 80-89 → B 60-79 → C <60 → D
# grade = int(input("输入分数"))
# if grade >=90:
#     print("A")
# elif grade >=80 and grade <89:
#     print("B")
# elif grade >=60 and grade <79:
#     print("C")
# else :
#     print("D")

#7、用while计算 1+2+…+10，输出总和
# i = 1
# j = 1
# while i < 10 :
#     i += 1
#     j += i
# else :
#     print(j)

#8、用for + range打印 1~20 之间所有奇数，遇到 13 用continue跳过，遇到 19 用break停止
# even_num = []
# for i in range(1,20) :
#     if i % 2 != 0 :
#         if i==13 :
#             continue
#         if i == 19:
#             break
#     even_num.append(i)
# print(even_num)

'''9、输入一段英文
    转大写、转小写、首字母大写
    去掉两端空格
    按空格切分成列表
    统计a出现次数'''
# char = input("请输入一段英文")
# print(f"转大写{char.upper()}")
# print(f"转小写{char.lower()}")
# print(f"首字母大写写{char.capitalize()}")
# print(f"去掉两端空格{char.strip()}")
# print(f"按空格切分成列表{char.split()}")
# print(f"统计a出现次数{char.count('a')}")


'''10、创建列表：['张三','李四','王五']
在第 2 位插入赵六
删除李四
修改最后一个人为钱七
遍历输出所有名字
排序后输出
用列表推导式生成 [1,3,5,7,9]'''

# li = ['张三','李四','王五']
# li.insert(1,'赵六')
# li.remove('李四')
# li[-1] = '钱七'
# for i in li :
#     print(i)
# li.sort()
# print(li)

# even_number = [i for i in range(1,10) if i%2 != 0]
# print(even_number)


'''先创建一个学生名单：['张三', '李四', '王五']
显示菜单给用户选择：
查看所有学生
添加学生
删除学生
退出程序
用 while 循环 让程序一直运行，直到选 4 退出
用 if/elif 处理菜单选择
用 列表操作 完成增、查、删'''
stuLi = ['张三', '李四', '王五']
while True :
    sel = int(input("\n1、查看所有学生\t2、添加学生\n3、删除学生\t4、退出程序\n"))
    if sel == 1:
        for i in stuLi :
            print(i)
    elif sel == 2:
        adname = input("请输入需要添加的同学\n")
        stuLi.append(adname)
        print("成功添加\n")
        continue
    elif sel == 3:
        delname = input("请输入需要删除的同学姓名\n")
        if delname in stuLi :
            stuLi.remove(delname)
            print("成功删除\n")
            continue
        else :
            print("不存在该同学\n")
            continue
    elif sel == 4:
        print("退出\n")
        break
    else :
        print("请输入正确选项\n")
        continue
            

