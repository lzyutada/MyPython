
import json

def getConfig():
    # 读取并解析 mytest.config.json 中的内容
    with open('./config/mytest.config.json', 'r') as file: cfgObj = json.load(file)
    return cfgObj