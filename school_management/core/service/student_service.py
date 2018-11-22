# -*- encoding:utf-8 -*-
# Author: Koctr


from core import data_utils
from core.service import base_service
from core.clazz import Student
from core.clazz import StudentCourse


# 已登录学生数据字典，未使用装饰器进行验证
student_data = {
    "student_id": None
}


def login():
    """
    学生登录
    1. 提示用户输入
    2. 输入back，返回主菜单；不输入任何内容，设置is_valid = True；输入用户名，则执行2.1
    2.1 获取学生数据字典，查找字典中是否存在输入的用户名
    2.2 如用户名存在，设置is_valid = True，否则设置input_count += 1，如果input_count > 3，返回主菜单
    3. 如果is_valid == True，输出学生菜单
    """
    # 输入错误次数统计
    input_count = 0
    # 输入是否有效
    is_valid = False
    # 是否退出循环
    exit_flag = False
    while not exit_flag:
        user_input = input("请输入学生用户名，未注册直接回车，输入back返回主菜单：").strip()
        if user_input == "back":
            base_service.print_main_menu()
            break
        elif not user_input:
            is_valid = True
            break
        else:
            students_data = data_utils.load_file("students")
            for key in students_data:
                if students_data[key].name == user_input:
                    is_valid = True
                    exit_flag = True
                    student_data["student_id"] = key
                    break
        if not is_valid:
            input_count += 1
            print("\33[31;1m输入的学生用户名不正确，请重新输入（还有%s次机会）\33[0m"
                  % (3 - input_count))
            if input_count == 3:
                base_service.print_main_menu()
                break
    if is_valid:
        student_menu = """
           -----学生入口菜单-----
               1. 注册
               2. 缴费
               3. 选班
               4. 返回
           """
        student_dict = {
            "1": register,
            "2": payment,
            "3": choose_class,
            "4": base_service.print_main_menu
        }
        while True:
            print(student_menu)
            student_input = input("请输入数字选择菜单，输入exit退出程序：").strip()
            if student_input in student_dict:
                student_dict[student_input]()
                if student_input == "4":
                    student_data["student_id"] = None
                    break
            elif student_input == "exit":
                exit()
            else:
                print("\33[31;1m无效的选择\33[0m")


def register():
    """
    学生注册
    1. 如果学号存在，提示学生已注册
    2. 否则，提示输入注册名，注册名如有效，注册学生
    """
    if student_data["student_id"]:
        print("\33[31;1m学生已注册，无需重复注册\33[0m")
    else:
        student_name = input("请输入注册名：").strip()
        is_valid = True
        students_data = data_utils.load_file("students")
        for key in students_data:
            if students_data[key].name == student_name:
                is_valid = False
                print("\33[31;1m学员姓名重复\33[0m")
                break
        if is_valid:
            if not data_utils.check_data_valid("students", {"name": student_name}):
                pass
            else:
                student = Student(None, student_name)
                if student.register():
                    student_data["student_id"] = student.id
                    print("学生已注册")
                else:
                    print("\33[31;1m未能成功注册\33[0m")


def payment():
    """
    缴费
    1. 如果学号不存在，提示未注册
    2. 获取学校、课程、讲师、班级及相关联的数据字典，如果获取失败，提示“数据加载失败”（有默认课程存在，不存在无课程数据的情况）
    3. 输出开班课程列表，提示输入序号缴费
    4. 如输入合规，关联课程与学生，未考虑学生与课程重复关联的情况
    """
    if not student_data["student_id"]:
        print("\33[31;1m学生未注册，请先注册\33[0m")
    else:
        courses_data = data_utils.load_file("courses")
        teachers_data = data_utils.load_file("teachers")
        schools_data = data_utils.load_file("schools")
        classes_teachers_courses_data = data_utils.load_file("classes_teachers_courses")
        if not classes_teachers_courses_data:
            print("\33[31;1m暂无开班课程\33[0m")
            return
        data = tuple(classes_teachers_courses_data.values())
        index = 1
        print("序号\t课程名称\t价格\t周期\t学校\t讲师")
        for class_teacher_course in data:
            print("%s\t%s\t%s\t%s\t%s\t%s\t" % (index, courses_data[class_teacher_course.course].name,
                                                courses_data[class_teacher_course.course].price,
                                                courses_data[class_teacher_course.course].cycle,
                                                schools_data[teachers_data[class_teacher_course.teacher].school].
                                                location,
                                                teachers_data[class_teacher_course.teacher].name))
            index += 1
        student_input = input("输入序号进行缴费：").strip()
        if not student_input.isdigit() or int(student_input) < 1 or int(student_input) > len(data):
            print("\33[31;1m输入的序号不正确\33[0m")
        else:
            student_course = StudentCourse(None, schools_data[teachers_data[data[int(student_input)-1].teacher].school],
                                           student_data["student_id"],
                                           courses_data[data[int(student_input) - 1].course].id)
            success = student_course.payment()
            if success:
                print("缴费成功")
            else:
                print("\33[31;1m缴费失败\33[0m")


def choose_class():
    """选班
    1. 如果学号不存在，提示未注册
    2. 如果学生没有与任何课程关联，提示未缴费
    3. 以上皆通过，输出与学生课程相关联班级，供选择
    4. 根据选择更新学生班级
    """
    if not student_data["student_id"]:
        print("\33[31;1m学生未注册，请先注册\33[0m")
    else:
        students_courses_data = data_utils.load_file("students_courses")
        is_payment = False
        for key in students_courses_data:
            print(key, students_courses_data[key])
            if students_courses_data[key].student == student_data["student_id"]:
                is_payment = True
                break
        if is_payment:
            classes_teachers_courses_data = data_utils.load_file("classes_teachers_courses")
            filtered = []
            for s_key in students_courses_data:
                for c_key in classes_teachers_courses_data:
                    if students_courses_data[s_key].course == classes_teachers_courses_data[c_key].course:
                        filtered.append(classes_teachers_courses_data[c_key])
            if not filtered:
                print("\33[31;1m该课程暂未开班\33[0m")
                return
            index = 1
            classes_data = data_utils.load_file("classes")
            print("序号\t班级")
            for clazz in filtered:
                print("%s\t%s" % (index, classes_data[clazz.class_id].name))
            student_input = input("请输入序号选择班级：").strip()
            if not student_input.isdigit() or int(student_input) < 1 or int(student_input) > len(filtered):
                print("\33[31;1m输入的序号不正确\33[0m")
            else:
                student = Student(student_data["student_id"], None)
                success = student.choose_class(filtered[int(student_input) - 1].class_id)
                if success:
                    print("选班成功")
                else:
                    print("\33[31;1m选班失败\33[0m")
        else:
            print("\33[31;1m学生尚未缴费，请先缴费\33[0m")
