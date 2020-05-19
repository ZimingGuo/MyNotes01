# author: Ziming Guo
# time: 2020/2/7
'''
练习5：
在列表中删除大于10的数字
列表：[9,25,12,8]
'''

# 这只是我的一种删除方式：
list01 = [9, 25, 12, 8]
count = 0
for i in range(0, 4):
    if list01[count] > 10:
        list01.remove(list01[count])
        count -= 1
    count += 1
print(list01)

# 老师推荐的删除方式是从后往前删除：
#   用所银的方式从后往前删除，尽量不用切片的形式，因为重新建立列表划不来
#   倒着来
list01 = [9, 25, 12, 8]
for i in range(3, -1, -1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)
