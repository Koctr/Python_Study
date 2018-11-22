# -*- coding:utf-8 -*-
# Author: Koctr


class SchoolMember(object):
    """学校成员基类"""
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        """注册"""
        print("Just enrolled a new school member [%s]" % self.name)
        SchoolMember.member += 1

    def tell(self):
        """学校成员信息"""
        print("---------info: %s--------" % self.name)
        for k, v in self.__dict__.items():
            print("\t", k, v)
        print("---------end: %s---------" % self.name)


class Teacher(SchoolMember):
    """讲师"""
    def __init__(self, name, age, sex, salary, course):
        SchoolMember.__init__(self, name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        """教学"""
        print("Teacher [%s] is teaching [%s]" % (self.name, self.course))


class Student(SchoolMember):
    """学生"""
    def __init__(self, name, age, sex, course, tuition):
        # 经典类
        # SchoolMember.__init__(self, name, age, sex)
        # 新式类
        super(Student, self).__init__(name, age,sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        """缴费"""
        print("Student [%s] has just paied [%s]" % (self.name, amount))
        self.amount += amount

    def __del__(self):
        print("开除了[%s]" % self.name)
        SchoolMember.member -= 1


t1 = Teacher("Wusir", 27, "M", 3000, "Python")
s1 = Student("HaiTao", 30, "M", "Python", 30000)
s2 = Student("LiChuang", 12, "M", "Python", 15000)

print(SchoolMember.member)

del s2

print(SchoolMember.member)

t1.tell()
s1.tell()
