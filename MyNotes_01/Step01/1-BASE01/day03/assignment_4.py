# author: Ziming Guo
# time: 2020/2/4
'''
作业4：
在控制台获取年龄：
如果小于0岁，打印输入有误
小于2岁，打印是个婴儿
2-13岁，打印是个儿童
13-20岁，打印是个青少年
20-65岁，打印是个成年人
65-150岁，打印是个老年人
150岁以上，打印是不可能的
'''
age = int(input("请输入年龄："))
if age < 0:
    print("输入年龄有误！")
elif age > 150:
    print("impossible！")
elif age < 2:
    print("婴儿")
elif age < 13:
    print("儿童")
elif age < 20:
    print("青少年")
elif age < 65:
    print("成年人")
else:
    print("老年人")

# 体会一下elif的用法：排斥性
