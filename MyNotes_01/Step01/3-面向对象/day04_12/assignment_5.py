# author: Ziming Guo
# time: 2020/2/18
'''
    (扩展)将面向过程的购物车，改为面向对象的购物车.
'''


class CommodityModel:
    """
        获取数据，把数据放在一列表里
    """

    def __init__(self, name=0, price=0, id=0, number=0):
        self.__name = name
        self.__price = price
        self.__id = id
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id

    @property
    def number(self):
        return self.__number


class CommodityDataController:
    def __init__(self):  # 表示初始的时候应该建立什么东西(列表 or 字典 etc)
        self.__to_buy_list = []  # 购物车：是个大列表，里面是小列表保存名称，编号，数量 etc
        self.__commodity_list = []  # 创建一个列表：里面放的是一个个商品对象，但是对象里面不包括数量信息

    @property  # 只读
    def to_buy_list(self):
        return self.__to_buy_list

    @property  # 只读
    def commodity_list(self):
        return self.__commodity_list

    def transfer(self, dict):
        """
            转换形式
            程序给过来的是个字典，要把字典的 (键值对) 各个信息拆开来，然后创建一个对象，包括一个商品的所有信息
        :param dict: 要转换的字典 dict
        :return: 无返回值
        """
        for key, value in dict.items():
            c = CommodityModel(value["name"], value["price"], key)  # 创建了一个对象，里面包括商品信息
            self.__commodity_list.append(c)  # 把这个商品对象放进商品列表

    def add_to_cart(self, id, number):
        """
            将 number 个编号为 id 的商品放入购物车
            购物车也是个列表，购物车这个列表里面的对象除了商品的基本三个信息外还有商品的购买数量
        :param id: 想要购买的商品的编号
        :param number: 想要购买的商品的个数
        :return: 当这个商品存在于商品列表中的时候，返回 True，在 View 类中继续使用
                 当这个商品不存在于商品列表中的是时候，返回 False，在 View 类中继续使用
        """
        for item in self.commodity_list:  # 遍历商品列表里的每一个对象
            if item.id == id:
                l = CommodityModel(item.name, item.price, item.id, number)
                self.to_buy_list.append(l)
                return True
        return False

    def calculate(self):
        """
        计算总共的价格
        :return: 返回总共应该支付的钱数 int
        """
        total_price = 0
        for item in self.to_buy_list:
            price = item.price
            number = item.number
            total_price += price * number
        return total_price

    def sub(self, a, b):
        """
        实际支付值和应该支付值做差，返回找零金额
        :param a: 实际支付金额
        :param b: 应当支付金额
        :return: 找零金额
        """
        change = a - b
        return change

    def show(self, object):
        """
        显示商品信息
        :param object: 需要显示出来的对象
        :return: 无返回值
        """
        print("商品名称:", object.name, "商品价格:", object.price, "商品编号:", object.id)


class ShoppingCartView:
    def __init__(self):  # 表示初始的时候应该建立什么东西(列表 or 字典 etc)
        self.__one_commodity = CommodityModel()  # 创建了一个 Commodity 类的对象,用于以后调第一个类里面的方法
        self.__two_logic = CommodityDataController()  # 创建了一个 LogicController 类的对象,用于以后调第二个类里面的方法

    def __display(self):
        """
            commodity_list 是个列表，里面装着一个个商品对象
        :return: 无返回值
        """
        for item in self.__two_logic.commodity_list:
            self.__two_logic.show(item)

    def __calculate_01(self):
        """
            显示支付界面
        :return: 无返回值
        """
        total_price = self.__two_logic.calculate()
        while True:
            print("您应该支付:", total_price)
            money = int(input("请输入支付金额:"))
            if money < total_price:
                print("金额不足，请重新输入支付金额")
                continue  # 用 continue 是想继续进行下一个循环
            change = self.__two_logic.sub(money, total_price)
            print("支付成功！")
            print("应该找您:", change)
            break

    def __add_to_cart_01(self):
        """
            将商品加入购物车 的 显示界面
        :return:
        """
        id = int(input("请输入商品编号:"))
        number = int(input("请输入购买数量:"))
        if self.__two_logic.add_to_cart(id, number):
            print("添加成功！")
        else:
            print("商品不存在，添加失败！")

    def __select_menu(self):
        """
            开始时候的显示界面，选择功能
        :return: 无返回值
        """
        b01 = int(input("按1购买，按2结算，请输入:"))
        if b01 == 1:
            self.__add_to_cart_01()
        elif b01 == 2:
            self.__calculate_01()

    def main(self, dict):
        """
            主函数
        :param dict: 要转换的字典
        :return: 无返回值
        """
        self.__two_logic.transfer(dict)
        # 要首先把字典转换成列表包含对象的形式，然后之后才能够使用
        # 以后就是循环了，可以一直用这个转换完的列表
        # 之前的程序不行是因为：每次执行程序都会建立一个新的列表，新的列表里面，没有信息
        while True:
            self.__display()
            self.__select_menu()


# 测试代码:
dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

v01 = ShoppingCartView()
v01.main(dict_commodity_info)

# for item in c01.commodity_dict:
#     print(item.id)
#     print(item.name)
#     print(item.price)
#
# l01 = LogicController()
# l01.add_to_cart(c01.commodity_dict[1], 2)
#
# print(l01.to_buy_list)
