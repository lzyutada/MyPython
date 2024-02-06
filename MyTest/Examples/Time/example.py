'''the following examples refers to: 「页面」Python基础语法 | 菜鸟教程  https://www.runoob.com/python/python-basic-syntax.html'''

# try time
import time
def exTime() :
    print(time.time())
    print(time.localtime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) # 格式化成Sat Mar 28 22:24:24 2016形式
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))) # 将格式字符串转换为时间戳
