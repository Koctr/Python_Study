# -*- encoding:utf-8 -*-
# Author: Koctr


from core import data_utils
from core.clazz import Teacher
from core.clazz import Class
from core.clazz import ClassTeacherCourse
from core.clazz import Course
from core.service import base_service


def login():
    """
    管理登录，没有验证用户名和密码
    :return: 无
    """
    admin_menu = """
            -----管理入口菜单-----
            1. 注册讲师
            2. 创建班级
            3. 建立课程
            4. 返回
            """
    admin_menu_dic = {
        "1": create_teacher,
        "2": create_class,
        "3": create_course,
        "4": base_service.print_main_menu
    }
    while True:
        print(admin_menu)
        admin_option = input("请输入数字选择菜单，输入exit退出程序：").strip()
        if admin_option in admin_menu_dic:
            admin_menu_dic[admin_option]()
            if admin_option == "4":
                break
        elif admin_option == "exit":
            exit()
        else:
            print("\33[31;1m无效的选择\33[0m")


def create_teacher():
    """
    创建讲师
    1. 获取学校数据字典、课程数据字典、学校与课程的关联数据字典
    2. 如果所有数据获取成功，获取学校与课程关联数据字典的值（关联数据对象）元组，根据关联数据输出对应的学校和课程；
       如果获取不成功，提示数据加载失败
    3. 提示输入讲师姓名和序号，如果输入正确，创建讲师，将讲师、学校、课程关联起来，讲师与学校、课程是一对一的关系，
       如输入不正确，提示。
    :return: 无
    """
    schools_data = data_utils.load_file("schools")
    courses_data = data_utils.load_file("courses")
    schools_courses_data = data_utils.load_file("schools_courses")
    if schools_data and courses_data and schools_courses_data:
        schools_courses = tuple(schools_courses_data.values())
        index = 1
        print("序号\t学校地点\t课程名称")
        for school_courses in schools_courses:
            print("%s\t%s\t%s" % (index, schools_data[school_courses.school].location,
                                  courses_data[school_courses.course].name))
            index += 1
        admin_input = input("请输入教师姓名，序号，以逗号分隔：").strip()
        admin_input = admin_input.split(",")
        if len(admin_input) == 2:
            teacher_name = admin_input[0].strip()
            index = admin_input[1].strip()
            if not data_utils.check_data_valid("teachers", {"name": teacher_name}):
                pass
            elif not index.isdigit() or int(index) < 1 or int(index) > len(schools_courses):
                print("\33[31;1m输入的序号不正确\33[0m")
            else:
                teacher = Teacher(None, teacher_name, schools_courses[int(index) - 1].school,
                                  schools_courses[int(index) - 1].course)
                if teacher.save():
                    print("注册讲师成功")
                else:
                    print("\33[31;1m注册讲师失败\33[0m")
        else:
            print("\33[31;1m输入格式不正确\33[0m")
    else:
        print("\33[31;1m数据加载失败，无法创建讲师\33[0m")


def create_class():
    """
    创建班级
    1. 获取讲师数据字典，如获取失败，提示请先创建讲师或数据加载失败；如获取成功，则获取学校数据字典和课程数据字典，
       如获取成功，执行2，否则提示数据加载失败；
    2. 获取讲师数据字典的值元组，根据讲师与学校、课程的关联关系，输出序号、学校、课程、讲师
    3. 提示输入班级名称和序号，如果输入正确，通过学校创建班级，将班级与学校、讲师、课程关联，如果输入错误，提示
    :return: 
    """
    teachers_data = data_utils.load_file("teachers")
    if not teachers_data:
        print("\33[31;1m讲师数据加载失败或讲师数据不存在\33[0m")
        return
    schools_data = data_utils.load_file("schools")
    courses_data = data_utils.load_file("courses")
    if schools_data and courses_data:
        teachers = tuple(teachers_data.values())
        index = 1
        print("序号\t学校地点\t课程名称\t讲师姓名")
        for teacher in teachers:
            print("%s\t%s\t%s\t%s" % (index, schools_data[teacher.school].location,
                                      courses_data[teacher.course].name, teacher.name))
            index += 1
        admin_input = input("请输入班级名称和序号，以逗号分隔：").strip()
        admin_input = admin_input.split(",")
        if len(admin_input) == 2:
            class_name = admin_input[0].strip()
            index = admin_input[1].strip()
            if not data_utils.check_data_valid("classes", {"name": class_name}):
                pass
            elif not index.isdigit() or int(index) < 1 or int(index) > len(teachers):
                print("\33[31;1m输入的序号不正确\33[0m")
            else:
                teacher = teachers[int(index) - 1]
                course = courses_data[teacher.course]
                a_class = Class(None, class_name)
                class_teacher_course = ClassTeacherCourse(None, teacher.id, course.id)
                school = schools_data[teacher.school]
                if school.create_class(a_class, class_teacher_course):
                    print("班级创建成功")
                else:
                    print("\33[31;1m班级创建失败\33[0m")
        else:
            print("\33[31;1m输入格式不正确\33[0m")
    else:
        print("\33[31;1m数据加载失败，无法创建班级\33[0m")


def create_course():
    """
    创建课程：
    1. 获取学校数据字典，如果获取成功，执行2，获取失败，提示数据加载失败
    2. 输出学校数据：序号、地点
    3. 提示输入序号及课程相关数据
    4. 如果输入的数据有效，创建课程，否则提示错误
    :return: 无
    """
    schools_data = data_utils.load_file("schools")
    if schools_data:
        print("学校序号\t学校地点")
        index = 1
        schools = tuple(schools_data.values())
        for school in schools:
            print("%s\t%s" % (index, school.location))
            index += 1
        admin_input = input("请输入课程名称、费用、周期、学校序号，以逗号分隔：").strip()
        admin_input = admin_input.split(",")
        if len(admin_input) == 4:
            course_name = admin_input[0].strip()
            course_price = admin_input[1].strip()
            course_cycle = admin_input[2].strip()
            index = admin_input[3].strip()
            if not data_utils.check_data_valid("courses", {"name": course_name,
                                                           "price": course_price,
                                                           "cycle": course_cycle}):
                pass
            elif not index.isdigit() or int(index) < 1 or int(index) > len(schools):
                print("\33[31;1m输入的序号不正确\33[0m")
            else:
                course = Course(None, course_name, course_price, course_cycle)
                if schools[int(index) - 1].create_course(course):
                    print("课程创建成功")
                else:
                    print("\33[31;1m课程创建失败\33[0m")
        else:
            print("\33[31;1m输入的格式不正确\33[0m")
    else:
        print("\33[31;1m数据加载失败，无法创建课程\33[0m")
