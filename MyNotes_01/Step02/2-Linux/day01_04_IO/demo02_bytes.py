# author: Ziming Guo
# time: 2020/3/14

s = "hello"  # 字符串
print(s)
s = b"hello"  # 字节串（python中二进制表示方式，0 1形式）
print(s)

s = "你好"
print(s)
# 这种情况下就要用 encode 来转换了
# encode 也可以用来转换 ascii 码，encode 是万能的，"b"是ascii特权
s = "你好".encode()
print(s)
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode())
print(s.decode())

'''
所有的字符串都能用 encode 转化成字节串 
但不是所有的字节串都能用 decode 转化成字符串
只有那些能够被转化成文本的东西才能被转化成字符串
像音频视频啥的就不行，因为不能被转化成文本。
'''
