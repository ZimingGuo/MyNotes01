# author: Ziming Guo
# time: 2020/2/2
'''
练习2：
在控制台中录入一个商品单价。
再录入这个商品的数量。
最后获取金额，并计算应该找回多少零钱。
'''
unit_cost = input("请输入商品单价：")
number = input("请输入商品购买数量：")
amount = input("请输入您支付的金额：")

change = float(amount) - float(number) * float(unit_cost)
print("找您的零钱数额为："+str(change))
