'''the following examples refers to: 「页面」SimplePrograms- Python Wiki  https://wiki.python.org/moin/SimplePrograms'''

# datatype, dictionary
def exDictionary1() :
    print('\r\n\r\nDictionaries, generator expressions')
    prices = {'apple': 0.40, 'banana': 0.50}
    my_purchase = {
        'apple': 1,
        'banana': 6}
    grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                    for fruit in my_purchase)
    print ('I owe the grocer $%.2f' % grocery_bill)
    for fruit in my_purchase:
        print(fruit)

# about dictionary
def exDictionary2() :
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two" 
    tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}
    print (dict['one'])          # 输出键为'one' 的值
    print (dict[2])              # 输出键为 2 的值
    print (tinydict)             # 输出完整的字典
    print (tinydict.keys())      # 输出所有键
    print (tinydict.values())    # 输出所有值
    # print (dict['This is one'])    # 查找value, error with 'KeyError'
