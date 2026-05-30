# 读文件
#1.打开文件
f = open("resources/a.txt","r",encoding="utf-8")
#2.读取文件内容
content = f.read() # 读取所有内容
print(content)

content_list = f.readlines() # 逐行读取
for line in content_list:
    print(line.strip())

# 3.关闭文件
f.close()

# 写文件
# 1.打开文件
f2 = open("resources/a.txt","w",encoding="utf-8")
# 2.写入文件内容
f2.write("哈哈哈哈哈或或\n")
f2.close()


#  ======================================释放资源 方式一================================================
# 写文件
# 1.打开文件
f3 = open("resources/a.txt","w",encoding="utf-8")
try:
    f3.write("666666666666666\n");
finally:
    f.close() #关闭资源


#  ======================================释放资源 方式二================================================
# 写文件
# 1.打开文件
with open("resources/a.txt","w",encoding="utf-8") as f:
    # 2.写入文件内容
    f3.write("666666666666666\n");
