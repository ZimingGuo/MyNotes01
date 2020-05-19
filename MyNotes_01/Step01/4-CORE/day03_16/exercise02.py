# author: Ziming Guo
# time: 2020/2/25
'''
    练习2:
        不使用for，获取字典所有数据。
     {"铁扇公主":101,"铁锤公主":102,“扳手王子”:103}
'''

dict = {"铁扇公主": 101, "铁锤公主": 102, "扳手王子": 103}

key = dict.keys().__iter__()
value = dict.values().__iter__()
while True:
    try:
        print(key.__next__())
        print(value.__next__())
    except:
        print("没了，别取了")
        break

# 老师的另一种方法：
iterator = dict.__iter__()
while True:
    try:
        key01 = iterator.__next__()
        print(key01, dict[key01])
    except:
        print("没了，别取了")
        break
