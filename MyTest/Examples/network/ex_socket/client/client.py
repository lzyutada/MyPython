'''
socket client
refers to: https://www.runoob.com/python3/python3-socket.html
'''

def communicate(p) :
    '''
    connect to socket server, send and receive stream from server
    :param p: socket port
    '''
    try:
        # 导入 socket、sys 模块
        import socket
        import sys
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 创建 socket 对象
        host = socket.gethostname()                             # 获取本地主机名
        port = p                                             # 设置端口号
        s.connect((host, port))                                 # 连接服务，指定主机和端口
        msg = s.recv(1024)                                      # 接收小于 1024 字节的数据
        s.close()
        print (msg.decode('utf-8'))
    except Exception as ex: print("socket client communicate() error: ", ex)


