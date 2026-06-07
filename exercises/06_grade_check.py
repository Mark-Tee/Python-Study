"""练习 6 — 多分支分数等级
输入分数(0-100)，输出等级：
  90~100 → A
  80~89  → B
  60~79  → C
  <60    → D
"""

score = int(input("请输入分数(0-100)："))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")
