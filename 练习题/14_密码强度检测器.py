"""
==================== 密码强度检测器 ====================

🟢 难度：简单偏中（热身练习）
📌 知识点：字符串、列表、循环、条件判断、函数

需求：
实现一个密码强度检测器，用户输入密码后，根据以下规则打分并评级。

评分规则（满分 10 分）：
| 条件                                       | 得分 |
|--------------------------------------------|------|
| 长度 ≥ 8 位                                | +2   |
| 长度 ≥ 12 位                               | +1（叠加，共 3）|
| 包含大写字母                                | +2   |
| 包含小写字母                                | +2   |
| 包含数字                                   | +2   |
| 包含特殊字符（如 !@#$%^&* 等）              | +1   |
| 大写、小写、数字都有 ≥ 2 个不同字符          | +1（奖励分）|

评级：
    0~3 分 → 「弱 🔴」建议：加长密码，混合字符类型
    4~6 分 → 「中 🟡」建议：增加特殊字符，拉长密码
    7~8 分 → 「强 🟢」不错！可再加一点特殊字符
    9~10分 → 「非常强 🟣」密码很安全！

要求：
1. 使用函数封装：check_length / check_upper / check_lower / check_digit / check_special / check_diversity
   每个函数返回对应的得分
2. 主函数 calculate_strength(password) 调用上述函数，汇总得分并返回评级
3. 允许用户循环检测多个密码，输入 q 退出
"""

# ==================== 你的代码写在下面 ====================


def check_length(password: str) -> int:
    """检查长度得分"""
    # TODO: len ≥ 12 → 3分, len ≥ 8 → 2分
    if len(password) >=12 :
        return 3
    elif len(password) >=8:
        return 2
    else :
        return 0


def check_upper(password: str) -> int:
    """检查是否包含大写字母"""
    # TODO: 遍历字符串，有任意大写 → 2分，否则 0
    for i in password :
        if i.isupper():
            return 2
    return 0

def check_lower(password: str) -> int:
    """检查是否包含小写字母"""
    # TODO: 有任意小写 → 2分，否则 0
    for i in password:
        if i.islower():
            return 2
    return 0


def check_digit(password: str) -> int:
    """检查是否包含数字"""
    # TODO: 有任意数字 → 2分，否则 0
    for i in password:
        if i.isdigit():
            return 2
    return 0


def check_special(password: str) -> int:
    """检查是否包含特殊字符"""
    # TODO: 有 !@#$%^&*()-_=+[]{};:'\",.<>?/~` 等 → 1分，否则 0
    for i in password:
        if i in "!@#$%^&*()-_=+[]{};:'\",.<>?/~":
            return 1
    return 0


def check_diversity(password: str) -> int:
    """检查字符多样性：大写、小写、数字分别至少有 2 个不同字符 → 1分"""
    # TODO: 统计不同的大写/小写/数字个数，各有 ≥ 2 → +1
    pw = {i for i in password}
    uppass = [i for i in pw if i.isupper()]
    lowpass = [i for i in pw if i.islower()]
    digpass = [i for i in pw if i.isdigit()]
    if  len(uppass)>=2 and  len(lowpass)>=2  and len(digpass)>=2:
        return 1
    else :
        return 0


def get_level(score: int) -> str:
    """根据总分返回评级文字"""
    # TODO: 按评分规则返回对应评级
    if  0<= score<=3 :
        return "[弱] 建议：加长密码，混合字符类型"
    elif 4<= score<=6  :
        return "[中] 建议：增加特殊字符，拉长密码"
    elif 7<= score<=8  :
        return "[强] 不错！可再加一点特殊字符"
    else:
        return "[非常强] 密码很安全！"


def calculate_strength(password: str) -> tuple[int, str]:
    """
    汇总所有得分，返回 (总分, 评级)
    """
    score = check_length(password) + check_upper(password) + check_lower(password) +check_digit(password)+check_special(password)+check_diversity(password)
    level = get_level(score)
    # TODO: 调用上面的函数，汇总分数
    print(f"总分：{score}等级：{level}")
    return (score,level)


def main():
    """主函数：循环检测"""
    print("=" * 40)
    print("** 密码强度检测器 (输入 q 退出) **")
    print("=" * 40)

    while True:
        password = input("\n请输入密码: ").strip()
        if password.lower() == 'q':
            print("再见！")
            break
        if not password:
            print("密码不能为空！")
            continue

        # TODO: 调用 calculate_strength，打印总分和评级
        calculate_strength(password)

if __name__ == "__main__":
    main()


# ==================== 编码提示 ====================

"""
【提示 1：检查某类字符】
    用 for 循环 + 字符串方法：
    - 大写: char.isupper()
    - 小写: char.islower()
    - 数字: char.isdigit()
    只要找到一个就返回对应分数

【提示 2：检查特殊字符】
    定义特殊字符集，然后遍历检查：
    special_chars = "!@#$%^&*()-_=+[]{};':\",.<>?/`~"
    for char in password:
        if char in special_chars:
            return 1
    return 0

【提示 3：check_diversity】
    用 set 收集不同的大写/小写/数字字符：
    upper_set = set()
    for char in password:
        if char.isupper():
            upper_set.add(char)
    然后判断 len(upper_set) >= 2 and len(lower_set) >= 2 and len(digit_set) >= 2

【提示 4：get_level 参考】
    def get_level(score):
        if score <= 3:
            return '弱 🔴 — 建议：加长密码，混合字符类型'
        elif score <= 6:
            return '中 🟡 — 建议：增加特殊字符，拉长密码'
        ...
"""
