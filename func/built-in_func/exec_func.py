# -*- encoding:utf-8 -*-
# Author: Koctr

code = '''
def foo():
    print("in the foo")

    def bar():
        print("in the bar")
    bar()


foo()
'''

print("exec: ")
exec(code)
