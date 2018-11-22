# -*- coding:utf-8 -*-
# Author: Koctr


class Person(object):
    """人"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sex = "normal"

    def talk(self):
        """走"""
        print("Person is talking...")


class WhitePerson(Person):
    pass


class BlackPerson(Person):
    """黑人"""
    def __init__(self, name, age, strength):
        Person.__init__(self, name, age)
        self.strength = strength
        print(self.name, self.age, self.sex)

    def talk(self):
        """走"""
        Person.talk(self)
        print("Black person is talking...")

    def walk(self):
        """说"""
        print("Black person is walking...")

p = BlackPerson("Tom", 30, "strong")
p.walk()
p.talk()
