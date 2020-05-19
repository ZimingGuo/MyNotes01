# author: Ziming Guo
# time: 2020/2/24
'''
    main
'''
import sys
import skill_system.skill_deployer as sd

s01 = sd.Three()

s01.class_fun03()
s01.statistic_fun03()
sd.fun03()

print(sys.path)

# 按理来说应该最后打印 fun03 那一系列
