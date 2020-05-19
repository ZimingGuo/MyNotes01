# author: Ziming Guo
# time: 2020/2/26
'''
    练习7:
        从列表[4,5,566,7,8,10]中选出所有偶数
        -- 结果存入另外一个列表中
        -- 使用生成器实现
'''

# 方法1-最基础的遍历列表：
list01 = [4, 5, 566, 7, 8, 10]
list02 = []
for item in list01:
    if item % 2 == 0:
        list02.append(item)
print(list02)


# 方法2-今天讲的迭代器和生成器：
def my_even_list(list_target):
    for object in list_target:
        if object % 2 == 0:
            yield object


for thing in my_even_list(list01):
    print(thing)
