# author: Ziming Guo
# time: 2020/2/4
'''
练习1：
在控制台中录入一个商品单价。
再录入这个商品的数量。
最后获取金额，并计算应该找回多少零钱。
当钱不够的时候，提示金额不足
'''
unit_cost = float(input("请输入商品单价："))
number = float(input("请输入商品购买数量："))
money = float(input("请输入您支付的金额："))

change = money - number * unit_cost

if change > 0:
    print("找您的零钱数额为"+str(change)+"元")
elif change==0:
    print("钱正好，你可以走了哈")
else:
    debt=0-change
    print("金额不足，还应补"+str(debt)+"元")