# author: Ziming Guo
# time: 2020/2/9
'''
练习2:
["无忌","赵敏","周芷若"]  [101,102,103] ————> {"无忌":101,"赵敏":102,"周芷若":103}
'''
list01 = ["无忌", "赵敏", "周芷若"]
list02 = [101, 102, 103]

dict01 = {list01[i]: list02[i] for i in range(0, len(list01))}
print(dict01)
