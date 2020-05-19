# author: Ziming Guo
# time: 2020/2/3
'''
作业5：
计算各类温度值
摄氏度 = （华氏度 - 32）/ 1.8
华氏度 = 摄氏度 * 1.8 + 32
开氏度 = 摄氏度 + 237.15
'''
celsius = float(input("请输入摄氏度："))
# fahrenheit = float(input("请输入华氏度："))
# kelvin = float(input("请输入开氏度："))

fahrenheit_degree = celsius * 1.8 + 32
kelvin_degree = celsius + 237.15
# celsius_degree = (fahrenheit - 32) / 1.8

# print("转换后的摄氏度为:"+str(celsius_degree))
print("转换后的华氏度为:"+str(fahrenheit_degree))
print("转换后的开氏度为:"+str(kelvin_degree))
