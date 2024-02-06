'''
test: using import by relative path.
import others
'''

from ....subdir2 import f2

def func1() : 
    print("this is 'MyTest\\MyPackage\\subdir1\\subdir1_1\\subdir1_1_1\\f1_1_1.py'")
    print("invoking subdir2\\f2.py")
    f2.func1()