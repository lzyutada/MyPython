from . import employee
class Manager(employee.Employee):
    level = 0

    def __init__(self, name, salary, level):
        print("Manager::__init__")
        super(Manager, self).__init__(name, salary)
        self.level = level

    def displayEmployee(_this):
        print("Name : ", _this.name,  ", Salary: ", _this.salary, ", Level:", _this.level)
