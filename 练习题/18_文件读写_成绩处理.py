"""
==================== 文件读写 + 成绩数据处理 ====================

🟢 难度：中等
📌 知识点：open()、read/write、with、split、map、filter、sorted

你新学的文件操作，搭配之前的数据处理工具，做一个完整的成绩分析器。

题目：读取 scores.txt，每行格式为 "姓名,成绩"。计算总分、平均分、
最高分的学生，以及及格率（≥60），结果写入 result.txt。

示例 scores.txt：
    张三,85
    李四,92
    王五,58
    赵六,78
    钱七,45

预期 result.txt：
    === 成绩分析报告 ===
    总人数: 5
    总分: 358
    平均分: 71.6
    最高分: 李四 (92分)
    及格率: 60.0%
"""

# ═══════════════════════════════════════════════════════════
# 预备步骤：先创建 scores.txt 测试文件

def create_test_file():
    """创建测试用的 scores.txt"""
    data = [
        "张三,85",
        "李四,92",
        "王五,58",
        "赵六,78",
        "钱七,45",
    ]
    with open("scores.txt", "w", encoding="utf-8") as f:
        for line in data:
            f.write(line + "\n")
    print("[OK] 已创建 scores.txt")


# ═══════════════════════════════════════════════════════════
# 题目：实现 analyze() 函数，读取 scores.txt → 分析 → 写入 result.txt

def analyze():
    """
    1. 读取 scores.txt，每行 "姓名,成绩"
    2. 解析为 [(姓名, 成绩), ...] 列表
    3. 计算：总人数、总分、平均分、最高分（含姓名）、及格率
    4. 写入 result.txt（格式参照上方示例）
    """
    # === 步骤 1：读取文件 ===
    students = []
    with open("scores.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()           # 去掉换行符
            if not line:                  # 跳过空行
                continue
            name, score = line.split(",") # 按逗号拆开
            students.append((name, int(score)))

    # TODO: 补充步骤 1 的读取逻辑（参考上面的框架）
    pass

    # === 步骤 2：计算统计 ===
    # 提示：
    #   总人数 = len(students)
    manNum = len(students)
    #   总分   = sum(score_list) 或用 reduce
    from functools import reduce
    grade = [x[1] for x in students]
    allGrade = reduce(lambda x,y:x+y,grade)
    #   平均分 = 总分 / 总人数
    arvGrade = allGrade / manNum
    #   最高分 = max(students, key=lambda x: x[1])
    topname,topgrade = max(students,key=lambda x:x[1])
    #   及格率 = len([s for s in students if s[1] >= 60]) / 总人数 * 100
    perGrade = len([x for x in students if x[1] >=60])/manNum *100
    # === 步骤 3：写入 result.txt ===
    # 提示：
    #   with open("result.txt", "w", encoding="utf-8") as f:
    #       f.write("=== 成绩分析报告 ===\n")
    #       f.write(f"总人数: {total}\n")
    #       ...
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("=== 成绩分析报告 ===\n")
        f.write(f"总人数: {manNum}\n")
        f.write(f"总分: {allGrade}\n")
        f.write(f"平均分: {arvGrade}\n")
        f.write(f"最高分: {topgrade},是{topname}\n")
        f.write(f"及格率: {perGrade}%\n")




# ==================== 测试区域 ====================
if __name__ == "__main__":
    create_test_file()
    analyze()
    print("\n生成的结果文件：")
    with open("result.txt", "r", encoding="utf-8") as f:
        print(f.read())
