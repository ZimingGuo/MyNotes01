# author: Ziming Guo
# time: 2020/2/11
'''
    练习8：
        记录一个函数 fun01 的执行次数 & 画出内存图
    想办法，也许可以用到 global
'''
count = 0

def fun01():
    global count
    count += 1
    pass


fun01()
fun01()
fun01()
fun01()

print(count)
