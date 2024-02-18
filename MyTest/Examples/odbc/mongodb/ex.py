"""
this is a test .py for mongodb examples
can be imported with local project.
using MyPackage.Example.odbc.mongodb.ex when coding in codespace.
"""

class MyMongoDbInfo :
    host="192.168.3.101:27017/"
    username="user"
    pwd="user"

import loghelper.loghelper
logger = loghelper.loghelper.get_logger()

def import_module(): 
    """
    import module(pymongo)
    """
    import pymongo
    return "1 - import pymongo ok."

def create_db(): 
    """
    connect to exist db or create a new one
    """
    import pymongo
    dbclient = pymongo.MongoClient(F"mongodb://{MyMongoDbInfo.username}:{MyMongoDbInfo.pwd}@{MyMongoDbInfo.host}")
    mydb = dbclient["mydb"]
    return F"2 - connect to server ok. mydb={mydb}"

def create_collection(): 
    """
    get or create a collection
    """
    import pymongo
    dbclient = pymongo.MongoClient(F"mongodb://{MyMongoDbInfo.username}:{MyMongoDbInfo.pwd}@{MyMongoDbInfo.host}")
    mydb = dbclient["mydb"]
    coll1 = mydb["mydb"]
    return F"3 - get collection: {coll1}"

def is_exist_collection(): 
    """
    if a collection exist or not
    """
    # try: 
    import pymongo
    dbclient = pymongo.MongoClient(F"mongodb://admin:admin@192.168.3.101:27017/")
    # dbclient = pymongo.MongoClient(F"mongodb://{MyMongoDbInfo.username}:{MyMongoDbInfo.pwd}@{MyMongoDbInfo.host}")
    mydb = dbclient["mydbdel"]
    logger.debug(F"mydbdel={mydb}")
    collist = mydb.list_collection_names()
    logger.debug(F"collist={collist}")
    if "dummycoll" in collist:
        return F"4 - collection[dummycoll] exist"
    else : 
        return F"4 - collection[dummycoll] not exist"
    # except BaseException as err:
    #     return F"4 - collection[dummycoll] exist exception: {err}"

def insert_one(): 
    """
    insert one row.
    """
    import uuid
    import pymongo
    _id = str(uuid.uuid4())
    # dbclient = pymongo.MongoClient(F"mongodb://{MyMongoDbInfo.username}:{MyMongoDbInfo.pwd}@{MyMongoDbInfo.host}")
    # dbclient = pymongo.MongoClient(F"mongodb://user:user@192.168.3.101:27017/?authSource=mydb", serverSelectionTimeoutMS=3000, socketTimeoutMS=3000)
    dbclient = pymongo.MongoClient(
        host="192.168.3.101", # 主机
        port=27017, # 端口
        username="user", # 用户名
        password="user", # 密码
        authSource="mydb" # 需要用户名和密码进行身份认证的数据库
    )
    mydb = dbclient["mydb"]; logger.debug(F"mydb={mydb}")
    mycol = mydb["mydb"]; logger.debug(F"mycol={mycol}")
    ret = mycol.insert_one({"name": "insert one by pro"}) 
    return ret
