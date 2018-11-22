# -*- encoding:utf-8 -*-
# Author: Koctr
i = 100
print("bin(x: x>0): ", bin(i))
i = -100
print("bin(x: x<0): ", bin(i))
print("bin(prefix '0b'): ", format(i, '#b'))
print("bin(not prefix '0b'): ", format(i, 'b'))
print("simple format bin:", f'{i:#b}', f'{i:b}')
