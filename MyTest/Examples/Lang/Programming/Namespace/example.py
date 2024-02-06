'''the following examples refers to: 「页面」Python基础语法 | 菜鸟教程  https://www.runoob.com/python/python-basic-syntax.html'''

# 命名空间和作用域
Money = 2000
def AddMoney():
#    global Money   # using global variable
#    Money = 0      # local variable, 想改正代码就取消注释
   Money = Money + 1
print(Money)
AddMoney()
print(Money)
