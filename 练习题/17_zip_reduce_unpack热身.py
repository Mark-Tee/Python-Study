"""
==================== zip / reduce / 拆包 热身 ====================

🟢 难度：中等偏易（快速热手）
📌 知识点：zip、reduce、拆包、min/max+key

三道小题，15 分钟搞定。
"""

# ═══════════════════════════════════════════════════════════
# 题目一：zip 并行处理
# 用 zip 把两个列表合并成字典 {姓名: 年龄}，一行代码搞定。

names = ["Alice", "Bob", "Charlie"]
ages  = [25, 30, 22]
# TODO: name_age = ...
nameage = dict(zip(names,ages))
print(nameage)
# 结果：{'Alice': 25, 'Bob': 30, 'Charlie': 22}


# ═══════════════════════════════════════════════════════════
# 题目二：拆包
# 给定一个元组，用 a,*b 拆包，分别打印 a 和 b。

nums = (10, 20, 30, 40, 50)
# TODO: 拆包后 print(a), print(b)



# 应输出：10 和 [20, 30, 40, 50]


# ═══════════════════════════════════════════════════════════
# 题目三：reduce
# 用 reduce + lambda 求列表中所有数的乘积。
# 提示：from functools import reduce

data = [2, 3, 4, 5]
# TODO: result = ...
# 计算过程：2×3=6 → 6×4=24 → 24×5=120
# 结果：120


# ═══════════════════════════════════════════════════════════
# 附加题：min + key
# 找出身高列表中绝对值最接近 0 的数（即绝对值最小的那个）。
# 提示：用 min(xx, key=abs)

heights = [-5, 3, -1, 8, 2]
# TODO: closest = ...
# 结果：-1（绝对值 1 最小）


# ==================== 测试区域 ====================
if __name__ == "__main__":
    print("题目一:", dict(zip(names, ages)) if 'zip' in dir(__builtins__) else "TODO")
    print("题目二:", "TODO")
    a,*b = nums
    print(a)
    print(b)
    print("题目三:", "TODO")
    from functools import reduce
    res =  reduce(lambda a,b:a*b,data)
    print(res)
    print("附加题:", "TODO")
    closest = min(heights,key = abs)
    print(closest)
