# author: Ziming Guo
# time: 2020/2/23
'''
    订单模型
'''
class OrderModel:
    """
        订单模型
    """

    def __init__(self, commodity=None, count=0, id=0):
        self.id = id
        self.commodity = commodity
        self.count = count