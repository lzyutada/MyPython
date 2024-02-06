# try catch
Money = 2000
def func1() :
    try: 
        print("before invoke: ", Money)
        __AddMoney()
        print("after invoke: ", Money)
            # print("this is an indendtation error")
    except IndentationError as err:
        print("?? IndentationError: ", err)
    except BaseException as err:
        print("?? BaseException: ", err)
    else:
        print(Money)


def __AddMoney():
    # 想改正代码就取消以下注释:
    #    global Money   # using global variable
    # Money = 0      # local variable
    Money = Money + 1
