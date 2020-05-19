# author: Ziming Guo
# time: 2020/2/3
'''
作业4
加速度：
已知加速度，初速度，时间
计算：距离
公式为：加速度 = （ 距离 - 初速度 * 时间 ）* 2 / 时间的平方
'''
accelerated_volicity = int(input("请输入加速度："))
time = int(input("请输入时间："))
initial_volicity = int(input("请输入初速度："))

distance = accelerated_volicity * (time ** 2) /2 + initial_volicity * time
print("计算出的距离为："+str(distance))
