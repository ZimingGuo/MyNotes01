# author: Ziming Guo
# time: 2020/2/23
'''
    购物车控制台界面视图模块
'''

import order_model as om
import shopping_cart_controller as scc


class ShoppingConsoleView:
    """
        购物车控制台界面视图
    """

    def __init__(self):
        self.__controller = scc.ShoppingCartController()

    def __select_menu(self):
        """
            菜单选择　
        """
        while True:
            item = input("1键购买，2键结算。")
            if item == "1":
                self.__buying()
            elif item == "2":
                self.__settlement()

    def __buying(self):
        """
            购买
        """
        self.__print_commodity()
        self.__create_order()
        print("添加到购物车。")

    def __print_commodity(self):
        """
            打印商品信息
        """
        for commodity in self.__controller.list_commodity_info:
            print("编号：%d，名称：%s，单价：%d。" % (commodity.id, commodity.name, commodity.price))

    def __create_order(self):
        """
            创建订单
        """
        while True:
            cid = int(input("请输入商品编号："))
            # 如果该商品存在，则退出循环，否则重新输入。
            commodity = self.__controller.get_commodity_by_id(cid)
            if commodity:
                break
            else:
                print("该商品不存在")
        count = int(input("请输入购买数量："))
        order = om.OrderModel(commodity, count)
        self.__controller.add_order(order)

    def __settlement(self):
        """
            结算
        """
        self.__print_order()
        total_price = self.__controller.get_total_price()
        self.__pay(total_price)

    def __print_order(self):
        """
            打印订单
        """
        for order in self.__controller.list_order:
            commodity = order.commodity
            print("商品：%s，单价：%d,数量:%d." % (commodity.name, commodity.price, order.count))

    def __pay(self, total_price):
        """
            支付
        :param total_price: 需要支付的价格
        :return:
        """
        while True:
            money = float(input("总价%d元，请输入金额：" % total_price))
            if money >= total_price:
                print("购买成功，找回：%d元。" % (money - total_price))
                self.__controller.list_order.clear()
                break
            else:
                print("金额不足.")

    def main(self):
        """
            界面入口
        """
        while True:
            self.__select_menu()
