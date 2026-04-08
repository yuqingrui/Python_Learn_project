# for循环：遍历输入的字符串

# msg = input("请输入需要遍历的字符串：")
#
# for s in msg:  # s 表示遍历出来的元素； msg 表示需要遍历的数据
#     print(f"元素：{s}")
# else:
#     print("遍历结束！")


i = 0
total = 0
for i in range(100):
    if i % 2 != 0:
        total += i

print( total)
