"""练习 7 — while 循环求和
用 while 循环计算 1+2+…+10，输出总和。
"""

total = 0
i = 1

while i <= 10:
    total += i
    i += 1

print(f"1+2+…+10 = {total}")  # → 55
