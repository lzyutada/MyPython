'''
examples for 'pymysql'
refers to: https://www.runoob.com/python3/python3-mysql.html
'''

class MySqlConnInfo :
    def __init__(that) :
        '''default constructor'''
        that.host = ""
        that.username = ""
        that.password = ""
        that.dbname = ""

    def __init__(that, h, u, p, n) :
        '''construct with arguments'''
        that.host = h
        that.username = u
        that.password = p
        that.dbname = n

def getConnectInfo() :
    '''get DB connection info'''
    ret = None
    cfg = __getConfig() # read from config
    target_elem = None # 找到 dbinfo 中 infoname 为 'dbinfo1' 的元素
    for elem in cfg.get('dbinfo', []):
        if elem.get('infoname') == 'dbinfo1': target_elem = elem; break
    if target_elem:
        host = target_elem.get('host'); user = target_elem.get('user'); password = target_elem.get('password'); dbname = target_elem.get('dbname')
        ret = MySqlConnInfo(host, user, password, dbname)
    else :
        ret = MySqlConnInfo()
    return ret

import json
def __getConfig():
    # 读取并解析 mytest.config.json 中的内容
    with open('./config/mytest.config.json', 'r') as file: cfgObj = json.load(file)
    return cfgObj

# def __func1() :
#     '''connect to MySQL'''
#     import pymysql
#     cfg = __getConnectInfo() # read from config
#     db = pymysql.connect(
#         host = cfg.host,
#         user = cfg.username,
#         password = cfg.password,
#         database = cfg.dbname
#         )  # 打开数据库连接
#     cursor = db.cursor()                # 使用 cursor() 方法创建一个游标对象 cursor
#     cursor.execute("SELECT VERSION()")  # 使用 execute()  方法执行 SQL 查询 
#     data = cursor.fetchone()            # 使用 fetchone() 方法获取单条数据.
#     db.close()                          # 关闭数据库连接
#     print ("Database version : %s " % data)

# def __func2() :
#     '''insert row'''
#     import pymysql
#     import time
#     from datetime import datetime
#     try:
#         cfg = __getConnectInfo() # read from config
#         db = pymysql.connect(host = cfg.host, user = cfg.username, password = cfg.password, database = cfg.dbname)  # 打开数据库连接
#         cursor = db.cursor()    # 使用cursor()方法获取操作游标 
#         f = 0; ticks = int(time.time()) if 0 == f else 0
#         timedes = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]; datedes = datetime.now().strftime('%Y-%m-%d')
#         # SQL 插入语句
#         sql = "INSERT INTO `doclist`(`DataSourceId`, \
#                 `DocName`, \
#                 `DataSrcLink`, \
#                 `AddTime`, \
#                 `AddDate`, \
#                 `LastTime`, \
#                 `LastDate`, \
#                 `IsDel`, \
#                 `Remark`, \
#                 `Disorder`) \
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#         val = ('3', F'Sample Document{ticks}', F'http://example{ticks}.com/sample', timedes, datedes, timedes, datedes, '0', 'This is a test document', '0')
#         try:
#             cursor.execute(sql, val) # 执行sql语句
#             db.commit()         # 提交到数据库执行
#         except Exception as ex:
#             print("func2()::DB error: ", ex)
#             db.rollback()       # 如果发生错误则回滚
#         db.close()              # 关闭数据库连接
#     except Exception as ex: print("func2() error: ", ex)
