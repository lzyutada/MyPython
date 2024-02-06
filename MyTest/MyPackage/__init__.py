'''
this is a package('MyPackage\') for test
文件夹下必须存在 __init__.py 文件
__init__.py 用于标识当前文件夹是一个包
'''

print('__init__.py in "MyPackage"')
if __name__ == '__main__':
    print('作为主程序运行')
else:
    print('package(MyPackage) 初始化')