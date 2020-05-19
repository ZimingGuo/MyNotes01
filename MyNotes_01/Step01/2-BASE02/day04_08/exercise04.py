# author: Ziming Guo
# time: 2020/2/10
'''
    练习4：
    定义 判断列表中是否存在相同元素 的函数
    之前练习：
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路：所有元素俩俩比较,发现相同的则打印结果
    　　　所有元素比较结束，都没有发现相同项，则打印结果.
'''


# # 定义函数
# def same_or_not(list_target):
#     for m in range(len(list_target) - 1):
#         for i in range(m + 1, len(list_target)):
#             if list_target[m] == list_target[i]:
#                 return "具有相同项" # 如果有相同项，就直接跳出方法了
#                                   # 不需要后面的一系列 break 跳出 for 循环
#                                   # 因为 break 只能跳出一层循环
#     return "没有相同项"
# #   有了return能够直接跳出两个循环，逻辑和结构更加清晰了
# #   return 可以大大减少嵌套层级

# 调用函数
# list_01 = [3, 80, 45, 5, 80, 3, 1]
# print("最终的结果是：%s" % (same_or_not(list_01)))

def same_or_not(list_target):
    for m in range(len(list_target) - 1):
        for i in range(m + 1, len(list_target)):
            if list_target[m] == list_target[i]:
                return True       # 如果有相同项，就直接跳出方法了
                                  # 不需要后面的一系列 break 跳出 for 循环
                                  # 因为 break 只能跳出一层循环
    return False
# 再编程中不应该用字符串来代表状态，而应该用 bool 类型（True & False）
# 多种状态应该用 0 1 2 3 ...

list_01 = [6, 81, 45, 5, 80, 3, 1]
print("最终的结果是：%s" % (same_or_not(list_01)))