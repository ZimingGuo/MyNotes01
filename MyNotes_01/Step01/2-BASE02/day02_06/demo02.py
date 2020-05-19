# author: Ziming Guo
# time: 2020/2/8
'''
    demo02
    元组
        基础操作
'''
# 1 创建元组（空）
tuple01 = ()
tuple01 = tuple()
#   因为一个元组里面也是一个个变量，所以也可以指向任何数据类型
#   所以元组里面也能放列表，字符串，数字

#   列表可以转换成元组：
tuple01 = tuple(["a", "b"])
print(tuple01)
#   元组也可以转换成列表：
list01 = list(tuple01)
print(list01)
#   这两种形式的相互转换其实是两个存储机制之间的转换
#   由按需分配到预留空间 & 由预留空间到按需分配

#   创建元组（具有默认值）
tuple01 = (1, 2, 3)
print(tuple01)

#   如果元组里面只有一个元素，要在这个元素的后面加上逗号
tuple02 = (100)
print(tuple02)  # 此时打印出来的只是一个整形 100 int
tuple02 = (100,)
print(tuple02)  # 此时打印出来的才是元组形式
#   这是元组的一个特殊形式

#   不能增加
#   没有 append 和 insert

# 2 获取元素（索引 & 切片）
tuple03 = ("a", "b", "c", "d")
e01 = tuple03[1]  # 此处的 e01 是字符串类型
e01 = tuple03[-2:]  # 表示的是取后两个元素 # 切片出来的是元组类型

tuple04 = (100, 200)
# 可以直接将元组赋值给多个变量，但是变量的个数和元组里面的元素个数必须相等
# 其实所有容器都支持这种写法，但一般都是用元组
a, b = tuple04
print(a)  # 100 整形
print(b)  # 200 整形

# 3 遍历元素
# 正向
for item in tuple04:
    print(item)
# 反向
for i in range(-1, -len(tuple04) - 1, -1):
    print(tuple04[i])
