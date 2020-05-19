# author: Ziming Guo
# time: 2020/2/23
"""
    时间处理
    练习：exercise02.py
         exercise02.py
"""
import time

# 这导进来的是个模块，模块里面有很多方法
# 下面就开始调用这些方法实现不同的功能

# 1. 获取当前时间戳(从1970年1月1日到现在经过的秒数)
# 1560998261.108855
print(time.time())

# 2. 时间元组(年，月，日，时，分，秒，一周的第几天，一年的第几天，夏令时)
# 他其实是个类，只不过支持元组的操作方式
# 时间戳 --> 时间元组
m = time.localtime(1560998261)
print(m)
# 通过元组的操作获取时间
tuple_time = time.localtime()  # 获取此时的时间元组
for item in tuple_time:
    print(item)
print(tuple_time[1])  # 获取月

# 通过类的操作获取时间
# 通过类来操作比较麻烦
print(type(tuple_time)) # 打印结果说明这个所谓的元组是个类
# print(time.struct_time)
print(tuple_time.tm_year)  # 获取年

#  时间元组 --> 时间戳
print(time.mktime(tuple_time))

# 3. 时间元组 -->  str
str_time01 = time.strftime("%Y / %m / %d %H:%M:%S", tuple_time)
# 一般是用 / 来分隔的，也可以用别的来分隔（格式是固定的 Y m d H M S ）
print(str_time01)

# str  -->  时间元组
print(time.strptime(str_time01, "%Y / %m / %d %H:%M:%S"))
# time.strptime 方法里前面是要转换的字符串，后面是字符串的格式，返回的结果就是时间元组的形式
