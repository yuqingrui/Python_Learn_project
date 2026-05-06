

# 字符串 基本操作 ---> 不可变的(无法修改)、有序性、可迭代性
s = "Hello-Python"

print(s[4])  # 正向索引
print(s[-8])  # 反向索引

for i in s:
    print(i)

# 切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[6:12:1])  # 从索引6到11，步长为1
print(s[6::1])  # 从索引6到末尾，步长为1

print("-------------------------------")
# 步长 --> 正数：从前往后截取 ；负数：从后往前截取
print(s[-1:-7:-1])  # 从索引-1到-6，步长为-1（反向截取）
print(s[::-1])  # 整个字符串反转，步长为-1


# ---------------------------------- 字符串常用方法 ----------------------------------
s = "Hello-Python-Hello-World"

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

# count() 统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)

# upper() 转为大写
su = s.upper()
print(su)

# lower() 转为小写
sl = s.lower()
print(sl)

# split() 将字符串按照指定字符串切割 -> 列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空格
ss = s.strip()

# replace() 将字符串中的指定子串替换为新的内容
sr = s.replace("-",  "_")
print(sr)

# startswith() / endswith() 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))

print("--------------------------------------------------")
print(s)


# ---------------------------------- 字符串案例 ----------------------------------
# 案例1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出“邮箱格式正确”，否则输出“邮箱格式错误”。

# 1. 接收用户输入的邮箱
mail = input("请输入邮箱：")

# 2. 判断邮箱的格式
if mail.count("@") == 1 and mail.count(".") >= 1:
    print(f"{mail} 是合法的邮箱")
else:
    print(f"{mail} 是非法的邮箱")


# 方式一： in 运算符 ---> 判断串是否包含在字符串中，存在，返回True；否则，返回False
# 1. 接收用户输入的邮箱
mail = input("请输入邮箱：")

# 2. 判断邮箱的格式
if mail.count("@") == 1 and "." in mail:
    print(f"{mail} 是合法的邮箱")
else:
    print(f"{mail} 是非法的邮箱")


# ---------------------------------- 练习 1：回文判断 ----------------------------------
# 1. 输入一个字符串，判断该字符串是否是回文(两边对称)。
s1 = input("请输入一个字符串：")
# 使用切片[::-1]反转字符串并与原字符串比较
if s1 == s1[::-1]:
    print(f"'{s1}' 是回文")
else:
    print(f"'{s1}' 不是回文")

# ---------------------------------- 练习 2：字符串处理与列表 ----------------------------------
# 2. 将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
result_list = []
print("请依次输入10个字符串：")
for _ in range(10):
    user_input = input("请输入：")
    # 反转并转大写
    processed_str = user_input[::-1].upper()
    result_list.append(processed_str) # 添加到列表 result_list 的末尾

print("\n处理后的列表内容：")
for item in result_list:
    print(item)


