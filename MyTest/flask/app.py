'''
app.py
practice on flask
'''

from flask import Flask

app = Flask(__name__)
@app.route("/")

def _odbc_mongodb_ex() : 
    # from MyPackage.Example.odbc.mongodb.ex import import_module
    # # import MyPackage.Example.odbc.mongodb.ex
    # retList = []
    # tmpMsg = import_module()
    # retList.append(tmpMsg)
    from MyPackage.mypmodule1 import MyPFunc1
    retList = MyPFunc1()
    return retList

def run() :
    respDes = ""
    msgDes = ""
    msgList = _odbc_mongodb_ex()
    for i, msg in enumerate(msgList):
        msgDes = F"""{msgDes}
<div>{i} - {msg}</div>
"""
    respDes = F'<div style="display: flex; flex-direction: column;">{msgDes}</div>'
    return respDes
