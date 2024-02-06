'''the following examples refers to: 「页面」SimplePrograms- Python Wiki  https://wiki.python.org/moin/SimplePrograms'''

# about string
def exString1() :
    des = "1234567890"
    print(F"length of des is {des.__len__()}")
    print(F"{des}[2:4] is {des[2:4]}")
    print(F"{des}[0:4] is {des[0:4]}")
    print(F"{des}[2:-2] is {des[2:-2]}")
    print(F"{des}[-3:-1] is {des[-3:-1]}")
    print(F"{des}[-5:-3] is {des[-5:-3]}")
    
# about string
def exString2() :
    str = 'Hello World!'
    print(F"{str}, *2 is is {str * 2}")
    print(F"{str}, + 'TEST' is {str + "TEST"}")
    int = 2
    print(F"{int}, *2 is is {int * 2}")
    print(F"{int}, + 'TEST' is {int.__str__() + "TEST"}")
