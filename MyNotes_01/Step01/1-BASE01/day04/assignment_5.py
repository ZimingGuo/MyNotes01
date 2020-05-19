# author: Ziming Guo
# time: 2020/2/6
'''
作业5：
    在控制台中录入一个字符串，判断是否为回文．
      判断规则:正向与反向相同．
      　　　上海自来水来自海上
    # 这是一道经典的面试题，只不过在 python 里面执行特别简单
'''
text = input("请输入一段字符：")
length = len(text)
count = 0
# 奇数情况：
if length % 2 == 1:
    check_time = int((length - 1) / 2)
    for word in range(0, check_time):
        if text[word] == text[length - word - 1]:
            count += 1
            if count == check_time:
                print("这是回文")
                break
        else:
            print("不是回文")
            break
# 偶数情况：
else:
    check_time = int(length / 2)
    for word in range(0, check_time):
        if text[word] == text[length - word - 1]:
            count += 1
            if count == check_time:
                print("这是回文")
                break
        else:
            print("不是回文")
            break


# 老师的方法：
#   超级简单，我真是，咋办啊啊啊啊啊
# 思想：把这一串字符倒过来，和原字符进行比较，一样就是回文，不一样就不是

message=input("输入一串字符：")
if message==message[::-1]:
    print("是回文")
else:
    print("不是回文")

# 经验：
# 不一定非要前后逐字判断，只要是对称就可以

