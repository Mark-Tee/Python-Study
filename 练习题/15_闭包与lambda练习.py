"""
==================== 闭包与 lambda 练习 ====================

🟢 难度：中等
📌 知识点：闭包、lambda、列表、字典、sorted

题目一：制作「累加器」闭包

实现 make_accumulator(step)，每次调用返回的数都比上次多 step：

    acc = make_accumulator(3)
    print(acc())   # 3
    print(acc())   # 6
    print(acc())   # 9

题目二：基于题目一，改造为 make_accumulator(start, step)

起始值和步长都可自定义：

    acc = make_accumulator(10, 5)
    print(acc())   # 15
    print(acc())   # 20

题目三：用 lambda 完成以下操作

    students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

    1. 用 sorted + lambda 按成绩从高到低排序
    2. 用 sorted + lambda 按姓名长度排序（短的在前）

题目四：统计每个分数段的次数（用 lambda + 字典推导式）

    scores = [85, 92, 78, 65, 90, 55, 72]
    分数段：60以下→"不及格", 60-79→"中等", 80-89→"良好", 90+→"优秀"
    输出: {"优秀": 2, "良好": 1, "中等": 2, "不及格": 2}

    提示：先写一个 lambda 判断分数段，再手动统计到字典。
"""

# ==================== 你的代码写在下面 ====================


# === 题目一 ===
def make_accumulator(step: int):
    """每次调用返回值比上次多 step"""
    total = 0

    def inner():
        # TODO
        nonlocal total
        total += step
        return total
    
    return inner


# === 题目二 ===
def make_accumulator_v2(start: int, step: int) -> int:
    """起始值 start，步长 step"""
    # TODO
    total = start
    step = step
    def inner():
        nonlocal total
        total += step
        return total
    return inner

# === 题目三 ===
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# 1. 按成绩从高到低排序
# sorted_1 = sorted(students, key=lambda ...)
# print(sorted_1)
sorted_1 = sorted(students, key=lambda x:x[1],reverse=True)
# 2. 按姓名长度排序（短的在前）
sorted_2 = sorted(students, key=lambda x:len(x[0]))
# print(sorted_2)


# === 题目四 ===
scores = [85, 92, 78, 65, 90, 55, 72]
to_grade = lambda s:"优秀" if s>=90 else("良好" if 80<=s<=89 else ("中等" if 60<=s<=79 else "不及格")) 
result = {}
for i in scores :
    grade = to_grade(i)
    if grade in result:
        result[grade]+=1
    else:
        result[grade]=1
# 提示：写一个 lambda，输入分数，返回等级字符串

# to_grade = lambda s: ...
# 然后遍历 scores，手动统计到字典


# ==================== 测试区域 ====================
if __name__ == "__main__":
    # 题目一
    print("=== 题目一 ===")
    acc = make_accumulator(3)
    print(acc())   # 应输出 3
    print(acc())   # 应输出 6
    print(acc())   # 应输出 9

    # 题目二
    print("\n=== 题目二 ===")
    acc2 = make_accumulator_v2(10, 5)
    print(acc2())  # 应输出 15
    print(acc2())  # 应输出 20

    # 题目三
    print("\n=== 题目三 ===")
    print("按成绩排序:", sorted_1)
    # print("按姓名长度排序:", sorted_2)

    # 题目四
    print("\n=== 题目四 ===")
    print("分数段统计:", result)
