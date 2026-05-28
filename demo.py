NameLi = []
addSel = "增加姓名"
delSel = "删除姓名"
chaSel = "修改姓名"
serSel = "查找姓名"

def SqlNameEasy ():
    Sel = input(f"1、{addSel}\t2、{delSel}\n3、{chaSel}\t4、{serSel}\n5、退出\n请输入选项：")
    if Sel == "1":
        Name = input("请输入姓名：")
        NameLi.append(Name)
        print(f"已添加姓名：{Name}")
        return SqlNameEasy()
    elif Sel == "2":
        Name = input("请输入要删除的姓名：")
        if Name in NameLi:
            NameLi.remove(Name)
            print(f"已删除姓名：{Name}")
        else:
            print("姓名不存在！")
        return SqlNameEasy()
    elif Sel == "3":
        OldName = input("请输入要修改的姓名：")
        if OldName in NameLi:
            NewName = input("请输入新的姓名：")
            index = NameLi.index(OldName)
            #index = NameLi.index(OldName) 获取旧姓名的索引位置
            NameLi[index] = NewName
            print(f"已修改姓名：{OldName} -> {NewName}")
        else:
            print("姓名不存在！")
        return SqlNameEasy()
    elif Sel == "4":
        Name = input("请输入要查找的姓名：")
        if Name in NameLi:
            print(f"找到了姓名：{Name}")
        else:
            print("姓名不存在！")
        return SqlNameEasy()
    elif Sel == "5":
        print("退出程序")
        return
    else:
        print("无效选项！")
        return SqlNameEasy()
SqlNameEasy ()    