'''the following examples refers to: 「页面」Python基础语法 | 菜鸟教程  https://www.runoob.com/python/python-basic-syntax.html'''

# member operator
def exOperator1() :
    a = 10; list = [1, 2, 3, 4, 5 ]
    if ( a in list ):
        print("变量 a 在给定的列表中 list 中")
    else:
        print("变量 a 不在给定的列表中 list 中")
        
    isin = a in list
    if isin:
        print("(isin)变量 a 在给定的列表中 list 中")
    else:
        print("(isin)变量 a 不在给定的列表中 list 中")
