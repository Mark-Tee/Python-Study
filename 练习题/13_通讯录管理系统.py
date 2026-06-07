"""
==================== 通讯录管理系统 ====================

🟢 难度：中等（综合练习）
📌 涉及知识点：字典、列表、函数、字符串操作、输入验证、类型转换

需求：
实现一个通讯录管理系统，支持以下功能：
1. 添加联系人（姓名 + 手机号）
2. 删除联系人
3. 查找联系人（支持按姓名或手机号查找）
4. 显示所有联系人
5. 退出系统

要求：
1. 手机号必须是 11 位数字（用 isdigit() 和 len() 校验）
2. 姓名不能重复（添加时检查是否已存在）
3. 查找支持模糊搜索：输入部分姓名或部分手机号都能找到匹配项
4. 联系人按姓名首字母排序显示（用 sorted() + key）
5. 使用函数封装每个功能，主流程调用函数

==================== 提示与思路 ====================

数据结构建议：用字典存储，键为姓名，值为手机号
    contacts = {"张三": "13800138000", "李四": "13900139000"}

具体编码提示见代码下方。
"""

# ==================== 你的代码写在下面 ====================

def add_contact(contacts: dict) -> None:
    """添加联系人"""
    # TODO: 1. 输入姓名，检查是否已存在
    add_name = input("输入姓名:\n").strip()
    if add_name in contacts :
        print("姓名已存在\n")
    else : 
        # TODO: 2. 输入手机号，检查是否为 11 位纯数字
        add_num = input("输入手机号:\n")
        if (add_num.isdigit() and len(add_num) == 11 ):
            contacts[add_name] = add_num
            # TODO: 3. 添加成功后打印确认信息
            print(f"您输入的信息为：\n姓名：{add_name}\n电话：{add_num}")
        else :
            print("输入号码有误\n")


def delete_contact(contacts: dict) -> None:
    """删除联系人"""
    # TODO: 1. 输入姓名
    del_name = input("请输入想要删除的姓名")
    # TODO: 2. 检查是否存在，存在则删除并打印确认；不存在则提示
    if del_name in contacts :
        del contacts[del_name]
        print(f"已删除{del_name}\n")
    else:
        print(f"不存在{del_name}\n")


def search_contact(contacts: dict) -> None:
    """查找联系人（模糊搜索：支持按姓名或手机号部分匹配）"""
    # TODO: 1. 输入搜索关键词
    ser_info = input("输入搜索关键词,支持按姓名或手机号部分匹配:\n").strip()
    # TODO: 2. 遍历字典，找到姓名或手机号中包含关键词的所有匹配项
    results = []
    for key , val in contacts.items():
    # TODO: 3. 输出所有匹配结果；没有匹配则提示
        if(ser_info in key or ser_info in val) :
            results.append((key,val))
    # print(results)
    if results :
            for info in results:
                print(f"姓名: {info[0]}, 手机号: {info[1]}")
    else:
            print("没有结果")

def show_all(contacts: dict) -> None:
    """显示所有联系人（按姓名首字母排序）"""
    # TODO: 1. 判断通讯录是否为空
    if len(contacts) == 0 :
        print("未输入任何信息\n")
    # TODO: 2. 用 sorted() 按姓名排序，遍历输出
    else :
        for key,val in sorted(contacts.items()) :
            # TODO: 3. 每行格式: "姓名: xxx, 手机号: xxx"
            print(f"姓名：{key}，手机号:{val}")



def main():
    """主函数：菜单循环"""
    contacts = {}  # 通讯录，键=姓名，值=手机号
    menu = """
    ===== 通讯录管理系统 =====
    1. 添加联系人
    2. 删除联系人
    3. 查找联系人
    4. 显示所有联系人
    5. 退出
    =========================="""

    while True:
        print(menu)
        choice = input("请输入操作编号 (1-5): ").strip()

        # TODO: 根据 choice 调用对应函数
        if choice =='1' :
            add_contact(contacts)
        elif choice == '2' :
            delete_contact(contacts)
        elif choice == '3' :
            search_contact(contacts)
        elif choice == '4' :
            show_all(contacts)
        elif choice == '5' :
            break
        # 提示: 1→add_contact  2→delete_contact  3→search_contact
        #       4→show_all  5→break


# 如果直接运行此文件，执行主函数
if __name__ == "__main__":
    main()


# ==================== 详细编码提示 ====================

"""
【提示 1：添加联系人】
    name = input("请输入姓名: ").strip()
    if name in contacts:
        print(f"联系人 \"{name}\" 已存在！")
        return
    phone = input("请输入手机号: ").strip()
    if not (len(phone) == 11 and phone.isdigit()):
        print("手机号必须是 11 位数字！")
        return
    contacts[name] = phone
    print(f"✓ 已添加 {name}: {phone}")

【提示 2：删除联系人】
    name = input("请输入要删除的联系人姓名: ").strip()
    if name in contacts:
        del contacts[name]  # 或 contacts.pop(name)
        print(f"✓ 已删除 {name}")
    else:
        print(f"未找到联系人 \"{name}\"")

【提示 3：模糊搜索】
    keyword = input("请输入关键词（姓名或手机号的一部分）: ").strip()
    results = []
    for name, phone in contacts.items():
        if keyword in name or keyword in phone:
            results.append((name, phone))
    if results:
        print(f"找到 {len(results)} 个匹配：")
        for name, phone in results:
            print(f"  姓名: {name}, 手机号: {phone}")
    else:
        print(f"未找到包含 \"{keyword}\" 的联系人")

【提示 4：排序显示】
    if not contacts:
        print("通讯录为空")
        return
    print(f"共 {len(contacts)} 个联系人：")
    for name in sorted(contacts.keys()):  # sorted() 返回按字母排序的键列表
        print(f"  姓名: {name}, 手机号: {contacts[name]}")
"""
