'''the following examples refers to: 「页面」SimplePrograms- Python Wiki  https://wiki.python.org/moin/SimplePrograms'''
# Output
def exOutput():
    print('Output')
    print ('Hello, world!')
    print ('中文字符')

# Input, assignment
def exInput(): 
    name = input('What is your name?\n')
    print ('Hi, %s.' % name)

'''「页面」Python格式化输出的三种方式- 知乎  https://zhuanlan.zhihu.com/p/78346304'''
# user input & format output(refers to: runoob/python and 
def exOutput2() :
    # myinput = input("按下 enter 键退出，其他任意键显示...\n")
    # print(F"user input is: {myinput}")

    # a bulk of codes
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    if days.__len__() == 5 : 
        print("length of variable is 5")
    elif days.__len__() == 4 :
        print("length of variable is 4")
    else :
        print(F"length of variable is not 4 or 5, it's {days.__len__()}")

    a, b, c, d, e = 1, 2.5, "john", ["number", 'string', '''list''', 'tuple', 'dictionary'], {'int': 8, 'double': 16, 'string': 8}
    print(a); print(b); print(c); print(d); print(e)

# I/O, input
def exInput3() :
    str = input("please input sth. :")
    print("your input is: ", str)

# I/O, file
def exFile4() :
    fobj = open("./appdir/IO/file1", "rb+")
    fstr = fobj.read(20)
    print("read file: ", fstr)
    fobj = open("./appdir/IO/file1", "w")
    fstr = fobj.write("this is file1\r\n这是中文字符")
    print("write file: ", fstr)
