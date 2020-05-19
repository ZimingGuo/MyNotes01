# author: Ziming Guo
# time: 2020/2/23
'''
    购物车逻辑控制器模块
'''

import commodity_model as cm


class ShoppingCartController:
    """
        购物车逻辑控制器
    """
    init_order_id = 0

    def __init__(self):
        self.__list_order = []
        self.__list_commodity_info = self.__load_commodity()

    @property
    def list_order(self):
        return self.__list_order

    @property
    def list_commodity_info(self):
        return self.__list_commodity_info

    def __load_commodity(self):
        """
            加载商品信息
        :return: 商品列表
        """
        return [
            cm.CommodityModel(101, "屠龙刀", 10000),
            cm.CommodityModel(102, "倚天剑", 10000),
            cm.CommodityModel(103, "九阴白骨爪", 8000),
            cm.CommodityModel(104, "九阳神功", 9000),
            cm.CommodityModel(105, "降龙十八掌", 8000),
        ]

    def add_order(self, order_base_info):
        """
            添加订单
        :param order:订单基础信息
        """
        order_base_info.id = self.__generate_order_id()
        self.__list_order.append(order_base_info)

    def __generate_order_id(self):
        """
            生成订单编号
        :return: 订单编号
        """
        ShoppingCartController.init_order_id += 1
        return ShoppingCartController.init_order_id

    def get_total_price(self):
        """
            根据订单计算总价格
        :return:总价格
        """
        total_price = 0
        for item in self.__list_order:
            total_price += item.commodity.price * item.count
        return total_price

    def get_commodity_by_id(self, id):
        """
            获取指定的商品
        :param id: 商品编号
        :return: 商品对象
        """
        for item in self.__list_commodity_info:
            if item.id == id:
                return item
