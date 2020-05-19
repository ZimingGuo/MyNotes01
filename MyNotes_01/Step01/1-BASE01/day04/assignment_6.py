# author: Ziming Guo
# time: 2020/2/6
'''
作业6：
    (扩展)一个小球从 100m 的高度落下
        　　每次弹回原高度的一半．
        　　计算：总共弹起来多少次（最小弹起高度0.01ｍ）．
                总共走了多少米
'''
count = 0
height = 100
distance = 100
while True:
    height /= 2
    distance += height * 2 # 累加起 & 落的高度
    count += 1
    if height / 2 < 0.01: # 这个地方 height 必须要 / 2
                          # 因为当高度小于 0。01 的时候就不能弹起了
        break

print("此时高度为%.3f" % (height))
print("一共弹起%d次" % (count))
print("一共走了%.3f米" % (distance))
