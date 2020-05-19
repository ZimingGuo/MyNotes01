# author: Ziming Guo
# time: 2020/2/2
'''
练习4：
古代的秤：1斤 = 16两
获取输入的两数
输出是几斤零几两
'''
weight_liang = float(input("请输入两数："))

jin = weight_liang // 16
rest_weight_liang = weight_liang % 16

# print("最终的斤数为：" + str(jin))
# print("最终的两数为：" + str(rest_weight_liang))

print("最终的重量为："+str(jin)+"斤零"+str(rest_weight_liang)+"两")


