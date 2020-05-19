# author: Ziming Guo
# time: 2020/2/3

a = "悟空"
b = a
c = a
# 删除变量a,b，但不释放对象"悟空"
del a
# 由于变量c不再引用变量"悟空"，而"悟空"的引用计数为0，所以被标记为可 回收
c = None