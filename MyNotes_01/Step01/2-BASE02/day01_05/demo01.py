# author: Ziming Guo
# time: 2020/2/6
"""
    demo01
    列表
    练习:exercise02.py
        exercise02.py
        exercise03.py
"""
# 1. 创建列表
# 空
list01 = []
list01 = list()

# 默认值
list02 = ["悟空", 100, True]  # 根据数据来创建列表
# 也就是说里面可以有多种类型
list02 = list("我是齐天大圣")  # 根据另外一个容器来创建列表
# 里面只能有一种容器类型(字符串 or 列表 or ...)
# 上面这种写法的好处就是：把一个字符串变成了一个列表形式，
# 这样就可以直接改里面的内容了，因为列表序列可变

# 2. 获取元素
# 索引
print(list02[2])  # 齐（拿第三个元素）
# 切片
print(list02[-4:])  # ['齐', '天', '大', '圣']（拿后四个元素）
# 这个结果说明，列表里的每个元素在里面是分开的

# 3. 添加元素
# 追加(在末尾添加)
list02.append("八戒")
print(list02)
# 插入(在指定位置添加)
list02.insert(1, True)  # 在索引为１(第二个)的位置添加True
print(list02)

# 4. 删除元素
# 根据元素删除
list02.remove("是")
# 根据位置删除

del list02[0]  # 也可以根据切片来修改里面的元素
print(list02)

# 5 定位元素，目的是可以：增删改查
# （1）切片
del list02[1:3]  # 删除指定的一段元素
print(list02)  # [True, '大', '圣', '八戒']

list02[1:3] = ["a", "b"]  # 替换指定的一段元素
print(list02)  # [True, 'a', 'b', '八戒']

list02[1:3] = [1, 2, 3, 4, 5, 6]  # 替换指定的一段元素
print(list02)  # [True, 1, 2, 3, 4, 5, 6, '八戒']

list02[1:3] = []  # 把指定的一段字符串变成空的，其实就是删除一段元素
print(list02)  # [True, 3, 4, 5, 6, '八戒']

# 遍历列表：一个一个把元素拿出来
# 获取列表中的所有元素
for item in list02:
    print(item)

# 倒序获取所有元素
# 不建议这句话（这句话用的是切片，不太好）
# 因为 list02[::-1] 创建了一个新的列表
# 只要通过切片往外拿东西了，就会生成一个新的列表，划不来
for item in list02[::-1]:
    print(item)

# 建议
for i in range(len(list02) - 1, -1, -1):  # 这句话就会生成一段从3到-1，不包括-1，以-1为步长的数列
    # 3 2 1 0
    print(list02[i])

# 或者
for i in range(-1, -len(list02) - 1, -1):
    # -1
    print(list02[i])

# 总结：在 range 中步长为 -1 就表示倒序
# 倒序的范围应该是列表内想要倒序的范围
