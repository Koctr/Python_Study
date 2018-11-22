# -*- coding:utf-8 -*-
# Author: Koctr


import time


def consumer(name):
    """
    消费者
    :return:
    """
    print("%s准备吃包子了。" % name)
    while True:
        baozi = yield
        print("%s包子来了，被%s吃了。" % (baozi, name))

c = consumer("Alex")
c.__next__()

b1 = "韭菜馅"
c.send(b1)

def producer(*args):
    """
    生产者
    :return: 
    """
    c = consumer(args[0])
    c2 = consumer(args[1])
    c.__next__()
    c2.__next__()
    print("准备开始做包子了。")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半。")
        c.send(i)
        c2.send(i)

producer("Alex", "Koctr")


def fib(m):
    """
    斐波那契数列
    :return: 结果
    """
    n, a, b = 0, 0, 1
    while n < m:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# fib(10)


def fib_generator(m):
    """
    生成器模式的斐波那契数列
    :return:
    """
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib_generator(100))
f = fib_generator(10)
print('in')
print(f.__next__())
print('out')
print(f.__next__())

print("start loop")
for i in f:
    print(i)

g = fib_generator(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
