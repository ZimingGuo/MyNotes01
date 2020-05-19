# author: Ziming Guo
# time: 2020/2/5
'''
练习9：
'''
# 练习1:在控制台中，获取一个字符串，打印每个字符的编码值
str01 = input("请输入一串字符：")
for item in str01:
    print(ord(item))

# 练习2:在控制台中，重复录入一个编码值，然后打印字符.
#      如果输入空字符串，则退出程序.

code = input("请输入一个编码值：")
while True:
    if code == "":
        break
    elif code != "":
        print(chr(int(code)))  # chr 函数应该一般情况下和 int 一起使用
                               # 因为是从数字转换成字符
        code = input("请输入一个编码值：")

