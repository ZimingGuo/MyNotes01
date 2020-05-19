# author: Ziming Guo
# time: 2020/3/30
'''
    demo 进程池事例
'''

from multiprocessing import Pool
from time import sleep, ctime


# 写一个事件函数（进程池事件）
# 进程池的这个事件函数要写在创建进程池之前，池子一旦创建，进程就已经存在了
def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)


# 创建进程池
pool = Pool()  # 默认数量的进程

# 向进程池队列添加事件
for i in range(10):
    msg = "Haha %d" % i
    pool.apply_async(func=worker, args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()

# 注：
# 进程之间不按照顺序是很正常的，谁先执行完，谁后执行完，我们也不知道，计算机说了算
