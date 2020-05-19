# author: Ziming Guo
# time: 2020/2/11
'''
    作业7：
    重构 shopping
'''


def add_to_cart(commodity_number, count):
    """
    输入要买的商品编号 & 数量 ；返回购物车清单
    :param commodity_number: 商品编号
    :param count: 商品数量
    :return: 购物清单
    """
    order = []
    order.append({"commodity_number": commodity_number, "count": count})
    return order


def check_out_price(order):
    """
    输入购物车清单 & 拿多少钱，返回找零
    :param order: 购物车清单
    :return: 应付钱数
    """
    price = 0
    for item in order:
        commodity = commodity_info[item["commodity_number"]]  # 通过键（商品编号） 索引到了值（商品名称和价钱的字典）
        price += commodity["price"] * item["count"]
    return price


def check_out_change(price, money_from_customer):
    if money_from_customer >= price:
        change = money_from_customer - price
        return change
    else:
        return "金额不足!"


commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

while True:
    item = input("1键购买，2键结算。")
    if item == "1":
        for key, value in commodity_info.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

        while True:
            commodity_number = int(input("请输入商品编号："))
            if commodity_number in commodity_info:
                break
            else:
                print("该商品不存在")
        count = int(input("请输入购买数量："))
        order = add_to_cart(commodity_number, count)  # 调用购买函数生成购物车清单
        print("已添加到购物车。")

    elif item == "2":
        price = check_out_price(order)
        money_from_customer = float(input("总价%d元，请输入金额：" % price))
        change = check_out_change(price, money_from_customer)
        print("购买成功，找回：%d元。" % (change))
        order.clear()


#########################################################################################################
# while True:
#     item = input("1键购买，2键结算。")
#     if item == "1":
#         for key, value in commodity_info.items():
#             print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
#         while True:
#             commodity_number = int(input("请输入商品编号："))
#             if commodity_number in commodity_info:
#                 break
#             else:
#                 print("该商品不存在")
#         count = int(input("请输入购买数量："))
#         order.append({"commodity_number": commodity_number, "count": count})
#         print("添加到购物车。")
#     elif item == "2":
#         price = 0
#         for item in order:
#             shang_pin = commodity_info[item["commodity_number"]]
#             print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
#             price += shang_pin["price"] * item["count"]
#         while True:
#             money_from_customer = float(input("总价%d元，请输入金额：" % price))
#             if money_from_customer >= price:
#                 print("购买成功，找回：%d元。" % (money_from_customer - price))
#                 order.clear()
#                 break
#             else:
#                 print("金额不足.")

#
# commodity_info = {
#     101: {"name": "屠龙刀", "price": 10000},
#     102: {"name": "倚天剑", "price": 10000},
#     103: {"name": "九阴白骨爪", "price": 8000},
#     104: {"name": "九阳神功", "price": 9000},
#     105: {"name": "降龙十八掌", "price": 8000},
#     106: {"name": "乾坤大挪移", "price": 10000}
# }
#
# order = []
#
#
# def shopping():
#     """
#         购物
#     :return:
#     """
#     while True:
#         item = input("1键购买，2键结算。")
#         if item == "1":
#             for key, value in commodity_info.items():
#                 print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))
#             while True:
#                 commodity_number = int(input("请输入商品编号："))
#                 if commodity_number in commodity_info:
#                     break
#                 else:
#                     print("该商品不存在")
#             count = int(input("请输入购买数量："))
#             order.append({"commodity_number": commodity_number, "count": count})
#             print("添加到购物车。")
#         elif item == "2":
#             price = 0
#             for item in order:
#                 shang_pin = commodity_info[item["commodity_number"]]
#                 print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
#                 price += shang_pin["price"] * item["count"]
#             while True:
#                 money_from_customer = float(input("总价%d元，请输入金额：" % price))
#                 if money_from_customer >= price:
#                     print("购买成功，找回：%d元。" % (money_from_customer - price))
#                     order.clear()
#                     break
#                 else:
#                     print("金额不足.")
#
#
# shopping()
