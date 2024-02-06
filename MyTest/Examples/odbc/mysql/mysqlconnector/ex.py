
'''
installation: pip install mysqlclient
-- import MySQLdb

install mysql module: python -m pip install mysql-connector,
-- for python3
-- import mysql.connector
「页面」PythonMySQL – mysql-connector 驱动 | 菜鸟教程  https://www.runoob.com/python3/python-mysql-connector.html
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

import MyModule.myconfig

def __getConnectInfo() :
    '''get DB connection info'''
    ret = None
    cfg = MyModule.myconfig.getConfig() # read from config
    target_elem = None # 找到 dbinfo 中 infoname 为 'dbinfo1' 的元素
    for elem in cfg.get('dbinfo', []):
        if elem.get('infoname') == 'dbinfo1': target_elem = elem; break
    if target_elem:
        host = target_elem.get('host'); user = target_elem.get('user'); password = target_elem.get('password'); dbname = target_elem.get('dbname')
        ret = MySqlConnInfo(host, user, password, dbname)
    else :
        ret = MySqlConnInfo()
    return ret


# MySQL, connect to DB
def func1() :
    import MySQLdb
    cfg = __getConnectInfo() # read from config
    db = MySQLdb.connect(cfg.host, cfg.username, cfg.password, cfg.dbname, charset='utf8' ) # 打开数据库连接
    cursor = db.cursor() # 使用cursor()方法获取操作游标 
    cursor.execute("SELECT VERSION()") # 使用execute方法执行SQL语句
    data = cursor.fetchone() # 使用 fetchone() 方法获取一条数据
    print("Database version : %s " % data )
    db.close() # 关闭数据库连接

# MySQL, create table
def func2() :
    import MySQLdb
    tmpTableName = "DocList"; tmpTableComment = "document list"
    columns = """
    DocId           INT             AUTO_INCREMENT  PRIMARY KEY     COMMENT '(PK) document id',
    DataSourceId    INT             NOT NULL        DEFAULT '0'     COMMENT 'data source id, where to get the doc.',
    DocName         VARCHAR(4000)   NOT NULL        DEFAULT ''      COMMENT 'doc name',
    DataSrcLink     VARCHAR(4000)   NOT NULL        DEFAULT ''      COMMENT 'link of doc',
    AddTime         DATETIME        NOT NULL        COMMENT 'add time',
    AddDate         DATE            NOT NULL        COMMENT 'add date',
    LastTime        DATETIME        NOT NULL        COMMENT 'latest update time',
    LastDate        DATE            NOT NULL        COMMENT 'latest update date',
    IsDel           INT             NOT NULL        DEFAULT '0'     COMMENT 'deleted status',
    Remark          VARCHAR(4000)   NOT NULL        DEFAULT ''      COMMENT 'remark',
    Disorder        INT             NOT NULL        DEFAULT '0'     COMMENT 'disorder'
    """

    db = MySQLdb.connect("192.168.3.101", "pro_py", "FT*26G@njfBPEZdq", "mydb", charset='utf8' ) # 打开数据库连接
    cursor = db.cursor() # 使用cursor()方法获取操作游标 
    cursor.execute(F"DROP TABLE IF EXISTS {tmpTableName}") # 如果数据表已经存在使用 execute() 方法删除表。
    # 创建数据表SQL语句
    sql = F"""CREATE TABLE {tmpTableName} (
            {columns} ) COMMENT='{tmpTableComment}'"""
    cursor.execute(sql)
    db.close()      #关闭数据库连接

# MySQL, insert
def func3(f = 1) : 
    '''
    insert row
    :param f: insert a row with fixed 'DocName' and 'DataSrcLink'
    '''
    import MySQLdb
    from datetime import datetime
    import time
    cfg = __getConnectInfo() # read from config
    timedes = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]; datedes = datetime.now().strftime('%Y-%m-%d')
    ticks = int(time.time()) if 0 == f else 0

    db = MySQLdb.connect(cfg.host, cfg.username, cfg.password, cfg.dbname, charset='utf8' ) # 打开数据库连接
    try:
        cursor = db.cursor() # 使用cursor()方法获取操作游标 

        # SQL, insert one row
        sql = "INSERT INTO `doclist`(`DataSourceId`, \
                `DocName`, \
                `DataSrcLink`, \
                `AddTime`, \
                `AddDate`, \
                `LastTime`, \
                `LastDate`, \
                `IsDel`, \
                `Remark`, \
                `Disorder`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = ('1', F'Sample Document{ticks}', F'http://example{ticks}.com/sample', timedes, datedes, timedes, datedes, '0', 'This is a test document', '0')
        cursor.execute(sql, val) # 执行sql语句
        db.commit()         # 提交到数据库执行
    except BaseException as ex:
        print(F"DB error: {ex}")
        db.rollback()   # 发生错误时回滚
    db.close()      # 关闭数据库连接

# MySQL, insert rows
def func4(f = 1) :
    '''
    insert rows
    :param f: insert a row with fixed 'DocName' and 'DataSrcLink'
    '''
    import mysql.connector
    import time
    from datetime import datetime

    cfg = __getConnectInfo() # read from config
    ticks = int(time.time()) if 0 == f else 0
    timedes = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]; datedes = datetime.now().strftime('%Y-%m-%d')
    try:
        db = mysql.connector.connect(
            host = cfg.host, 
            user = cfg.username,
            passwd = cfg.password,
            database = cfg.dbname) # 打开数据库连接
        cursor = db.cursor() # 使用cursor()方法获取操作游标 

        # SQL, insert multiple rows
        sql = "INSERT INTO `doclist`(`DataSourceId`, \
                `DocName`, \
                `DataSrcLink`, \
                `AddTime`, \
                `AddDate`, \
                `LastTime`, \
                `LastDate`, \
                `IsDel`, \
                `Remark`, \
                `Disorder`) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        i = 0; vals = []
        while  i < 5: 
            name = F'Sample Document{i}-{ticks}'
            link = F'http://example{i}-{ticks}.com/sample'
            vals.append((i % 2, name, link, timedes, datedes, timedes, datedes, '0', 'This is a test document', '0'))
            i += 1
        # print(vals)
        cursor.executemany(sql, vals)
        db.commit()         # 提交到数据库执行
        db.close()          # no close using mysql.connector
    except BaseException as ex: print(F"DB error: {ex}")


# MySQL, select
def func5() : 
    '''
    MySQL select example
    '''
    import mysql.connector
    try :
        cfg = __getConnectInfo() # read from config
        mydb = mysql.connector.connect(
            host = cfg.host, 
            user = cfg.username,
            passwd = cfg.password,
            database = cfg.dbname)
        mycursor = mydb.cursor()
        # mycursor.execute("SELECT * FROM doclist WHERE DataSourceId = 0") # select all columns
        mycursor.execute("SELECT DocId, DocName, DataSrcLink FROM doclist WHERE DataSourceId = 0") # select specified columns
        # myresult = mycursor.fetchall()     # fetchall() 获取所有记录
        myresult = mycursor.fetchone()     # select 1 row
        for x in myresult:
            print(x)
    except Exception as err: print("Exception: ", err)
    except BaseException as err: print("BaseException: ", err)
    finally : pass
