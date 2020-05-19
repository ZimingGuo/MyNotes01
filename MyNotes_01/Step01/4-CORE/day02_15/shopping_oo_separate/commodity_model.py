# author: Ziming Guo
# time: 2020/2/23
'''
    商品模型模块
'''
class CommodityModel:
    """
        商品模型
    """

    def __init__(self, id=0, name="", price=0):
        self.id = id
        self.name = name
        self.price = price
