# author: Ziming Guo
# time: 2020/2/6
'''
# 练习10:
在控制台中获取一个字符串
打印第一个字符
打印最后一个字符
打印倒数第三个字符
打印前两个字符
倒序打印字符
如果字符串长度是奇数，则打印中间字符.
'''
str01 = input("请输入一段字符：")

# 打印第一个字符
print(str01[0])

# 打印最后一个字符
print(str01[-1])

# 打印倒数第三个字符
print(str01[-3])

# 打印前两个字符
print(str01[0:2])

# 倒序打印字符
print(str01[::-1])

# 如果字符串长度是奇数，则打印中间字符
count01 = 0
for item in str01:
    count01 += 1

if count01 % 2 == 1:
    count02 = int((count01 - 1) / 2)
    print(str01[count02])
else:
    print("字符串长度是偶数！")

# 老师的方法：
if len(str01) % 2 == 1:
    print(str01[len(str01) // 2])
# len 函数的作用就是求字符串的长度

# 总结：
#       len 函数用来求字符串的长度，输出的是一个数字（浮点数）
