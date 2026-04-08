# 换行是不需要;结尾
print(100) # 整数(int)
print(3.14) # 浮点数/小数
print(True) # 布尔(bool)
print(False) # 布尔(bool)
print("hello world") # 字符串(str)
print(None) # 空值(None)


# 变量 ----> Python是动态类型的语言,一个变量可以存储不同类型的数据(但项目开发中,推荐只存储一种类型的数据)
# 布尔类型本质也是整数类型True:1 , False:0
print(True + 1) # 2
print(False - 1) # -1

# 变量
num = 1114.1
print(num)

num = num + 1
print(num)

num = "OK"
print(num)

num = True
print(num)

# 案例

base = 20.7 # 基础播放量
incr = 50 # 每一个月的新增播放量
print("未来第一个月的播放总量: ", base + incr)
print("未来第二个月的播放总量: ", base + incr + incr)

# 案例 - 升级：一次性可以定义多个变量
base, incr = 20.7, 50
print("未来第一个月的播放总量: ", base + incr)
print("未来第二个月的播放总量: ", base + incr + incr)