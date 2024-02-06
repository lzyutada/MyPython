from MyPackage.subdir1.subdir1_1 import employee, manager, tempworker, myclass1, f1_1
import datetime

def func1() :
    try:
        em1 = employee.Employee("Jhon", 120000)
        em2 = employee.Employee("Alterman", 1700000)
        em1.displayCount()
        em1.displayEmployee()
        em2.displayEmployee()
        print("hasattr('Age')", hasattr(em1, "Age"))
        # getattr(em1, "Age") # will throw an exception
        print("hasattr('Name')", hasattr(em1, "Name"))
        print("hasattr('name')", hasattr(em1, "name"))
        attr = getattr(em1, "name")
        print("getattr('name')", attr)
        setattr(em1, "name", "Senshkiv")
        em1.displayEmployee()
    except BaseException as ex:
        print("exception, ", ex)
    finally:
        print("Employee.__doc__:", em1.__doc__)
        # print("Employee.__ne__:", em1.__ne__)
        print("Employee.__module__:", em1.__module__)
        print("Employee.__class__:", em1.__class__)
        print("Employee.__dict__:", em1.__dict__)
    pass

# class, inherit
def func2() :
    try:
        em1 = manager.Manager("Jhon", 120000, 14)
        em1.displayCount()
        em1.displayEmployee()

        em2 = tempworker.TempWorker("Bill", 90000, datetime.date(2050, 8, 31))
        em2.displayCount()
        em2.displayEmployee()
    except BaseException as err:
        print("exception: ", err)
    finally:
        pass

# class, private method
def func3() :
    try:
        em1 = myclass1.MyClass1()
        em1.myPublicFunc()
        em1.invokePrivateFunc()
        em1.__myPrivateFunc()
    except BaseException as err:
        print("exception: ", err)
    finally:
        pass
