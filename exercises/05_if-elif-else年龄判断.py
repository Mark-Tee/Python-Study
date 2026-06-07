"""练习 5 — if-elif-else 条件判断
输入年龄，根据以下规则输出：
  < 18  → 未成年人
  18~60 → 成年人
  > 60  → 老年人
"""

age = int(input("请输入年龄："))

if age < 18:
    print("未成年人")
elif age <= 60:
    print("成年人")
else:
    print("老年人")
