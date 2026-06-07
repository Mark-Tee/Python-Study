"""练习 11 — 学生管理系统（while 循环版）

功能菜单：
  1. 查看所有学生
  2. 添加学生
  3. 删除学生
  4. 退出程序

要求：
  - 用 while 循环让程序一直运行，直到选 4 退出
  - 用 if/elif 处理菜单选择
  - 用列表操作完成增、查、删
"""

students = ['张三', '李四', '王五']

while True:
    print("\n" + "=" * 20)
    print("1. 查看所有学生")
    print("2. 添加学生")
    print("3. 删除学生")
    print("4. 退出程序")
    print("=" * 20)

    choice = input("请选择(1-4)：")

    if choice == "1":
        if students:
            print("当前学生名单：")
            for i, name in enumerate(students, 1):
                print(f"  {i}. {name}")
        else:
            print("名单为空")

    elif choice == "2":
        name = input("请输入要添加的学生姓名：")
        students.append(name)
        print(f"✅ 已添加：{name}")

    elif choice == "3":
        name = input("请输入要删除的学生姓名：")
        if name in students:
            students.remove(name)
            print(f"✅ 已删除：{name}")
        else:
            print(f"❌ 名单中不存在：{name}")

    elif choice == "4":
        print("👋 已退出程序")
        break

    else:
        print("❌ 无效选项，请输入 1-4")
