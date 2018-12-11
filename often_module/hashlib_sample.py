# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

import hashlib
import hmac

m = hashlib.md5()
m.update(b"Hello")
print(m.digest().hex())
print(m.hexdigest())
print(bytes.fromhex(m.hexdigest()))
print(m.digest())
m.update(",  世界。".encode(encoding="utf-8"))
exp1 = m.hexdigest()
print(exp1)

m2 = hashlib.md5()
m2.update("Hello, 世界。".encode(encoding="utf-8"))
exp2 = m.hexdigest()

print(exp1 == exp2)

h = hmac.new("这是密钥".encode(encoding="utf-8"), "这是要加密的消息".encode(encoding="utf-8"))
print(h.hexdigest())
