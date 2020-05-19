# author: Ziming Guo
# time: 2020/2/23
'''
    业务逻辑处理
'''
class StudentManagerController:
    """
        学生管理控制器，负责处理管理系统的逻辑处理
    """
    __init_id = 0

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
        学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
        添加一个新学生
        :param stu_info:没有编号的学生信息
        :return:
        """
        stu_info.id = self.__generate_id()

        self.stu_list.append(stu_info)

    def __generate_id(self):
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
                self.__stu_list.remove(item)
                return True
        return False

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

    def order_by_score(self):
        """
            根据成绩对学生列表进行升序排列
        :return:
        """
        for r in range(0, len(self.stu_list) - 1):
            for c in range(r + 1, len(self.stu_list)):
                if self.stu_list[r].score > self.stu_list[c].score:
                    self.stu_list[r], self.stu_list[c] = self.stu_list[c], self.stu_list[r]
