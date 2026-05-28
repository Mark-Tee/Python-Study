str = "许多"
print("许"in str)
#判断字符串中是否包含某个子串
print("许"not in str)
#判断字符串中是否不包含某个子串
print("许" in str and "多" in str)
#判断字符串中是否同时包含多个子串
print("许" in str or "多" not in str)
#判断字符串中是否至少包含一个子串
print("许" in str and "多" not in str)
#判断字符串中是否包含一个子串但不包含另一个子串
print("许" in str or "多" in str)
#判断字符串中是否包含一个子串或另一个子串
str2 = "dommyhsu"
i = 0
while i < len(str2):
    print(str2[i], end="")
    i += 1
li = [1, 2, 3, 4, 5]
li.extend([6])
li.append(7)
print(li)
#将12345拆解成一个列表
li2 = list("12345")
print(li2)
#将字符串拆解成一个列表
#将列表内的元素变成int类型
li2 = [int(i) for i in li2]
print(li2)

