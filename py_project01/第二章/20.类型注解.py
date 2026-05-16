# 变量定义 - 未指定类型注解 --->

a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count":2 , "total":10}
goods = ("手机", 6999, 1)

names.append("X")
names.append(10010)


# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}


# 函数类型注解
def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(8.5)
print(al)


def calc_order_cost(*args:tuple[str, float, int], coupon:int=0, score:int=0, express:int=0):
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
