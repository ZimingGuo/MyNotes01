# author: Ziming Guo
# time: 2020/3/16
"""
    demo09:
        空洞文件
"""

f = open('test', 'wb')

f.write(b'START')
f.seek(1024 * 1024 * 100, 2)
# 这段空间内没有任何数据
# 就是白白占用了这么大空间，所以才说空洞文件
# 这有点类似下载文件之前对于内存的预留空间
f.write(b'END')

f.close()
