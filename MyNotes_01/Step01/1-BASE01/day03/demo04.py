# author: Ziming Guo
# time: 2020/2/4
'''
选择语句
'''
sex=input("请输入性别：")
if sex == "男":
    print("您好先生！")
elif sex == "女":
    print("您好女士！")
else:
    print("性别未知")

print("后续逻辑")

# 调试：让程序中断，逐条语句执行
# 调试的目的：
# 1 审查运行时变量的取值
# 2 审查程序运行流程

# 步骤：
# 1 加断点：中断的地点
# 2 调试运行：点击 Debug
# 3 步过：再执行一行，看哪里蓝色，程序在执行哪个语句
#        调试是一种排错的手段
# 4 停止：红色小方块

# 练习：当钱不够的时候，提示金额不足
#      钱够的时候，显示应该找回
#      加断点初 ：在可能出错的行
#