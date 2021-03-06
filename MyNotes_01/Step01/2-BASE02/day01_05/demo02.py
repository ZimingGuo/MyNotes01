# author: Ziming Guo
# time: 2020/2/7
'''
    demo02
    列表内存图
'''

list01 = ["张无忌", "赵敏"]
list02 = list01
list01[0] = "无忌"  # 这句话修改的事列表的第一个元素
# 就是说列表第一个元素的位置指向了一个新的对象"无忌"
# 而不是直接改变了原来的对象"张无忌"
print(list02[0])

list01 = ["张无忌", "赵敏"]
list02 = list01
list01 = ["无忌"]  # 现在相当于又新建了一个列表
# 然后list01这块内存(这个变量)又重新指向了这个新的列表的地址
# 不会继续指向原来的列表
print(list02[0])  # 但是此时的list02还是原来的list01
# 因为list02这个变量所指向的地址没有变

# 画内存图练习1：
list01 = [800, 1000]
list02 = list01[:]  # 注意注意！这是一个切片操作 - 这种切片操作的意思是全都取出来
# 通过切片获取元素，会生成新的列表
# 说的是list01的列表本身 赋给了list02
# 说白了就是再创建一个新的列表 copy 一下，copy的只是列表本身
# 拷贝的只是里面的元素，而不是元素所指向的数据(800，1000)
# 拷贝之后里面的东西要重新指向原来的那两个对象
list01[0] = 900
print(list02[0])  # 800 因为变化的是原来的list01而不是之后的list02
list01 = [500]
print(list02[0])  # 800

# 画内存图练习2：好题
list01 = [800, [1000, 500]]
list02 = list01  # 两个变量指向的是同一个列表
list01[1][0] = 900
print(list02[1][0])  # 900

# 画内存图练习3：浅拷贝
list01 = [800, [1000, 500]]
list02 = list01[:]  # 这道题体现了，切片的时候只是复制列表本身，不会复制元素所指向的对象
# 只会复制一层 ！！！
# 新列表里面的元素会指向原来的对象，而不是复制一个新对象指向新对象
list02 = list01.copy()  # 这叫做浅拷贝，和上面那句切片的语句一样的
list01[1][0] = 900
print(list02[1][0])  # 900

# 深拷贝代码：
import copy
list01 = [800, [1000, 500]]
# 深拷贝：
list02 = copy.deepcopy(list01)  # 这两行代码就能执行深拷贝了
list01[1][0] = 900
print(list02[1][0])
