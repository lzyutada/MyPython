'''the following examples refers to: 「页面」Python基础语法 | 菜鸟教程  https://www.runoob.com/python/python-basic-syntax.html'''

# one programing statement in multiple lines
def example1() :
    item_one = "part1"; item_two = "part2"; item_three = "part3"
    total = item_one + \
            item_two + \
            item_three
    print(total)

# no need charactor backslash('\')
def example2() :
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    print(days)

# condition statement, 'if else'
def exConditionStatement1() : 
    flag = False
    name = 'luren'
    if name == 'python':         # 判断变量是否为 python 
        flag = True              # 条件成立时设置标志为真
        print('welcome boss')     # 并输出欢迎信息
    else:
        print(name)               # 条件不成立时输出变量名称

# condition statement, 'if elif else'
def exConditionStatement2() :
    num = 5     
    if num == 3:            # 判断num的值
        print ('boss')
    elif num == 2:
        print ('user')
    elif num == 1:
        print ('worker')
    elif num < 0:           # 值小于零时输出
        print ('error')
    else:
        print ('roadman')     # 条件均不成立时输出

# condition statement, multiple conditions, 'if cond1 and cond2 or cond3 and (cond4 or cond5)
def exConditionStatement3() :
    num = 9
    if num >= 0 and num <= 10:    # 判断值是否在0~10之间
        print( 'hello') # 输出结果: hello
    
    num = 10
    if num < 0 or num > 10:    # 判断值是否在小于0或大于10
        print ('hello')
    else:
        print('undefine') # 输出结果: undefine

    num = 8 # 判断值是否在0~5或者10~15之间
    if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    
        print('hello')
    else:
        print('undefine') # 输出结果: undefine

# condition statement, another style of coding
def exConditionStatement4() :
    var = 100
    if ( var  == 100 ) : print ("变量 var 的值为100" )
    print( "Good bye!")
    var = 80
    if ( var  == 100 ) : print ("变量 var 的值为100" )
    print( "Good bye!")
