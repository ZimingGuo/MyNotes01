# author: Ziming Guo
# time: 2020/2/10
'''
    练习2：
        古代的秤：1斤 = 16两
        获取输入的两数
        输出是几斤零几两

        练习：定义根据两，计算几斤零几两的函数
'''

# 定义函数
def exchange_liang_to_jin(weight_liang):
    """
    根据两，计算几斤零几两的函数
    :param weight_liang: 两的值
    :return: 元组（斤 和 两）
    """
    jin = weight_liang // 16
    rest_weight_liang = weight_liang % 16
    return (jin, rest_weight_liang)
    # 其实返回的是个元组，而不是多个变量，只是 python 里面支持这样写
    # 所以建议还是要加上括号，因为是一个东西
    # 虽然我想返回的是多个结果，但是实际上我返回的是一个元组


# 调用函数
jin, liang = exchange_liang_to_jin(200)
print("最终的重量为：" + str(jin) + "斤零" + str(liang) + "两")

#   后者也可以堪称返回的是一个结果
result = exchange_liang_to_jin(30)
print("最终的重量为：" + str(result[0]) + "斤零" + str(result[1]) + "两")
