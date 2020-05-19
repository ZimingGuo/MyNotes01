# author: Ziming Guo
# time: 2020/2/24
'''
    list_helper
'''


class Two:

    def class_fun02(self):
        print("this is class_fun02 in list_helper")

    @staticmethod
    def statistic_fun02():
        print("this is statistic_fun02")


def fun02():
    print("this is fun02 in list_helper")


import main as mpm

print("common_my -- list_helper")

import sys

# 如果不再pycharm中运行当前模块，则导包失败.
# 将项目根目录加入path中，导包才会成功.
sys.path.append("/home/tarena/1905/month01/code/day15/my_project")
print(sys.path)

# from main import *
