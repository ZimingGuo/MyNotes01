# author: Ziming Guo
# time: 2020/2/24
'''
    skill_deployer
'''


class Three:

    def class_fun03(self):
        print("this is class_fun03 in skill_deployer")

    @staticmethod
    def statistic_fun03():
        print("this is statistic_fun03")


def fun03():
    print("this is fun03 in skill_deployer")


import skill_system.skill_manager as sm

s02 = sm.Four()

s02.class_fun04()
s02.statistic_fun04()
sm.fun04()
