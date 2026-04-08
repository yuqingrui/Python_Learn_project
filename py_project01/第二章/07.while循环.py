# i = 0
# while i < 10:
#     print("我爱Python")
#     i += 1
# else:
#     print("循环结束")
#
#

# while案例：计算1-100之间所有偶数的累加之和
total = 0  # 记录累加之和   total: 0
i = 1  # 循环开始数字   i: 1

while i <= 100:
    if i % 2 == 0:  # 偶数
        total += i
    i += 1

print(f"1-100之间所有偶数的累加之和为：{total}")
