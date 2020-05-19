# author: Ziming Guo
# time: 2020/3/30
'''
    demo_array 的演示：
    共享内存存放一组数据
'''

from multiprocessing import Process, Array

# 创建共享内存
# shm = Array('i', [1, 2, 3, 4])  # 表示放入初始四个值的列表
# shm = Array('i', 5) # 表示初始开辟了一个包含五个整型空间的列表
shm = Array('c', b'hello')  # 表示初始值是一个字节串，c 代表类型是字符，但是后面加上的必须是个字节串


def fun01():
    # array 创建的共享内存对象是可迭代的
    for i in shm:
        print(i)
    shm[0] = b'H'  # 在子进程中修改共享内存


p = Process(target=fun01)
p.start()
p.join()

# 在父进程中遍历修改后的共享内存，并遍历
# 父进程中也会获取到修改后的共享内存的内容 (因为共享内存的这块区域只有一块，虽然父子进程是独立的)
for i in shm:
    print(i)

print(shm.value)  # 表示整体的打印字节串，只能打印字节串，不能打印整型的列表啥的

