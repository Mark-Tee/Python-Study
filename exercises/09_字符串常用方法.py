"""练习 9 — 字符串常用方法
输入一段英文，分别：
  - 转大写
  - 转小写
  - 首字母大写
  - 去掉两端空格
  - 按空格切分成列表
  - 统计字母 'a' 的出现次数
"""

text = input("请输入一段英文：")

print(f"转大写：{text.upper()}")
print(f"转小写：{text.lower()}")
print(f"首字母大写：{text.capitalize()}")
print(f"去掉两端空格：'{text.strip()}'")
print(f"按空格切分：{text.split()}")
print(f"字母 'a' 出现次数：{text.count('a')}")
