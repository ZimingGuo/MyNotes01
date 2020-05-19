# author: Ziming Guo
# time: 2020/2/24
'''
    skill_manager
'''


class Four:

    def class_fun04(self):
        print("this is class_fun04 in skill_deployer")

    @staticmethod
    def statistic_fun04():
        print("this is statistic_fun04")


def fun04():
    print("this is fun04 in skill_manager")


from common_my.double_list_helper import *

dlh = One()
dlh.class_fun01()
dlh.statistic_fun01()
fun01()
