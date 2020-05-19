# author: Ziming Guo
# time: 2020/2/4
'''
作业5：
根据身高 & 体重，参考BMI值，返回身体状况
BMI：体重的 kg 数除以身高米数的平方，得出的数字
参考标准：
BMI小于18.5：体重过轻
18.5<=BMI<24：正常范围
24<=BMI<28：超重
28<=BMI<30：I度肥胖
30<=BMI<40：II度肥胖
BMI>=40：III度肥胖
'''
height = float(input("请输入身高(m)："))
weight = float(input("请输入体重(kg)："))

BMI = weight / height ** 2

if BMI < 18.5:
    print("体重过轻")
elif BMI < 24:
    print("正常范围")
elif BMI < 28:
    print("超重")
elif BMI < 30:
    print("I度肥胖")
elif BMI < 40:
    print("II度肥胖")
else:
    print("III度肥胖")
