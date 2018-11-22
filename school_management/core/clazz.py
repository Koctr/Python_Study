# -*- coding:utf-8 -*-
# Author: Koctr


import uuid
from core import data_utils


class School(object):
    """"学校类"""
    def __init__(self, school_id, location):
        if not school_id:
            self.id = uuid.uuid1()
        else:
            self.id = school_id
        self.location = location

    def save(self):
        """保存学校数据"""
        data = data_utils.load_file("schools")
        data[self.id] = self
        success = data_utils.save_file("schools", data)
        return success

    def create_course(self, course):
        """
        创建课程
        :param course: 课程
        :return: 无
        """
        course.school = self.id
        """
        if not course.price.isdigit() or int(course.price) < 0:
            print("课程价格应为正整数")
            return
        if not course.cycle.isdigit() or int(course.cycle) < 1 or int(course.cycle) > 12:
            print("课程周期应为正确的月份（1-12）")
            return
        """
        is_valid = True
        data = data_utils.load_file("courses")
        for key in data:
            course_in_data = data[key]
            if course_in_data.name == course.name and course_in_data.school == self.id:
                print("课程已存在")
                is_valid = False
                break
        if is_valid:
            data[course.id] = course
            data_utils.save_file("courses", data)
            schools_courses_data = data_utils.load_file("schools_courses")
            school_course = SchoolCourse(None, self.id, course.id)
            schools_courses_data[school_course.id] = school_course
            success = data_utils.save_file("schools_courses", schools_courses_data)
            return success
        return False

    def create_class(self, a_class, class_teacher_course):
        """
        创建班级
        :param a_class: 班级对象
        :param class_teacher_course: 班级、讲师、课程关联对象
        :return: 
        """
        a_class.school = self.id
        is_valid = True
        classes_data = data_utils.load_file("classes")
        for key in classes_data:
            if classes_data[key].name == a_class.name and classes_data[key].school == self.id:
                print("班级已存在")
                is_valid = False
                break
        if is_valid:
            classes_data[a_class.id] = a_class
            data_utils.save_file("classes", classes_data)
            class_teacher_course.class_id = a_class.id
            classes_teachers_courses_data = data_utils.load_file("classes_teachers_courses")
            classes_teachers_courses_data[class_teacher_course.id] = class_teacher_course
            success = data_utils.save_file("classes_teachers_courses", classes_teachers_courses_data)
            return success
        return False


class Course(object):
    """课程类"""
    def __init__(self, course_id, name, price, cycle):
        if not course_id:
            self.id = uuid.uuid1()
        else:
            self.id = course_id
        self.name = name
        self.price = price
        self.cycle = cycle
        self.school = None


class SchoolCourse(object):
    """学校、课程关联类"""
    def __init__(self, sc_id, school, course):
        """
        构造函数
        :param sc_id: 学校、课程关联ID
        :param school: 学校ID
        :param course: 课程ID
        """
        if not sc_id:
            self.id = uuid.uuid1()
        else:
            self.id = sc_id
        self.school = school
        self.course = course


class Teacher(object):
    """讲师类"""
    def __init__(self, teacher_id, name, school, course):
        """
        构造函数
        :param teacher_id: 讲师id
        :param name: 讲师姓名
        :param school: 所属学校（id）
        :param course: 所授课程（id）
        """
        self.name = name
        self.school = school
        self.course = course
        if not teacher_id:
            self.id = uuid.uuid1()
        else:
            self.id = teacher_id

    def save(self):
        """保存讲师数据"""
        is_valid = True
        data = data_utils.load_file("teachers")
        for key in data:
            teacher = data[key]
            if teacher.name == self.name and teacher.school == self.school:
                print("\33[31;1m讲师已存在\33[0m")
                is_valid = False
                break
        if is_valid:
            data[self.id] = self
            success = data_utils.save_file("teachers", data)
            return success
        return False


class Student(object):
    """学生类"""
    def __init__(self, student_id, name):
        self.name = name
        if not student_id:
            self.id = uuid.uuid1()
        else:
            self.id = student_id
        self.clazz = None

    def register(self):
        """注册学生"""
        is_valid = True
        data = data_utils.load_file("students")
        for key in data:
            student = data[key]
            if student.name == self.name:
                print("\33[31;1m学生已存在\33[0m")
                is_valid = False
                break
        if is_valid:
            data[self.id] = self
            success = data_utils.save_file("students", data)
            return success
        return False

    def choose_class(self, clazz):
        """选班"""
        self.clazz = clazz
        data = data_utils.load_file("students")
        self.name = data[self.id].name
        data[self.id] = self
        success = data_utils.save_file("students", data)
        return success


class Class(object):
    """班级类"""
    def __init__(self, class_id, name):
        """
        构造函数
        :param class_id: 班级id
        :param name: 班级名称
        """
        self.name = name
        self.school = None
        if not class_id:
            self.id = uuid.uuid1()
        else:
            self.id = class_id

    def view_students(self):
        data = data_utils.load_file("students")
        if not data:
            print("\33[31;1m该班级没有学员\33[0m")
            return
        print("序号\t姓名")
        index = 1
        for key in data:
            if data[key].clazz == self.id:
                print("%s\t%s" % (index, data[key].name))
                index += 1


class ClassTeacherCourse(object):
    """班级、讲师、课程关联"""
    def __init__(self, c_t_c_id, teacher, course):
        """
        构造函数
        :param c_t_c_id: 关联id
        :param teacher: 讲师id
        :param course: 课程id
        """
        self.class_id = None
        self.teacher = teacher
        self.course = course
        self.status = False
        if not c_t_c_id:
            self.id = uuid.uuid1()
        else:
            self.id = c_t_c_id

    def update_status(self, status):
        """
        更新上课状态
        :param status: 上课状态
        :return: 
        """
        data = data_utils.load_file("classes_teachers_courses")
        data[self.id].status = status
        success = data_utils.save_file("classes_teachers_courses", data)
        return success


class StudentCourse(object):
    """学生、课程关联"""
    def __init__(self, s_c_id, school, student, course):
        """
        构造函数
        :param s_c_id: 学生课程关联id 
        :param school: 学校id
        :param student: 学生id
        :param course: 课程id
        """
        self.student = student
        self.school = school
        self.course = course
        self.score = None
        if not s_c_id:
            self.id = uuid.uuid1()
        else:
            self.id = s_c_id

    def update_score(self, score):
        """
        更新学生成绩
        :param score: 学生成绩 
        :return: 
        """
        self.score = score
        data = data_utils.load_file("students_courses")
        data[self.id] = self
        success = data_utils.save_file("students_courses", data)
        return success

    def payment(self):
        """缴费"""
        data = data_utils.load_file("students_courses")
        data[self.id] = self
        success = data_utils.save_file("students_courses", data)
        return success
