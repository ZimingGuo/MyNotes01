# author: Ziming Guo
# time: 2020/2/10
'''
    练习10：
        定义在控制台中打印一维列表的函数.
        例如：[1,2,3]-->1 2 3  每个元素一行
'''
def list_print(list01):
    """
    输入一个列表，把里面的元素逐行打印出来，一行一个元素
    :param list01: 想要打印的列表
    :return:
    """
    for item in list01:
        print(item)

list_print(["w","e","r","t","u","u"])