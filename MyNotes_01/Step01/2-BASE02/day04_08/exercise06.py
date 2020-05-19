# author: Ziming Guo
# time: 2020/2/11
'''
    练习6：
    定义列表升序排列的函数
    基于day07的练习5
'''

def up_ranking(list_target):
    # 传入的是可变对象
    # 判断 函数体改变的是栈中的变量还是传入的对象 ？修改的是传入的对象
    #   因为在函数里面每次改变都加了中括号，就表明是改变的是传入的对象
    #   这类的改变还有：append & insert 等等

    for m in range(len(list_target)-1): # 取数据
        for i in range(m + 1, len(list_target)): # 做比较
            if list_target[m] > list_target[i]:  # 降序的情况就是换这个比较符号
                list_target[m], list_target[i] = list_target[i], list_target[m]

    return list_target # 其实这句话已经用不着 return 了
                       # return 的作用是告诉调用者结果，但是这个函数改的是传入对象
                       # 即使不返回值，我也能得到改变之后的结果


# 有 return 的时候通过如下方式查询结果：
list01 = [3, 80, 45, 5, 7, 1]
print(up_ranking(list01))

# 没有 return 返回值的时候通过 查看原可变对象 来查询结果
print(list01)


