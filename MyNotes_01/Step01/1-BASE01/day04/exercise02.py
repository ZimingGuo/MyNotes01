# author: Ziming Guo
# time: 2020/2/5
'''
练习2：
一张纸的厚度是0.1毫米
请计算对着多少次，会超过珠穆朗玛峰的8844.43米
'''
# 对折一次 0.01*2 = 001*2**1
# 对折两次 0.01*2*2 = 001*2**2
# ...
# 对折n次 001*2**n

# 转换成米：
fold_times = 0
height_m = 0.01 * 0.001

while height_m < 8844.43:
    fold_times += 1
    height_m = height_m * 2

print(fold_times)
