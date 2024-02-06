'''the following examples refers to: 「页面」SimplePrograms- Python Wiki  https://wiki.python.org/moin/SimplePrograms'''

# Functions
def __greet(name):
    print ('Hello', name)
def exFunc() : 
    print('\r\n\r\nFunctions')
    __greet('Jack')
    __greet('Jill')
    __greet('Bob')

# function: def
def __MyFunc1(arg1, arg2):
    print(F"this arg1={arg1}")
    print(F"this arg2={arg2}")
    pass
def __MyFunc2(arg1, arg2):
    return arg1 * arg2
def exFunc1() :
    __MyFunc1(1, [1,2,3,4,5])
    print(F"MyFunc2={__MyFunc2(2, [1,2,3,4,5])}")

# function: mutable/inmutable argumernt
def __MyFunc3(arg):
    arg = 10
def __MyFunc4(arg):
    arg.append([4, 5, 6])
def exFunc2() :
    a = 2; b = [1, 2, 3]
    print(F"a={a}"); print(F"b={b}")
    __MyFunc3(a); __MyFunc4(b)
    print(F"after MyFunc1(a), a={a}")
    print(F"after MyFunc2(b), b={b}")

# function: keyword argument(invoke with specified argument name)
# function: argument with default value
# function: with unspecified count of arguments
def __MyFunc5(a, b): print(F"a={a}, b={b}")
def __MyFunc6(a, b = "[default of 'b']"): print(F"a={a}, b={b}")
def __MyFunc7(a, *params):
    print(F"a={a}")
    for p in params : print(F"{p} of 'params'")
def __MyFunc8(a, *params): print(F"take a look at 'params': {params}")
def exFunc3() :
    # def MyFunc3(a = "[default of 'a']", b): print(F"a={a}, b={b}") # script error
    print("invoke MyFunc1")
    __MyFunc5("regular invoke", "a and b")
    __MyFunc5(b = "[arg with name as 'b']", a = "[arg with name as 'a']")
    print("invoke MyFunc2")
    __MyFunc6("[Invoke as 'MyFunc2(a)']")
    print("invoke MyFunc3")
    __MyFunc7("[this is arg('a')]", "[this is 'p1']", "[this is 'p2']", ["this", "is", "p3"])
    print("invoke MyFunc4")
    __MyFunc8("[this is arg('a')]", "[this is 'p1']", "[this is 'p2']", ["this", "is", "p3"])

# function: anonymouse function
def exFunc4() :
    sum = lambda arg1, arg2: arg1 + arg2 # lambda declaration
    print("相加后的值为 : ", sum( 10, 20 )) # lambda invoke
    print("相加后的值为 : ", sum( 20, 20 )) # lambda invoke

# function: return
def __MyFunc9(a, b): print(F"MyFunc1(): a={a}, b={b}")
def __MyFunc10(a, b): print(F"MyFunc2(): a={a}, b={b}"); return a + b
def exFunc5() :
    print("return of MyFunc1", __MyFunc9(1, 2))
    print("return of MyFunc2", __MyFunc10(1, 2))

# function: global variable / local variable
total = 0 # 这是一个全局变量
def __MyFunc11( arg1, arg2 ):
   total = arg1 + arg2 # total在这里是局部变量.
   print("函数内是局部变量 : ", total)
   return total
def exFunc6() :
    __MyFunc11( 10, 20 ) #调用sum函数
    print("函数外是全局变量 : ", total)

def exFunc7(arg1, arg2) :
    '''
    MySQL select example
    :param arg1: comment of 'arg1'
    :param arg2: comment of 'arg2'
    :returns: return an object of 'MyDto1'
    :rtype: MyDto1
    '''
    ret = MyDto1(arg1, arg2)
    ret.toString()
    return ret

class MyDto1 :
    '''
    DTO definition for 'exFunc7'
    '''
    def __init__(that, c, m) :
        that.code = c
        that.message = m
    def toString(that) : print(F"MyDto1[{that.code}|{that.message}]")
