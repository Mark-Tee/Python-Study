"""练习 2 — input() 与 f-string 格式化
用 input 输入姓名、年龄、身高，然后用 f-string 格式化输出：
  我叫XX，今年XX岁，身高XX米。
"""

name = input("请输入姓名：")
age = input("请输入年龄：")
height = input("请输入身高(m)：")
print(f"我叫{name}，今年{age}岁，身高{height}米")
