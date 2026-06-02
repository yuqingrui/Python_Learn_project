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

# 匿名函数
# 需求1：打印一个分割线
# def out_line():
#     print("------------------------")

out_line = lambda : print("----------------------------------")
out_line()

# 需求2：计算两个数之和
# def addd(x, y):
#     return x + y

add = lambda x, y : x + y
print(add(x=100, y=200))

# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

data_list.sort(key=lambda item : len(item))
print(data_list)

# ======================================================
# csv_data
# ======================================================

# 案例1：计算n的阶乘
# 递归调用(先层层递进，再逐层回归)：指的是在函数中自己调用自己的情况 ----> 一定得有终结点
"""
jc(10) = 10 * jc(9)
jc(9) = 9 * jc(8)
jc(8) = 8 * jc(7)
jc(7) = 7 * jc(6) = 7 * 720 = 5040
jc(6) = 6 * jc(5) = 6 * 120 = 720
jc(5) = 5 * jc(4) = 5 * 24 = 120
jc(4) = 4 * jc(3) = 4 * 6 = 24
jc(3) = 3 * jc(2) = 3 * 2 = 6
jc(2) = 2 * jc(1) = 2 * 1 = 2
jc(1) = 1
"""

def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)

result = jc(10)
print(result)

# 案例2：根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
"""
:param args: 商品信息（商品名、价格、数量） ----> 如：("鼠标", 188, 2) ("键盘", 388, 1)
:param coupon: 优惠券
:param score: 积分
:param express: 运费
:return: 订单的总金额
"""

# 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费

def calc_order_cost(*args, coupon=0, score=0, express=0):
    # 1. 计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    print(f"商品总金额: {total_cost}")
    
    # 2. 扣减优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
        print(f"优惠券抵扣: -{coupon}")
    
    # 3. 扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
        print(f"积分抵扣: -{score // 100}")
    
    # 4. 添加运费
    total_cost += express
    print(f"运费: +{express}")
    
    print(f"订单的总金额: {total_cost}")
    return total_cost


# 测试案例2
print("\n========== 案例2测试 ==========")

# 测试
# total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 3999, 1), coupon=10, score=4000, express=9.9)
# print(total)

# total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1), coupon=10, score=4000, express=9.9)
# print(total)

total = calc_order_cost(("鼠标", 188, 2),("键盘", 388, 1),("手机", 6999, 1), express=9.9)
print(total)

