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
n = int(input("请输入直角边的边长："))

for i in range(1, n + 1):  # 外层循环控制行数
    for j in range(i):  # 内层循环控制每行打印的星号数量
        print("*", end=" ")
    print()


print("------------------------")

# 需求2：根据输入的数字，打印对应的数字金字塔
n = int(input("请输入数字金字塔的层数："))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("------------------------")

# 需求3：打印国际象棋棋盘
for i in range(8):  # 8行
    for j in range(8):  # 8列
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

"""
案例1：根据输入的用户名密码执行登录操作，具体要求如下：
1. 正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
2. 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
3. 输入的用户名和密码不能为空！
4. 登录成功：输出 "登录成功，进入B站首页~"
5. 登录失败：输出 "用户名或密码错误，请重新输入！"

关键字：
    break：只能够出现在循环中，表示结束、跳出循环的含义（break跳出循环时，while后面的else中的代码将不会执行）
    continue：只能够出现在循环中，表示中断本次循环，直接进入下一次循环
"""

while True:
    # 1. 接收输入的用户名和密码
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")

    # 2. 校验：输入的用户名和密码不能为空！
    if username == "" or password == "":
        print("输入的用户名和密码不能为空！请重新输入")
        continue  # 结束当前循环，直接进入下一轮循环

    # 3. 判断用户名和密码的正确性，执行登录操作
    if username == "admin" and password == "666888":
        print("登录成功，进入B站首页~")
        break  # 跳出循环
    elif username == "zhangsan" and password == "123456":
        print("登录成功，进入B站首页~")
        break  # 跳出循环
    elif username == "taoge" and password == "888666":
        print("登录成功，进入B站首页~")
        break  # 跳出循环
    else:
        print("用户名或密码错误，请重新输入！")

print("------------------------")

"""
案例2：猜数字游戏
1. 系统随机生成一个随机数
2. 用户根据提示猜数字，并将所猜的数字输入系统
3. 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
4. 如果猜对，系统自动退出，游戏结束
"""

import random
random_num = random.randint(1, 100)  # 生成随机数

while True:
    # 接收输入的数字
    num = int(input("请输入一个数字："))

    # 比较
    if num > random_num:
        print("您输入的数字太大了！")
    elif num < random_num:
        print("您输入的数字太小了！")
    else:
        print("恭喜您，猜对了，666")
        break  # 跳出循环

print("随机生成的数字是：", random_num)

print("------------------------")

# 练习：完成如下需求
# 需求1：将1-1000之间（含1000）所有的5的倍数的数字累加起来。
total = 0
for i in range(1, 1001):
    if i % 5 == 0:
        total += i
print(f"1-1000之间所有5的倍数的累加之和为：{total}")

print("------------------------")

# 需求2：统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
str1 = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
count_a = 0
count_k = 0
for char in str1:
    if char == "a":
        count_a += 1
    elif char == "k":
        count_k += 1
print(f"字符串中a的个数为：{count_a}")
print(f"字符串中k的个数为：{count_k}")

