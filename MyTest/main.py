'''the following examples refers to: 「页面」SimplePrograms- Python Wiki  https://wiki.python.org/moin/SimplePrograms'''

'''the following examples refers to: 「页面」Python基础语法 | 菜鸟教程  https://www.runoob.com/python/python-basic-syntax.html'''
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
'''the following examples refers to: 「页面」Python基础语法 | 菜鸟教程  https://www.runoob.com/python/python-basic-syntax.html'''

import loghelper.loghelper
logger = loghelper.loghelper.get_logger()

from flask import Flask

app = Flask(__name__)
@app.route("/")

def run() :
    respDes = ""; msgDes = ""
    msgList = __odbc_mongodb_ex()
    for msg in msgList:
        logger.debug(F"msg={msg}")
        msgDes = F"""{msgDes}<div>{msg}</div>"""
    respDes = F'<div style="display: flex; flex-direction: column;max-width: 600px; margin: 0 auto;">{msgDes}</div>'
    
    logger.debug(F"respDes={respDes}\r\nmsgDes={msgDes}")
    return respDes

if __name__=="__main__":
    app.run()#运行，启动程序

def __odbc_mongodb_ex() : 
    from Examples.odbc.mongodb.ex import import_module, create_db, create_collection, is_exist_collection, insert_one
    retList = []
    # tmpMsg = import_module()
    # retList.append(tmpMsg)
    # logger.debug(F"import_module finished")
    
    # tmpMsg = create_db()
    # retList.append(tmpMsg)
    # logger.debug(F"create_db finished")

    # tmpMsg = create_collection()
    # retList.append(tmpMsg)
    # logger.debug(F"create_collection finished")

    # tmpMsg = is_exist_collection()
    # retList.append(tmpMsg)
    # logger.debug(F"is_exist_collection finished")

    tmpMsg = insert_one()
    retList.append(tmpMsg)
    logger.debug(F"insert_one finished")

    return retList

# from Examples.DataType.List.example import exList1
# exList1()

# import queue
# workQueue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# while 1:
#     _input = input("""press 'Enter' to process one from list\n
# press 'q' to exit.\n
# """)
#     if ('q' == _input or 'Q' == _input) : print("bye"); break
#     else :
#         data = workQueue.get()
#         print("when you input '%s', processing: %d" % (_input, data))
