# author: Ziming Guo
# time: 2020/2/25
'''
    练习1：
    使用迭代器原理，遍历元组：
    ("铁扇公主","铁锤公主",“扳手王子”)
    tuple01 = ("铁扇公主","铁锤公主","扳手王子")
'''
# 这道题练的就是迭代器的原理

list01 = ("铁扇公主", "铁锤公主", "扳手王子")

iterator = list01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        print("没了，别取了")
        break
