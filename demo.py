NameLi = []
#封装get_name函数
def get_name():
    name = input("请输入姓名,输入q退出：\n")
    #判断输入的姓名是否为q或Q，如果是则退出程序并输出姓名列表；如果不是，则判断输入的姓名是否已经存在于姓名列表中，如果存在则提示用户重新输入；如果不存在则将输入的姓名添加到姓名列表中，并继续调用get_name函数进行下一次输入。
    if name =="q" or name == "Q":
        if len(NameLi) == 0:
            print("没有输入任何姓名！")
        else:
            print("输入的姓名列表为：", NameLi)
        return None
    elif name in NameLi or name.capitalize() in NameLi or name.lower() in NameLi or name.upper() in NameLi:
        print(f"输入的姓名 '{name}' 已被注册，请重新输入！")
        return get_name()
    else:
        NameLi.append(name)
        return get_name()
#调用get_name函数
get_name()