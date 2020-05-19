# author: Ziming Guo
# time: 2020/2/10
'''
    demo05：
        列表推导式的嵌套
            两层循环可以嵌套，列表推导式也可以嵌套
            推导式这个东西就是基于 for 循环的 我认为
'''
list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
list03 = []
for r in list01:
    for c in list02:
        list03.append(r + c)

print(list03)

list04 = [r + c for r in list01 for c in list02]
print(list04)

# 练习:列表的全排列
# [“香蕉”,"苹果","哈密瓜"]
# [“可乐”,"牛奶"]

list05 = ["香蕉", "苹果", "哈密瓜"]
list06 = ["可乐", "牛奶"]
list07 = []
for m in list05:
    for n in list06:
        list07.append(m + n)
print(list07)

list08 = [m + n for m in list05 for n in list06]
print(list08)

# 列表推导式的嵌套：
# 新的列表里面 先拿外层循环 再拿内层循环
