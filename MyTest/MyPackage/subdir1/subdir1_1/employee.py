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
