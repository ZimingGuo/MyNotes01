# author: Ziming Guo
# time: 2020/3/31
'''
    demo_dead_lock:
'''

from time import sleep
from threading import Thread, Lock


# 交易类
class Account():
    def __init__(self, _id, balance, lock):  # 第三个参数的意思就是要初始化一个锁对象，方便之后上锁
        # 创建了一个对象，就实例化了一个用户
        self.id = _id  # 用户
        self.balance = balance  # 存款
        self.lock = lock  # 锁

    # 存钱
    def withdraw(self, amount):
        self.balance -= amount

    # 取钱
    def deposit(self, amount):
        self.balance += amount

    # 查看余额
    def get_balance(self):
        return self.balance


# 产生了两个账户
# 每个人都有自己的锁
Tom = Account('Tom', 5000, Lock())
Alex = Account('Alex', 8000, Lock())


# 模拟一个转账的过程
def transfer(from_, to, amount):
    if from_.lock.acquire():  # 先让这个拿出钱的人上锁
        from_.withdraw(amount)  # 上锁之后，再让这个拿出钱的人，的账户的钱减少
        sleep(0.5)
        if to.lock.acquire():  # 然后在锁住对方的账户，也就是收钱的人的账户
            to.deposit(amount)  # 锁住对方的账户之后，就给对方的这个账户加钱
            to.lock.release()  # 然后再给这个账户解锁
        from_.lock.release()  # 拿钱的这个账户解锁
    print("%s 给 %s 转账 %d" % (from_.id, to.id, amount))


# 单独的以此转账
transfer(Tom, Alex, 4000)

t1 = Thread(target=transfer, args=(Tom, Alex, 2000))
t2 = Thread(target=transfer, args=(Alex, Tom, 3500))

# 一个特殊情况：Tom 正在给 Alex 转钱，与此同时，Alex 也在给 Tom 转钱
# 此时就会产生死锁
t1.start()
t2.start()
t1.join()
t2.join()
