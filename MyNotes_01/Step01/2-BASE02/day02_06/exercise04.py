# author: Ziming Guo
# time: 2020/2/8
'''
    练习4：
    在控制台中循环录入商品信息(名称,单价).
    　　　如果名称输入空字符,则停止录入.
         将所有信息逐行打印出来.
'''
dict_commodity = {}
while True:
    name = input("请输入商品的名称：")
    if name == "":
        break
    price = input("请输入商品的单价：")
    if price == "":
        break
    dict_commodity[name] = price

for n,p in dict_commodity.items():  # 这里面的n,p就是变量
    print("%s商品的价格是%s元"%(n,p))

# 在字典里面如果输入两个键相同的元素，第二个元素会覆盖第一个元素
#   即，进行修改
