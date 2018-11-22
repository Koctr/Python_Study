# -*- encoding:utf-8 -*-
# Author: Koctr


import re


def run():
    """
    1. 读取算式
    2. 取最里面括号内容
    3. 获取乘除加减，去掉空格，运算
    4. 用计算结果替换括号内容
    5. 重复3-6，直到没有括号
    6. 计算最外层算式并计算
    7. 输出结果
    :return: 无
    """

    exit_flag = False
    while not exit_flag:
        expression = input("请输入算式（输入exit退出）：")
        if expression == 'exit':
            exit_flag = True
        else:
            # 判断数字中间，小数点左右是否有空格
            have_escape = re.search('\.\s+\d+|\d+\s+\.|\d+\s+\d+', expression)
            if have_escape:
                print("数字中间不能有空格")
            else:
                calc_result = get_bracket_content(expression)
                # 0或0.0也会被识别为False，'0','0.0'不会
                if str(calc_result) and calc_result is not None:
                    # 输出为float时会降低精度
                    print("计算结果为：%s" % calc_result)
                else:
                    print("无效的算式")


def get_bracket_content(expression):
    """
    获取括号内容
    :param expression: 去掉空格后的算式
    :return: 计算结果
    """
    expression = re.sub("\s*", "", expression)
    left_bracket_and_number = re.search('\d*\.?\d*\(', expression)
    right_bracket_and_number = re.search('\)\d*\.?\d*', expression)
    if left_bracket_and_number and left_bracket_and_number.group() != '(':
        print('左括号左边不能是数字')
    elif right_bracket_and_number and right_bracket_and_number.group() != ')':
        print('右括号右边不能是数字')
    else:
        bracketed = re.search("\([^()]+\)", expression)
        while bracketed:
            base_expression = bracketed.group()
            base_expression_not_square_racket = re.sub('^\(|\)$', '', base_expression)
            # 判断括号中的内容是否为数字，这个正则表达式会匹配'.'和''
            is_number = re.match('^[+-]?\d*\.?\d*$', base_expression_not_square_racket)
            if is_number and is_number.group() not in ['', '.']:
                expression = expression.replace(base_expression, is_number.group())
                bracketed = re.search("\([^()]+\)", expression)
            else:
                calc_result = parse_equation(base_expression_not_square_racket)
                if str(calc_result) and calc_result is not None:
                    # expression = re.sub(base_expression, str(calc_result), expression)
                    expression = expression.replace(base_expression, str(calc_result))
                    bracketed = re.search("\([^()]+\)", expression)
                else:
                    break
        else:
            return parse_equation(expression)


def parse_equation(expression):
    """
    解析算式，先解析乘除，再解析加减
    使用re.search查找第一个符合条件的运算，就可以保证先计算最前面的
    :param expression: 只包含加减乘除的四则运算算式
    :return: 计算结果
    """
    # 进行乘除运算时，第一个数字不能search正负号，可能会把前面加减运算的符号获取到
    multiply_or_divide_expression = re.search('\d*\.?\d*[*/][+-]?\d*\.?\d*', expression)
    while multiply_or_divide_expression:
        base_expression = multiply_or_divide_expression.group()
        calc_result = calc_expression(base_expression)
        if str(calc_result) and calc_result is not None:
            expression = expression.replace(base_expression, str(calc_result))
            # expression = re.sub(base_expression, str(calc_result), expression)
            multiply_or_divide_expression = re.search('\d*\.?\d*[*/][+-]?\d*\.?\d*', expression)
        else:
            break
    else:
        # 乘除以后先判断是否是数字，然后判断加减法
        expression = expression.replace('--', '+')
        result = re.match('^[+|-]?\d+\.?\d+([Ee][+-]?\d+)?$', expression)
        if result:
            return float(result.group())
        plus_or_minus_expression = re.search('[+-]?\d*\.?\d*[+-][+-]?\d*\.?\d*', expression)
        while plus_or_minus_expression:
            base_expression = plus_or_minus_expression.group()
            calc_result = calc_expression(base_expression)
            if str(calc_result) and calc_result is not None:
                #  failure, example: re.sub('9*2', '18', '9*2') result: '9*18' 因为会匹配2,92,992...
                # expression = re.sub(base_expression, str(calc_result), expression)
                expression = expression.replace(base_expression, str(calc_result))
                # 再次先判断是否是数字
                expression = expression.replace('--', '+')
                result = re.match('^[+|-]?\d+\.?\d+([Ee][+-]?\d+)?$', expression)
                if result:
                    return float(result.group())
                plus_or_minus_expression = re.search('[+-]?\d*\.?\d*[+-][+-]?\d*\.?\d*', expression)
            else:
                break
        else:
            # 这段代码应该运行不到
            expression = expression.replace('--', '+')
            result = re.match('^[+|-]?\d+\.?\d+([Ee][+-]?\d+)?$', expression)
            if result:
                return float(result.group())


def calc_expression(base_expression):
    """
    进行两个数的四则运算
    :param base_expression: 算术表达式，只有两个数
    :return: 计算结果
    """
    calc_operator = {
        '*': multiply,
        '/': divide,
        '+': plus,
        '-': minus
    }
    base_expression_list = re.findall("^([+-]?\d*\.?\d*)([+\-*/])([+-]?\d*\.?\d*)$", base_expression)
    if len(base_expression_list[0]) == 3:
        if base_expression_list[0][0] in ['', '.'] or base_expression_list[0][2] in ['', '.']:
            pass
        else:
            return calc_operator[base_expression_list[0][1]](base_expression_list[0][0], base_expression_list[0][2])


def multiply(multiplicand, multiplier):
    """
    乘法运算
    :param multiplicand: 被乘数
    :param multiplier: 乘数
    :return: 运算结果
    """
    return float(multiplicand) * float(multiplier)


def divide(dividend, divisor):
    """
    除法运算
    :param dividend: 被除数
    :param divisor: 除数
    :return: 运算结果
    """
    if float(divisor) == 0:
        print("除数为0")
    else:
        return float(dividend) / float(divisor)


def plus(summand, addend):
    """
    加法运算
    :param summand: 被加数
    :param addend: 加数
    :return: 运算结果
    """
    return float(summand) + float(addend)


def minus(minuend, subtrahend):
    """
    减法运算
    :param minuend: 被减数
    :param subtrahend: 减数
    :return: 运算结果
    """
    return float(minuend) - float(subtrahend)
