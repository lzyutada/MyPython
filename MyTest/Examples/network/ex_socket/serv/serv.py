'''
socket server
refers to: https://www.runoob.com/python3/python3-socket.html
'''

def start(p) :
    '''
    start socket server, ready to recieve connecting from clients.
    :param p: socket port
    '''
    try:
        # 导入 socket、sys 模块
        import socket
        import sys

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # 创建 socket 对象
        host = socket.gethostname()         # 获取本地主机名
        port = p
        serversocket.bind((host, port))     # 绑定端口号
        serversocket.listen(3)              # 设置最大连接数，超过后排队
        while True:
            clientsocket,addr = serversocket.accept()   # 建立客户端连接
            print("连接地址: %s" % str(addr))
            msg = '欢迎访问菜鸟教程！'+ "\r\n"
            clientsocket.send(msg.encode('utf-8'))
            clientsocket.close()
    except Exception as ex: print("socket server staRT() error: ", ex)
