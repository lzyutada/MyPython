'''the following examples refers to: 「页面」SimplePrograms- Python Wiki  https://wiki.python.org/moin/SimplePrograms'''

def exFor() : 
    # For loop, built-in enumerate function, new style formatting
    print('\r\n\r\nFor loop, built-in enumerate function, new style formatting')
    friends = ['john', 'pat', 'gary', 'michael']
    for i, name in enumerate(friends):
        print ("iteration {iteration} is {name}".format(iteration=i, name=name))

def exWhile() :
    # Fibonacci, tuple assignment
    print('\r\n\r\nFibonacci, tuple assignment')
    parents, babies = (1, 1)
    while babies < 100:
        print ('This generation has {0} babies'.format(babies))
        parents, babies = (babies, parents + babies)

# loop, a simple loop of while
def exWhile2() :
    a = 1
    while a < 10:
        print(a)
        a += 2

# loop, a bit more complex loop of while
def exWhile3() :
    numbers = [27, 36, 19, 45, 22, 30, 41]
    even = []; odd = []
    while len(numbers) > 0 :
        number = numbers.pop()
        if (number % 2): odd.append(number)
        else : even.append(number)
    print(F"even: {even}"); print(F"odd: {odd}")

# loop, while else
def exWhile4() :
    count = 0
    while count < 5:
        print (count, " is  less than 5")
        count = count + 1
    else:
        print (count, " is not less than 5")

# loop, 'for'
def exWhile5() :
    for letter in 'Python':     # 第一个实例
        print("当前字母: %s" % letter)

    fruits = ['banana', 'apple',  'mango']
    for fruit in fruits:        # 第二个实例
        print ('当前水果: %s'% fruit)

    # loop, iterator for 'for'
    for idx in range(5): print("number is", idx)
