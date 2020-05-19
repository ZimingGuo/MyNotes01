# author: Ziming Guo
# time: 2020/2/2
'''
练习6：
在控制台中录入一个四位数
计算每一位相加和
显示结果
'''
four_digit_number = int(input("请输入一个四位数字："))

'''我的方法：'''
# thousand = four_digit_number // 1000
# hundred = (four_digit_number - thousand * 1000) // 100
# ten = (four_digit_number - thousand * 1000 - hundred * 100) // 10
# unit = four_digit_number % 10
# each_digit_sum = thousand + hundred + ten + unit

'''老师的方法1：用算数运算符'''
# 原理：分别计算再相加
# unit=four_digit_number%10
# ten=four_digit_number//10%10
# hundred=four_digit_number//100%10
# thousand=four_digit_number//1000
# each_digit_sum = thousand + hundred + ten + unit

'''老师的方法2：用增强运算符'''
# 原理：累加
# 个位：
each_digit_sum=four_digit_number%10
# 加上十位：
each_digit_sum+=four_digit_number//10%10
# 加上百位：
each_digit_sum+=four_digit_number//100%10
# 加上千位：
each_digit_sum+=four_digit_number//1000

print("四位数的各位和为：" +str(each_digit_sum))

# 练习：
# 分别画出 老师方法1 & 老师方法2 的内存图
# 看哪个内存图干净。就说明哪个方法性能高




