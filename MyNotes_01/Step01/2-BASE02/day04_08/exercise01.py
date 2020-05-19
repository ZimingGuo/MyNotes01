# author: Ziming Guo
# time: 2020/2/10
'''
    练习1：
    函数练习：定义计算四位整数，每位相加和的函数
    自己找数字测试
'''


# 语法上：做函数，用函数，参数，返回值
# 原理：累加


# 定义函数 (逻辑计算)
def add_four_digit_number(four_digit_number):
    """
    计算一个四位整数的各位相加和
    :param four_digit_number: 四位整数
    :return: 相加结果
    """
    # 个位：
    each_digit_sum = four_digit_number % 10
    # 加上十位：
    each_digit_sum += four_digit_number // 10 % 10
    # 加上百位：
    each_digit_sum += four_digit_number // 100 % 10
    # 加上千位：
    each_digit_sum += four_digit_number // 1000
    return each_digit_sum


# 开始调用12
result = add_four_digit_number(1234)
print("四位数的各位和为：" + str(result))

result = add_four_digit_number(5678)
print("四位数的各位和为：" + str(result))
