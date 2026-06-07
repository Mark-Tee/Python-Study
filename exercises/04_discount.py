"""练习 4 — 折扣计算 + 浮点格式化
输入商品原价，输入折扣（如 85 表示 85 折），计算折后价，
保留 2 位小数并输出 "XX元"。
"""

price = float(input("请输入商品原价："))
discount = int(input("请输入折扣（如 85 表示 85 折）："))

final_price = price * discount * 0.01
print(f"折后价：{final_price:.2f}元")
