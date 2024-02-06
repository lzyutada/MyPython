'''the following examples refers to: 「页面」Python基础语法 | 菜鸟教程  https://www.runoob.com/python/python-basic-syntax.html'''

# try math
def exMath1() :
    # import math
    positive = 2; nagetive = -2
    print(F"{positive} equals to {nagetive}: {positive == nagetive}")
    print(F"abs({positive}) equals to abs({nagetive}): {abs(positive) == abs(nagetive)}")

import math
def exMath2() :
    # print(ceil(1.2)) # script error
    print(math.ceil(1.2)) # output: 2
