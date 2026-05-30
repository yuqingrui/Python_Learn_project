# 读文件
"""
路径写法:

相对路径: 从当前文件所在目录开始查找(推荐)
    . : 当前目录 ---> ./resources/望庐山瀑布.txt   ./ 可以省略
    ..: 上一级目录 ---> ../第2章/file/寻隐者不遇.txt ---> ../../第2章/file/寻隐者不遇.txt

绝对路径: 从文件系统根目录开始查找, 文件位置的完整路径(注意: 反斜杠在字符串中表示的是转义字符, \n \t)
    方式一: D:\\Python-Project\\py_project01\\第3章\\resources\\望庐山瀑布.txt
    方式二: D:/Python-Project/py_project01/第3章/resources/望庐山瀑布.txt

"""

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


# ========================================== 示例代码 ================================================
# 读文件
with open("resources/望庐山瀑布.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


# 写文件
with open("resources/静夜思.txt", "w", encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
