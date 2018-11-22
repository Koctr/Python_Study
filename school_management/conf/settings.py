# -*- coding:utf-8 -*-
# Author: Koctr


import os


# 基本路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 数据字典
# DATA_DICT{"表名称": { "列名": ["列长度", "列类型", "列描述"]}
DATA_DICT = {
    "schools": {"id": [32, str, "学校ID"],
                "location": [20, str, "学校地点"]},
    "teachers": {"id": [32, str, "讲师ID"],
                 "name": [20, str, "讲师名"],
                 "school": [32, str, "讲师学校"],
                 "course": [32, str, "讲师课程"]},
    "courses": {"id": [32, str, "课程ID"],
                "name": [20, str, "课程名称"],
                "price": [5, int, "课程价格"],
                "cycle": [2, int, "课程周期"],},
    "classes": {"id": [32, str, "班级ID"],
                "name": [20, str, "班级名称"],
                "school": [32, str, "班级所属学校"]},
    "students": {"id": [32, str, "学员ID"],
                 "name": [20, str, "学员姓名"],
                 "clazz": [32, str, "学员所在班级"]},
    "schools_courses": {"id": [32, str, "学校课程ID"],
                        "course": [32, str, "课程ID"],
                        "school": [32, str, "学校ID"]},
    "classes_teachers_courses": {"id": [32, str, "班级、教师、课程ID"],
                                 "clazz": [32, str, "班级ID"],
                                 "teacher": [32, str, "讲师ID"],
                                 "course": [32, str, "课程ID"],
                                 "status": [1, bool, "课程状态"]},
    "students_courses": {"id": [32, str, "学生课程ID"],
                         "student": [32, str, "学校ID"],
                         "course": [32, str, "课程ID"],
                         "score": [3, int, "课程成绩"]},
}
