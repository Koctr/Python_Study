# -*- encoding:utf-8 -*-
# Author: Koctr


from core import main
from conf import settings


def run():
    # 商品列表文件包含商品名称、价格、数量三项内容
    # 商品字典，名称为key，值为[价格, 数量]
    product_file = '%s/shopping_mall/products' % settings.BASE_DIR
    product_dict = dict()
    with open(product_file, 'r', encoding='utf-8') as products:
        for line in products:
            product = line.split(', ')
            product[1] = int(product[1])
            product[2] = int(product[2])
            product_dict[product[0]] = [product[1], product[2]]

    exit_flag = False
    # 已购商品
    item_dict = dict()
    while not exit_flag:
        """
        1.打印商品列表，请求输入要购买的商品和数量
        1.1 如果输入exit，判断购物车是否为空
        1.1.1 是，打印已购列表，退出
        1.1.2 否，打印购物明细，退出
        1.2 否则：判断输入是否正确
        1.2.1 是：调用ATM的消费接口结算，判断结算是否成功
        1.2.1.1 是，将商品加入已购字典
        1.2.1.2 否，无操作
        1.2.2 否：打印错误信息，从1开始循环
        """
        print('\33[33;1m商品列表（序号、名称、价格、库存数量）：\33[0m')
        product_index = 0
        product_list = sorted(product_dict)
        for product in product_list:
            product_index += 1
            print(product_index, product, product_dict[product][0], product_dict[product][1])
        user_choice = input('\33[33;1m输入编号和数量（以逗号分隔）将商品加入购物车，输入exit退出购物：\33[0m').strip()
        if user_choice == 'exit':
            if item_dict:
                print("\33[42;1m已购商品为：\33[0m")
                for item in item_dict:
                    print(item, item_dict[item][0], item_dict[item][1])
            exit_flag = True
        else:
            user_choice_list = user_choice.split(',')
            if len(user_choice_list) != 2:
                print('\33[31;1m输入格式不正确\33[0m')
            else:
                if user_choice_list[0].isdigit() and 1 <= int(user_choice_list[0]) <= len(product_dict):
                    item_index = int(user_choice_list[0])
                    product_name = product_list[item_index - 1]
                    inventory_amount = product_dict[product_name][1]
                    if user_choice_list[1].isdigit() and 0 < int(user_choice_list[1]) <= inventory_amount:
                        item_amount = int(user_choice_list[1])
                        amount = product_dict[product_name][0] * item_amount
                        if main.consume(amount):
                            if product_name in item_dict:
                                item_dict[product_name][1] += item_amount
                            else:
                                item_dict[product_name] = [product_dict[product_name][0], item_amount]
                            product_dict[product_name][1] -= item_amount
                    else:
                        print('\33[31;1m商品数目 [%s] 不正确\33[0m' % user_choice_list[1])
                else:
                    print('\33[31;1m所选商品 [%s] 不在商品列表中\33[0m' % user_choice_list[0])

    with open(product_file, 'w', encoding='utf-8') as products:
        for product in product_dict:
            line = ', '.join([product, str(product_dict[product][0]), str(product_dict[product][1])])
            products.writelines(line + '\n')
