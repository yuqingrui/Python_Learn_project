# for循环：遍历输入的字符串

# msg = input("请输入需要遍历的字符串：")
#
# for s in msg:  # s 表示遍历出来的元素； msg 表示需要遍历的数据
#     print(f"元素：{s}")
# else:
#     print("遍历结束！")


# total = 0
# for i in range(100):
#     if i % 2 == 1:
#         total += i
#
# print( total)
#
# #简化 步长为2
# total1 = 0
# for i in range(1,100,2):
#     if i % 2 == 1:
#         total1 += i
#
# print("------------------------")
#
# # 案例2：计算 100-500 之间所有3的倍数的数字之和
# total = 0  # 记录累加之和
#
# for i in range(100, 501):
#     if i % 3 == 0:  # i 是3的倍数
#         total += i
#
# print("100-500之间3的倍数累加之和：", total)
#
# print("------------------------")

"""
循环嵌套：根据输入的长方形的长度m，宽度n，打印一个长方形；

如下：是一个长度为10，宽度为5的长方形

print("*")：自带换行效果，每一次执行都会输出新的一行中；
print("*", end="")：end表示的是每一次输出以什么结束；默认\n，表示换行。
"""

# 1. 接收键盘录入m, n
# 长度
# m = int(input("请输入长方形的长度："))
# # 宽度
# n = int(input("请输入长方形的宽度："))

# 2. 打印长方形
# for j in range(n):  # 控制行
#     for i in range(m):  # 控制列
#         print("*", end=" ")
#     print()
#
# print("------------------------")

# 嵌套循环案例：打印99乘法表
# for i in range(1, 10):  # 外层循环 - 控制行
#     for j in range(1, i + 1):  # 内层循环 - 控制列
#         print(f"{j} x {i} = {j * i}", end="\t")
#     print()
#
# print("------------------------")



print("------------------------")

# 需求1：根据输入的直角边的边长，打印等腰直角三角形
# n = int(input("请输入直角边的边长："))
#
# for i in range(1, n + 1):  # 外层循环控制行数
#     for j in range(i):  # 内层循环控制每行打印的星号数量
#         print("*", end=" ")
#     print()


for i in range(1, 7):  # 外层循环控制行数
    for j in range(i):  # 内层循环控制每行打印的星号数量
        print("*", end=" ")
    print()
