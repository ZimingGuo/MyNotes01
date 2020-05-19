# author: Ziming Guo
# time: 2020/2/3
'''
身份运算符
'''

a = 800
b = 1000
# id 函数，可以获取变量存储的对象的地址（id 拿到的是800和100的内存地址）
print(id(a))
print(id(b))
# False
print(a is b) # is 的本质就是通过 id 函数进行判断的

c = a
print(id(c))
print(c is a)

d = 1000
print(d is b) # 上文说 b = 1000，这句话所以运行之后是 True
# 这种判断方式只适用于文件式编写，交互式不可以，因为文件式进行了优化

# 下面这段代码在终端运行时结果如下：
b = 1000
d = 1000
print(b is d) # 结果是 False

e = 1
f = 1
print(e is f) # 结果是 True


