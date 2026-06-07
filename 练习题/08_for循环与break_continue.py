"""练习 8 — for + range + break + continue
用 for + range 打印 1~20 之间所有奇数：
  - 遇到 13 用 continue 跳过
  - 遇到 19 用 break 停止
"""

odd_nums = []

for i in range(1, 21):
    if i == 19:
        break        # 遇到 19 立即停止循环
    if i == 13:
        continue     # 遇到 13 跳过，不加入列表
    if i % 2 != 0:
        odd_nums.append(i)

print(odd_nums)  # → [1, 3, 5, 7, 9, 11, 15, 17]

# ⚠️ 注意：break 在 19 时触发，所以 19 不会被加入；
#        13 被 continue 跳过，也不会出现。
