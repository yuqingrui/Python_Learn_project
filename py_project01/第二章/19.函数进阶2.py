# 加
def add(x, y):
    return x+y

# 减
def subtract(x, y):
    return x-y

# 乘
def multiply(x, y):
    return x*y

# 除
def divide(x, y):
    return x/y

# 计算
def calc(x, y, oper):
    return oper(x, y)

print(calc(x=10, y=20, oper=add))
