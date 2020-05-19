# author: Ziming Guo
# time: 2020/3/15
file_display = open('test.txt', 'r')
data01 = file_display.read(10)
print(data01)

data02 = file_display.readline(100)
print(data02)
data02 = file_display.readline()
print(data02)
