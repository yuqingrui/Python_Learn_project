# csv操作 -方式一 :文件操作的原始方式
# 写
with open("csv_data/01.csv","w",encoding="utf-8") as f:
    f.write("姓名,年龄,爱好\n") # 写入表头
    f.write("小王,18,男,football\n") # 写入数据
    f.write("小李,18,男,Python\n")
    f.write("小张,18,女,C++\n")
    f.write("小张,18,男,Go\n")

# 读
with open("csv_data/01.csv","r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# csv操作 -方式二 :文件操作的原始方式
import csv

with open("csv_data/02.csv","w",encoding="utf-8") as f:
    writer = csv.DictWriter(f , fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader() # 写入表头
    writer.writerow({"姓名":"小王","年龄":18,"性别":"男","爱好":"Java"}) # 写入数据

# 读
with open("csv_data/02.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
