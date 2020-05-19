# author: Ziming Guo
# time: 2020/4/6
'''
    demo01:
    async
'''

import asyncio


# 定义协程函数
async def fun01():
    print("start 1")
    # 用来设置跳转的阻塞点
    await asyncio.sleep(2)
    print("end 1")


async def fun02():
    print("start 2")
    await asyncio.sleep(3)
    print("end 2")


# 即：把上面的两个函数都定义成协程函数，哪个能执行就执行哪个
#   当遇到阻塞的时候，就可以自动跳转
#   也就是说：先执行 fun01，然后当遇到阻塞 await 的时候就跳转执行 fun02
#   然后当 fun01 的两秒等待结束之后，再执行 fun01 的最后一句，然后再跳到 fun02 执行 fun02 的最后一句


# 生成协程对象
cor1 = fun01()
cor2 = fun02()

tasks = [asyncio.ensure_future(cor1),
         asyncio.ensure_future(cor2)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
