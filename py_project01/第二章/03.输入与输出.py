# 获取键盘上输入的数据 ---> input()
name = input("请输入你的姓名: ")
age = input("请输入你的年龄: ")
print(f"您的姓名是{name},年纪为:{age}")


total = 10000
money = input("请输入金额: ")
print(f"还剩{total - int(money)}")