# author: Ziming Guo
# time: 2020/2/2
'''
练习5：
在控制台中获取：距离，时间，初速度
最终要获取：加速度
公式为：加速度 = （ 距离 - 初速度 * 时间 ）* 2 / 时间的平方
'''

distance = float(input("请输入距离："))
time = float(input("请输入时间(单位为小时)："))
initial_speed = float(input("请输入初速度："))

accelerate_velocity = (distance - initial_speed * time) * 2 / time ** 2

print("最终的加速度为："+str(accelerate_velocity))

