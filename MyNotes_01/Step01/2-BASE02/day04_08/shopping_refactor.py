
# 重构

dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def select_menu():
    """
        选择菜单
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def settlement():
    """
    结算
    :return:
    """
    print_orders()
    total_price = calculate_total_price()

    paying(total_price)


def paying(total_price):
    """
    支付
    :param total_price: 需要支付的价格
    :return:
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money >= total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            list_order.clear()
            break
        else:
            print("金额不足.")


def calculate_total_price():
    """
    计算总价
    :return:
    """
    total_price = 0
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        total_price += commodity["price"] * order["count"]
    return total_price

def print_orders():
    """
    打印订单
    :return:
    """
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], order["count"]))


def buying():
    """
    购买
    :return:
    """
    print_commodity_info()

    creat_order()

    print("添加到购物车。")


def creat_order():
    """
    创建订单
    :return:
    """
    cid = input_commodity_id()
    count = int(input("请输入购买数量："))
    order = {"cid": cid, "count": count}
    list_order.append(order)


def input_commodity_id():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    return cid


def print_commodity_info():
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


select_menu()

# 想做一个函数就应该从上到下行云流水写完，然后在里面提取每个部分
#   用快捷键生成函数，然后再微调

# 合格的函数代码不能超过 10 行，这是最大的上限了
#   因为函数只能做一件事，多了就不简洁了，别人看了不舒服