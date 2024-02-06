__PORT = 23000
def func1() :
    try:
        # get arguments
        import sys
        type = sys.argv[1:2][0] # 忽略第一个参数（脚本名称），获取剩余的参数
        if ('s' == type) :
            __server_start()
        elif ('c' == type) :
            __client_communicate()
        else :
            print("unsupported argument: ", type)
    except Exception as ex: print("func1() error: ", ex)

def __server_start() :
    '''
    start socket server
    '''
    from .serv.serv import start
    start(__PORT)
    
def __client_communicate() :
    '''
    start an instance of socket client
    '''
    from .client.client import communicate
    communicate(__PORT)