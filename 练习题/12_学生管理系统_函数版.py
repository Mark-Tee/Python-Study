"""练习 12 — 学生管理系统（函数版）

在练习 11 的基础上扩展，支持：
  1. 增加姓名    2. 删除姓名
  3. 修改姓名    4. 查找姓名
  5. 查看全部    6. 退出

要求：
  - 用函数封装每个功能
  - 用字典存姓名 + 年龄（升级为更完整的数据结构）
"""

students = []  # 每个元素是 {"name": 姓名, "age": 年龄}


def show_menu():
    print("\n" + "=" * 25)
    print("1. 增加  2. 删除  3. 修改")
    print("4. 查找  5. 查看  6. 退出")
    print("=" * 25)


def add_student():
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    students.append({"name": name, "age": age})
    print(f"✅ 已添加：{name}, {age}岁")


def delete_student():
    name = input("请输入要删除的姓名：")
    for s in students:
        if s["name"] == name:
            students.remove(s)
            print(f"✅ 已删除：{name}")
            return
    print(f"❌ 不存在：{name}")


def modify_student():
    name = input("请输入要修改的姓名：")
    for s in students:
        if s["name"] == name:
            new_name = input("请输入新姓名（回车保留原名）：")
            new_age = input("请输入新年龄（回车保留原年龄）：")
            if new_name:
                s["name"] = new_name
            if new_age:
                s["age"] = new_age
            print(f"✅ 已修改")
            return
    print(f"❌ 不存在：{name}")


def search_student():
    name = input("请输入要查找的姓名：")
    for s in students:
        if s["name"] == name:
            print(f"✅ 找到：{s['name']}, {s['age']}岁")
            return
    print(f"❌ 不存在：{name}")


def view_all():
    if not students:
        print("名单为空")
        return
    print("当前学生名单：")
    for i, s in enumerate(students, 1):
        print(f"  {i}. {s['name']}, {s['age']}岁")


def main():
    while True:
        show_menu()
        choice = input("请选择(1-6)：")
        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            modify_student()
        elif choice == "4":
            search_student()
        elif choice == "5":
            view_all()
        elif choice == "6":
            print("👋 已退出")
            break
        else:
            print("❌ 无效选项")


main()
