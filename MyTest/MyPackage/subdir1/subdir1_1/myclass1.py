'''private method'''
class MyClass1:
    pass

    def __init__(self): pass

    def myPublicFunc(self): print("this is public method")

    def __myPrivateFunc(self): print("this is private method")

    def invokePrivateFunc(self): self.__myPrivateFunc()
