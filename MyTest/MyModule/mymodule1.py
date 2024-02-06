'''this is a module for test'''
import datetime

mm_country = 'Republic of Moldova'
def mmFunc1(): _countries= [mm_country]; _countries.append("Ukriane"); return _countries
def mmFunc2(): print("this is MyModule.mymodule1.Func2()")

'''class and inherit'''
class Employee:
    '所有员工的基类'
    empCount = 0

    # 构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    # self代表类的实例，而非类, 'self'不是关键字
    def __init__(self, name, salary):
        print("Employee::__init__")
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

class Manager(Employee):
    level = 0

    def __init__(self, name, salary, level):
        print("Manager::__init__")
        super(Manager, self).__init__(name, salary)
        self.level = level

    def displayEmployee(_this):
        print("Name : ", _this.name,  ", Salary: ", _this.salary, ", Level:", _this.level)

class TempWorker(Employee):
    endDate = None # datetime.date(1970, 1, 1)

    def __init__(self, name, salary, date):
        print("TempWorker::__init__")
        Employee.__init__(self, name, salary)
        self.endDate = date

    def displayEmployee(_this):
        Employee.displayEmployee(_this)
        print("Name : ", _this.name,  ", Salary: ", _this.salary, ", endDate:", _this.endDate)

'''private method'''
class MyClass1:
    pass

    def __init__(self): pass

    def myPublicFunc(self): print("this is public method")

    def __myPrivateFunc(self): print("this is private method")

    def invokePrivateFunc(self): self.__myPrivateFunc()
