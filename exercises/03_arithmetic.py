"""练习 3 — 算术运算
输入两个数字，输出它们的：
  和、差、积、普通除法(/)、整除(//)、取余(%)、幂(**)
"""

a = int(input("请输入第一个数字："))
b = int(input("请输入第二个数字："))

print(f"和：{a + b}")
print(f"差：{a - b}")
print(f"积：{a * b}")
print(f"普通除法：{a / b}")
print(f"整除：{a // b}")
print(f"取余：{a % b}")
print(f"幂(a 的 b 次方)：{a ** b}")
