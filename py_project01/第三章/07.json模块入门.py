import json
# 写入json数据文件
user = {
    "name": "余总",
    "age": 18,
    "gender": "男",
    "hobbies": ["读书","游泳"]
}
with open("resources/a.json","w",encoding="utf-8") as f:
    # ensure_ascii:默认为True ,确保所有的数据输出的都是ascii编码(非ASCII码会进行转义);False,非ASCII码保留原因输出
    # indent: 会在输出的json数据中添加缩进(格式化)
    json.dump(user,f,ensure_ascii=False,indent=2)

#  读取json数据文件
with open("resources/a.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))
