# -*- coding:utf-8 -*-
# Author: Koctr


# 模拟cs游戏，类的成员属性、私有属性、公有属性


class Role(object):
    """CS角色"""

    # 公有属性，国籍
    nationality = "JP"

    def __init__(self, name, role, weapon, life_value=100, money=15000):
        # 成员属性，内部外部可见
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        # 私有属性，内部可见
        self.__heart = "Normal"

    def shot(self):
        """射击，公有方法"""
        print("%s is shooting." % self.name)

    def got_shot(self):
        """中枪"""
        print("Ah..., I got shot...")
        self.__heart = "Die"
        print(self.__heart)

    def get_heart(self):
        """访问私有属性的方法"""
        return self.__heart

    def buy_gun(self, gun_name):
        """买枪"""
        self.weapon = gun_name
        print("%s just bought %s." % (self.name, gun_name))

r1 = Role("Alex", "Police", "AK47")
r2 = Role("Jack", "terrorist", "B22")

r1.shot()

r2.buy_gun("B46")
print(r2.weapon)

r2.got_shot()
print(r2.get_heart())

# 特殊的访问私有属性的方法
print(r1._Role__heart)

# 修改公有属性
Role.nationality = "US"
print(r1.nationality)
print(r2.nationality)

# 只创建了一个同名的成员属性
r1.nationality = "China"
Role.nationality = "JP"
# 仍然为China，因为调用的是自己的成员属性，所以调用方式应该为Role.nationality
print(r1.nationality)
print(r2.nationality)
print(Role.nationality)


def shot2(self):
    """"模拟一个私有方法"""
    print("%s Run this method" % self.name)


r1.shot = shot2
r1.shot(r1)
