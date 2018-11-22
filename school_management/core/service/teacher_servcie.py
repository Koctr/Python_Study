# -*- encoding:utf-8 -*-
# Author: Koctr


from core import data_utils
from core.service import base_service


teacher_data = {
    "teacher_id": None
}


def login():
    """
    讲师登录
    1. 提示输入讲师名
    2. 获取讲师数据字典，查找字典中讲师名是否存在
    2.1 如存在，设置is_valid = True，不存在，设置input_count += 1，如input_count > 3，返回主菜单
    3 如is_valid == True，输出讲师菜单
    """
    input_count = 0
    teachers_data = data_utils.load_file("teachers")
    is_valid = False
    exit_flag = False
    while not exit_flag:
        user_input = input("请输入讲师用户名，输入back返回主菜单：").strip()
        if user_input == "back":
            base_service.print_main_menu()
            break
        else:
            for key in teachers_data:
                if teachers_data[key].name == user_input:
                    is_valid = True
                    exit_flag = True
                    teacher_data["teacher_id"] = key
                    break
        if not is_valid:
            input_count += 1
            print("\33[31;1m输入的讲师用户名不正确，请重新输入（还有%s次机会）\33[0m"
                  % (3 - input_count))
            if input_count == 3:
                base_service.print_main_menu()
                break
    if is_valid:
        teacher_menu = """
        -----讲师入口菜单-----
            1. 选班上课
            2. 下课
            3. 查看学员
            4. 修改成绩
            5. 返回
        """
        teacher_dict = {
            "1": class_begin,
            "2": class_over,
            "3": view_students,
            "4": update_score,
            "5": base_service.print_main_menu
        }
        while True:
            print(teacher_menu)
            teacher_input = input("请输入数字选择菜单，输入exit退出程序：").strip()
            if teacher_input in teacher_dict:
                teacher_dict[teacher_input]()
                if teacher_input == "5":
                    teacher_data["teacher_id"] = None
                    break
            elif teacher_input == "exit":
                exit()
            else:
                print("\33[31;1m无效的选择\33[0m")


def class_begin():
    """
    选班上课
    1. 如果讲师号存在，执行2，否则提示讲师未登录
    2. 获取班级数据字典，课程数据字典，班级、讲师、课程关联数据字典，获取成功，执行3，否则提示数据加载失败
    3. 获取班级、讲师、课程关联数据字典值元组，在其中查找匹配讲师号的数据，如该数据存在且状态为True，提示已上课，否则
       过滤出该条数据（讲师关联的班级），执行4
    4. 根据过滤出的数据，输出班级、课程，提示选班
    5. 如选择合规，设置改条数据的状态为True
    """
    if teacher_data["teacher_id"]:
        classes_data = data_utils.load_file("classes")
        courses_data = data_utils.load_file("courses")
        classes_teachers_courses_data = data_utils.load_file("classes_teachers_courses")
        if classes_data and courses_data and classes_teachers_courses_data:
            data = tuple(classes_teachers_courses_data.values())
            filtered = []
            for class_teacher_course in data:
                if teacher_data["teacher_id"] == class_teacher_course.teacher:
                    if class_teacher_course.status:
                        print("\33[31;1m讲师已在上课中，请先选择下课\33[0m")
                        return
                    else:
                        filtered.append(class_teacher_course)
            index = 1
            print("序号\t班级\t课程")
            for class_teacher_course in filtered:
                print("%s\t%s\t%s" % (index, classes_data[class_teacher_course.class_id].name,
                                      courses_data[class_teacher_course.course].name))
                index += 1
            teacher_input = input("输入序号选择要上课的班级：").strip()
            if not teacher_input.isdigit() or int(teacher_input) < 1 or int(teacher_input) > len(filtered):
                print("\33[31;1m输入的序号不正确\33[0m")
            else:
                index = int(teacher_input) - 1
                success = filtered[index].update_status(True)
                if success:
                    print("已成功选班上课")
                else:
                    print("\33[31;1m选班上课失败\33[0m")
        else:
            print("\33[31;1m数据加载失败\33[0m")
    else:
        print("\33[31;1m讲师未登录\33[0m")


def class_over():
    """
    下课
    1. 如果讲师号存在，执行2，否则提示讲师未登录
    2. 获取班级、讲师、课程关联数据字典，获取成功，查找匹配讲师号的记录，执行3，获取失败，提示数据加载失败
    3. 记录状态为True，修改为False，提示成功下课，未能成功修改，提示数据操作失败
    4. 没有状态为True的记录，提示没有上课
    """
    if teacher_data["teacher_id"]:
        classes_teachers_courses_data = data_utils.load_file("classes_teachers_courses")
        if classes_teachers_courses_data:
            data = tuple(classes_teachers_courses_data.values())
            for class_teacher_course in data:
                if teacher_data["teacher_id"] == class_teacher_course.teacher:
                    if class_teacher_course.status:
                        success = class_teacher_course.update_status(False)
                        if success:
                            print("已成功下课")
                        else:
                            print("\33[31;1m数据操作失败\33[0m")
                        return
            print("\33[31;1m讲师没有上课，请先选班上课\33[0m")
        else:
            print("\33[1m数据加载失败\33[0m")
    else:
        print("\33[31;1m讲师未登录\33[0m")


def view_students():
    """
    查看学员
    1. 如果讲师号存在，执行2，否则提示讲师未登录
    2. 获取班级数据字典，班级、讲师、课程关联数据字典
    3. 从关联数据字典中过滤出包含讲师号的数据
    4. 根据过滤数据输出要查看学员的班级
    5. 提示输入，根据输入输出学员
    """
    if teacher_data["teacher_id"]:
        classes_teachers_course_data = data_utils.load_file("classes_teachers_courses")
        classes_data = data_utils.load_file("classes")
        if classes_teachers_course_data and classes_data:
            data = tuple(classes_teachers_course_data.values())
            filtered = []
            for class_teacher_course in data:
                if class_teacher_course.teacher == teacher_data["teacher_id"]:
                    filtered.append(class_teacher_course)
            index = 1
            print("序号\t班级名称")
            for classes in filtered:
                print("%s\t%s" % (index, classes_data[classes.class_id].name))
                index += 1
            teacher_input = input("请输入序号选择要查看的班级：").strip()
            if not teacher_input.isdigit() or int(teacher_input) < 1 or int(teacher_input) > len(filtered):
                print("\33[31;1m输入的序号不正确\33[0m")
            else:
                index = int(teacher_input) - 1
                classes_data[filtered[index].class_id].view_students()
        else:
            print("\33[31;1m数据加载失败\33[0m")
    else:
        print("\33[31;1m讲师未登录\33[0m")


def update_score():
    """
    修改成绩
    1. 如果讲师号存在，执行2，否则提示讲师未登录
    2. 获取学生数据字典，班级、讲师、课程关联数据字典，学生、课程关联数据字典，课程数据字典
    3. 从班级、讲师、课程关联数据字典中过滤出包含讲师号的数据
    4. 根据过滤出的班级、讲师、课程关联数据字典，以及学生数据字典，过滤出讲师管理的学生数据字典
    5. 根据过滤出的学生数据字典，学生、课程关联数据字典，过滤出学生、课程关联数据字典
    6. 输出过滤出的学生、课程数据，提示输入序号及要修改的成绩
    7. 如输入正确，则修改成绩
    """
    if teacher_data["teacher_id"]:
        classes_teachers_course_data = data_utils.load_file("classes_teachers_courses")
        students_data = data_utils.load_file("students")
        students_courses_data = data_utils.load_file("students_courses")
        courses_data = data_utils.load_file("courses")
        if classes_teachers_course_data and students_data and students_courses_data and courses_data:
            data = tuple(classes_teachers_course_data.values())
            # 找到教师管理的班级
            for class_teacher_course in data:
                if class_teacher_course.teacher != teacher_data["teacher_id"]:
                    classes_teachers_course_data.pop(class_teacher_course.id)
            # 找到班级对应的学生
            filtered_students = dict()
            for key in classes_teachers_course_data:
                for f_key in students_data:
                    if classes_teachers_course_data[key].class_id == students_data[f_key].clazz:
                        filtered_students[f_key] = students_data[f_key]
            # 找到学生对应的学生、课程关联数据
            filtered_students_courses = dict()
            for key in filtered_students:
                for f_key in students_courses_data:
                    if filtered_students[key].id == students_courses_data[f_key].student:
                        filtered_students_courses[f_key] = students_courses_data[f_key]
            if not filtered_students_courses:
                print("\33[31;1m没有学生学习课程\33[0m")
                return
            # 根据学生、课程关联数据输出列表
            index = 1
            data = tuple(filtered_students_courses.values())
            print("序号\t学生姓名\t课程\t成绩")
            for student_course in data:
                print("%s\t%s\t%s\t%s" % (index, filtered_students[student_course.student].name,
                                          courses_data[student_course.course].name,
                                          student_course.score))
            teacher_input = input("请输入新的成绩和序号，以逗号分隔：").strip()
            teacher_input = teacher_input.split(",")
            if len(teacher_input) == 2:
                score = teacher_input[0].strip()
                index = teacher_input[1].strip()
                if not index.isdigit() or int(index) < 1 or int(index) > len(data):
                    print("\33[31;1m输入的序号不正确\33[0m")
                elif not score.isdigit() or int(score) < 0 or int(score) > 100:
                    print("\33[31;1m成绩应该是0-100的整数\33[0m")
                else:
                    index = int(index) - 1
                    success = students_courses_data[data[index].id].update_score(int(score))
                    if success:
                        print("成绩已修改")
                    else:
                        print("\33[31;1m成绩修改失败\33[0m")
            else:
                print("\33[31;1m输入格式不正确\33[0m")
        else:
            print("\33[31;1m数据加载失败\33[0m")
    else:
        print("\33[31;1m讲师未登录\33[0m")
