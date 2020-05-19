# author: Ziming Guo
# time: 2020/2/22
'''
    练习4配套代码，二维向量移动
'''
class Vector:
    """

    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left(vector_old):
        # vector_new = vector_old
        # vector_new.x = vector_old.x
        # vector_new.y = vector_old.y - 1
        vector_old.y -= 1
        return vector_old

    @staticmethod
    def right(vector_old):
        # vector_new = vector_old
        # vector_new.x = vector_old.x
        # vector_new.y = vector_old.y + 1
        vector_old.y += 1
        return vector_old

    @staticmethod
    def up(vector_old):
        # vector_new = vector_old
        # vector_new.x = vector_old.x - 1
        vector_old.x -= 1
        # vector_new.y = vector_old.y
        return vector_old

    @staticmethod
    def down(vector_old):
        # vector_new = vector_old
        # vector_new.x = vector_old.x + 1
        vector_old.x += 1
        # vector_new.y = vector_old.y
        return vector_old

    @staticmethod
    def leftup(vector_old):
        vector_old.x -= 1
        vector_old.y -= 1
        return vector_old

    @staticmethod
    def leftdown(vector_old):
        vector_old.x += 1
        vector_old.y -= 1
        return vector_old

    @staticmethod
    def rightup(vector_old):
        vector_old.x -= 1
        vector_old.y += 1
        return vector_old

    @staticmethod
    def rightdown(vector_old):
        vector_old.x += 1
        vector_old.y += 1
        return vector_old


# v01 = Vector.left(Vector(1, 1))
# v02 = Vector.right(Vector(1, 1))
# v03 = Vector.up(Vector(1, 1))
# v04 = Vector.down(Vector(1, 1))
# print(v01.x, v01.y)
# print(v02.x, v02.y)
# print(v03.x, v02.y)
# print(v04.x, v02.y)


# 再创建一个类
class GetVectorHelper:
    """

    """
    @staticmethod
    def get_elements(target_list, vector, direction, count):
        vector_new_list = []
        v = Vector(0, 0)
        for i in range(count):
            if direction == "left":
                v = Vector.left(vector)
                # vector_new = target_list[v.x][v.y] # 这里一定注意：现在的  vector_new 是个字符串，没有 x y 的属性了！
                # vector_new_list.append(vector_new)
                # vector = v # 这个地方应该传过去一个 v
            elif direction == "right":
                v = Vector.right(vector)
            elif direction == "up":
                v = Vector.up(vector)
            elif direction == "down":
                v = Vector.down(vector)
            elif direction == "leftup":
                v = Vector.leftup(vector)
            elif direction == "leftdown":
                v = Vector.leftdown(vector)
            elif direction == "rightup":
                v = Vector.rightup(vector)
            elif direction == "rightdown":
                v = Vector.rightdown(vector)

            vector_new = target_list[v.x][v.y]
            vector_new_list.append(vector_new)
            vector = v
        return vector_new_list