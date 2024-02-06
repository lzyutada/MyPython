from . import employee

class TempWorker(employee.Employee):
    endDate = None # datetime.date(1970, 1, 1)

    def __init__(self, name, salary, date):
        print("TempWorker::__init__")
        employee.Employee.__init__(self, name, salary)
        self.endDate = date

    def displayEmployee(_this):
        employee.Employee.displayEmployee(_this)
        print("Name : ", _this.name,  ", Salary: ", _this.salary, ", endDate:", _this.endDate)
