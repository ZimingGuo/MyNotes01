# author: Ziming Guo
# time: 2020/2/11
'''
    作业4：
    定义函数，计算指定范围内的素数
'''


def prime_number_range(start_number, end_number):
    prime_list = []
    # 生成范围内的整数
    for number in range(start_number, end_number):
        # 判断是否为素数
        if number == 1:
            continue
        for i in range(2, number):
            if number % i == 0:
                break  # 如发现满足条件的数字，就不再判断后面，break 跳出的是整个 for 循环，包括else
        else:  # 表示：如果上面的条件都做完了还不满足 if 语句，就执行 else 的语句
            prime_list.append(number)
    return prime_list


a = prime_number_range(100, 1000)
print(a)


# 很实用的一个函数：挑选指定范围内的素数

####################################################################################

# 老师：其实上面的代码做了两件事，生成整数 & 判断素数
#      所以函数的质量不是很高，正常应该做一件事

# 定义一个 判断指定数字是否为素数 的函数
def is_prime(number):
    """
    判断指定数字是否为素数
    :param number: 指定的整数
    :return: True是素数 ；False不是素数
    """
    for i in range(2, number):
        if number == 1:
            return False
        if number % i == 0:
            return False  # 如发现满足条件的数字，就不再判断后面，break 跳出的是整个 for 循环，包括else
    return True  # 因为之前有return了，所以不用再写 else 了


def prime_number_range(start_number, end_number):
    """
    获取范围内的素数
    :param start_number: 开始值（包含）
    :param end_number: 结束值（包含）
    :return: 所有素数
    """
    prime_list = []
    for number in range(start_number, end_number):
        if is_prime(number):
            prime_list.append(number)
    return prime_list


print(prime_number_range(100, 1000))


####################################################################################

def is_prime_02(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_number_range_02(start_number, end_number):
    prime_list = []
    # 生成范围内的整数
    for number in range(start_number, end_number):
        # 判断是否为素数
        if is_prime_02(number) is True:
            prime_list.append(number)
    return prime_list


a = prime_number_range_02(100, 1000)
print(a)
