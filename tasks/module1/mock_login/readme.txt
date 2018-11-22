博客地址：http://www.cnblogs.com/koctr/
学习笔记一——学习笔记八是第一模块的学习笔记
python学习知识库，是编写程序过程中的问题及解决办法，
地址：http://www.cnblogs.com/koctr/p/7257561.html
目前包括：
1. File "<stdin>", line 2     f.readline()     ^ IndentationError: expected an indented block
2. OSError: telling position disabled by next() call
3. TypeError: eval() arg 1 must be a string, bytes or code object
4. python模块以及导入出现ImportError: No module named ‘xxx’问题
5. expected 2 blank lines, found 0 上面需要两行空白，找到0行
6. Typo:In word 错误拼写
7. 变量、值、运算符前后应加空格，逗号后应加空格，输出字符串时应采用诸如"test%s", % name的方式，%前后要有空格

程序实现过程：
建立项目tasks，在tasks下建立目录module1，表示是模块一的程序，建立mock_login目录，表示是模拟用户登录程序
1. 模拟用户登录
   包含以下文件：
   readme.txt是程序说明。
   流程图_模拟用户登录.png是程序流程图。
   mock_login.py是程序文件，在Pycharm中运行。
   users_info保存用户信息，每一行是一个诸如{'zhangsan': ['123', 0]}形式的字典，key是用户名，列表的第一个值是密码，第二个
   值是登录错误次数。
   locked_users保存被锁定用户。

   程序按照流程图顺序执行，特殊说明如下：
   打开users_info文件后，循环读取每一行，读取一行写入新文件一行（user_info.bak)，直到所有行循环完毕才能确定用户是否存在，
   如果用户密码错误，修改这一行的用户密码错误次数，写入新文件

   在Pycharm中运行程序

测试用例：
输入3次不存在的用户，退出
同一用户三次登录失败，锁定，退出
不同用户三次登录失败，允许继续登录，直到其中一个用户达到三次登录失败时锁定退出
用户登录成功后，登录失败次数设置为0

zhangsan 123 0 0
lisi 123 0 0
wangwu 123 0 0
Alex 123 0 0


