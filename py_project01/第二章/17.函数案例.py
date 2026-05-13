# 案例1：定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。
def triangle_area(b, h):
    """
    根据传入的底和高计算三角形面积
    :param b: 底长
    :param h: 高
    :return: 三角形面积
    """
    return b * h / 2

print("底长为 30，高度为 20 的三角形面积：", triangle_area(b=30, h=20))

# 案例2：定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
def count_aeiou(s):
    """
    统计字符串中元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num

print(count_aeiou("Hello Python Hello World OK"))

# 案例3：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
def calc_score(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param score_list: 分数列表
    :return: 最高分，最低分，平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg_s

s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
max_score, min_score, avg_score = calc_score(s_list)
print("最高分：", max_score)
print("最低分：", min_score)
print("平均分：", avg_score)

# 练习1：定义一个函数，根据传入的分数，计算对应的分数等级并返回。
def get_grade(score):
    """
    根据分数返回等级
    :param score: 分数
    :return: 等级 A/B/C/D
    """
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'D'

print("分数95的等级：", get_grade(95))
print("分数80的等级：", get_grade(80))
print("分数65的等级：", get_grade(65))
print("分数50的等级：", get_grade(50))

# 练习2：定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
def is_palindrome(s):
    """
    判断字符串是否是回文串
    :param s: 字符串
    :return: True或False
    """
    return s == s[::-1]

print("level 是回文串吗？", is_palindrome("level"))
print("radar 是回文串吗？", is_palindrome("radar"))
print("黄山落叶松叶落山黄 是回文串吗？", is_palindrome("黄山落叶松叶落山黄"))
print("hello 是回文串吗？", is_palindrome("hello"))

# 练习3：定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def convert_seconds(total_seconds):
    """
    将秒数转换为小时、分钟、秒
    :param total_seconds: 总秒数
    :return: 小时，分钟，秒
    """
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

h, m, s = convert_seconds(3661)
print("3661秒 =", h, "小时", m, "分钟", s, "秒")

# 练习4：定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型。
def triangle_type(a, b, c):
    """
    判定三角形的类型
    :param a: 边长a
    :param b: 边长b
    :param c: 边长c
    :return: 三角形类型字符串
    """
    # 先判断是否能构成三角形
    if a + b <= c or a + c <= b or b + c <= a:
        return "不能构成三角形"
    # 判断等边三角形
    elif a == b == c:
        return "等边三角形"
    # 判断等腰三角形
    elif a == b or b == c or a == c:
        return "等腰三角形"
    # 其他情况为普通三角形
    else:
        return "普通三角形"

print("边长3,4,5 的三角形类型：", triangle_type(3, 4, 5))
print("边长3,3,3 的三角形类型：", triangle_type(3, 3, 3))
print("边长3,3,5 的三角形类型：", triangle_type(3, 3, 5))
print("边长1,2,3 的三角形类型：", triangle_type(1, 2, 3))
