# author: Ziming Guo
# time: 2020/2/18
'''
    作业3：
    完成学生管理系统中，根据成绩升序显示的功能.
'''


class StudentModel:
    """
    学生信息模型（模版）
    """

    def __init__(self, name="", age=0, score=0, id=0):
        # 正常来说这个 id 就不应该是人输入的，而应该是系统自动生成的，以保证准确性
        # 每次系统 add 一遍都会让 id 加一
        """
        创建学生对象
        :param id:编号(该学生的唯一标识)
        :param name:姓名(字符串类型)
        :param age:年龄 int
        :param score:成绩 float
        """
        self.__id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
    #
    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     self.__name = value
    #
    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, value):
    #     self.__age = value
    #
    # @property
    # def score(self):
    #     return self.__score
    #
    # @score.setter
    # def score(self, value):
    #     self.__score = value


class StudentManagerController:
    """
        学生管理控制器，负责处理管理系统的逻辑处理
    """
    __init_id = 0  # 这是个类变量，在方法里访问的时候，应该用类去访问

    # 用类变量表示处世编号，所有变量共享

    # def __init__(self, stu_list): # 这句话的意思是让用这个类的人来填写 stu_list
    # 而这句话的真实目的是从 StudentModel 来获取 stu_list
    # 所以应该不再括号里面写这个 list
    def __init__(self):
        self.__stu_list = []  # 如果这个地方一直都是有双下划线
        # 就会在类外调用类的时候，看不见这个实例成员了

    @property
    def stu_list(self):
        """
        学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    # 做一个 stu_list 用来障眼
    # 就是说：在类的外面找 __stu_list 的时候，可以直接找 stu_list
    #   但是会被 property 拦截，然后 return 回来一个 __stu_list,这个才是真正要找的

    # @stu_list.setter
    # def stu_list(self, value):
    #     self.__stu_list = value

    # 正常情况下，加上这句话就可以 set stu_list 了，但是我拿掉这句话就不能在类的外面该这个列表了

    def add_student(self, stu_info):
        """
        添加一个新学生
        :param stu_info:没有编号的学生信息
        :return:
        """
        stu_info.id = self.__generate_id()

        self.stu_list.append(stu_info)

    def __generate_id(self):  # 加上了两个下划线的意思就是不让其他人看，也不让调用，只有在类的里面可以调用且查看
        """
            生成学生的 id 编号，一个学生只有一个编号，且编号都是独一无二的
        :return:
        """
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, stu_id):
        """
            根据编号一处学生信息
        :param stu_id: 学生的编号 int
        :return: 是否删除掉的 bool 类型
        """
        for item in self.__stu_list:
            if item.id == stu_id:
                # del item # 不能这么写，这样写是del了item这个变量，而不是列表里那个元素
                self.__stu_list.remove(item)
                return True  # 找到了就是移除成功了
        return False  # 没找到就是移除失败了

    def update_student(self, stu_info):
        """
            根据学生编号修改学生信息
        :param stu_info: 新的学生信息
        :return: 是否修改成功的 bool 状态
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

        # """
        #     根据 id 修改信息
        # :param stu_id:
        # :param type:
        # :param data:
        # :return:
        # """
        # for item in self.__stu_list:
        #     if item.id == stu_id:
        #         if type == "name":
        #             item.name = data
        #         if type == "age":
        #             item.age = data
        #         if type == "score":
        #             item.score = data

    def order_by_score(self):
        """
            根据成绩对学生列表进行升序排列
        :return:
        """
        # higher = self.stu_list[0]
        # if higher.score > self.stu_list[i].score:
        # higher, self.stu_list[i] = self.stu_list[i], higher
        # return self.stu_list
        # 这种方式一般是用来找最大值的，而不是用来升降序排列的

        for r in range(0, len(self.stu_list) - 1):
            for c in range(r + 1, len(self.stu_list)):
                if self.stu_list[r].score > self.stu_list[c].score:
                    self.stu_list[r], self.stu_list[c] = self.stu_list[c], self.stu_list[r]



class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()
        # 想要只创建一个对象，就把这个创建写成实例变量

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_student(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()

    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        # id = int(input("请输入学生编号:"))
        name = input("请输入学生姓名:")
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩:"))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_student(self, list_output):
        for item in list_output:
            print("编号:", item.id, "名字:", item.name, "年龄:", item.age, "成绩:", item.score)

    def __delete_student(self):
        num = int(input("请输入所删除学生的编号:"))
        if self.__manager.remove_student(num):
            print("删除成功！")
        else:
            print("失败！")

    def __modify_student(self):
        id = int(input("请输入要修改的学生的编号:"))
        name = input("请输入新的姓名:")
        age = int(input("请输入新的年龄:"))
        score = int(input("请输入新的成绩:"))
        info = StudentModel(name, age, score, id)
        # for item in self.__manager.stu_list:
        #     if item.id == id:
        if self.__manager.update_student(info):
            print("更改成功！")
        else:
            print("失败！")

    def __output_student_by_score(self):
        # 下面这个也可以，只不过是按照成绩高低显示 name 而不是所有信息
        # list01 = []
        # self.__manager.order_by_score()  # 这一步执行完之后就已经修改了列表了
        # for item in self.__manager.stu_list:
        #     list01.append(item.name)
        # print(list01)

        self.__manager.order_by_score()
        self.__output_student(self.__manager.stu_list)


view = StudentManagerView()
view.main()

'''
# 测试代码
manager = StudentManagerController()
s01 = StudentModel(0, "haha", 1, 2)
s02 = StudentModel(1, "baba", 3, 4)
manager.add_student(s01)
manager.add_student(s02)

# for item in manager.stu_list:
#     print(item.id, item.name, item.age, item.score)

# print(manager.remove_student(2))
# print(manager.remove_student(100))

for item in manager.stu_list:
    print(item.id, item.name, item.age, item.score)

new01 = StudentModel(1, "lala", 5, 6)
new02 = StudentModel(2, "gaga", 7, 8)
manager.update_student(new01)
manager.update_student(new02)

for item in manager.stu_list:
    print(item.id, item.name, item.age, item.score)
'''

'''
# 测试代码 
a01 = StudentModel("1", 2, 3)
a02 = StudentManagerController()
a02.add_student(a01)

for item in a02.stu_list:
    print(item.name, item.age, item.score, item.id)

a02.remove_student(1)

for item in a02.stu_list:1
    print(item.name, item.age, item.score, item.id)
'''
