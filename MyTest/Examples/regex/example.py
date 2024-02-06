'''the following examples refers to: 「页面」SimplePrograms- Python Wiki  https://wiki.python.org/moin/SimplePrograms'''

import re
# Import, regular expressions
def func1() :
    print('\r\n\r\nImport, regular expressions')
    for test_string in ['555-1212', 'ILL-EGAL']:
        if re.match(r'^\d{3}-\d{4}$', test_string):
            print (test_string, 'is a valid US local phone number')
        else:
            print (test_string, 'rejected')

# Import, regular expressions
def func2() :
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

# regular express
def func3() :
    p = r"^\d{6}(\d{4})(\d{2})(\d{2})\d{2}(\d)(\w)" # idno p, take a look at 'r"^...'
    d1 = "211221200108072110"; d2 = "211221200108072110123456789"; d3 = "0123456789" # des to be matched.
    # re.match
    m1 = re.match(p, d1); m1f = re.match(p, d1, flags=re.IGNORECASE); m2 = re.match(p, d2); m3 = re.match(p, d3)
    print("1.1 ", m1)
    print("1.2 ", m1f)
    print("1.3 ", m2)
    print("1.4 ", m3)

#re.group/re.groups
def func4() :
    d2 = "Experiment in the playground" # "Experiment in the playground. Experiment in the playground" try this??
    p1 = r"i(.*?)gr(.*)" # partition1
    p2 = "th" # partitioin2
    p3 = r"^(.*?)e(.*)" # partitioin3
    p4 = r"^(.*)e(.*)" # partitioin3
    # des to be matched.
    m1 = re.match(p1, d2)   # 只匹配字符串的开始
    m2 = re.search(p1, d2)  # 匹配整个字符串，直到找到一个匹配
    m3 = re.search(p3, d2, re.IGNORECASE)
    m4 = re.search(p4, d2, re.IGNORECASE)
    if m1 : print("2.1 ", m2.group(0), m1.groups())
    else : print("2.1", "no match")
    if m2 : print("2.2 ", m2.group(0), m2.groups())
    else : print("2.2", "no match")
    if m3 : print("2.3 ", m3.group(0), m3.groups())
    else : print("2.3", "no match")
    if m4 : print("2.4 ", m4.group(0), m4.groups())
    else : print("2.4", "no match")

# re, re.sub/refl
d = "IDCNO of client was '211221200108072110' was incorrect, his IDCNO was '211224200408037041'. '211221200108072110' should be replaced with '211224200408037041'"
dd = "'211221200108072110' was incorrect, his IDCNO was '211224200408037041', '211221200108072110' should be replaced with '211224200408037041'."
p1 = r"([1-6][1-9]|50)\d{4}(18|19|20)\d{2}((0[1-9])|10|11|12)(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]" # idno p, take a look at 'r"^...'

def __re_sub_refl(matched):
    matchedDes = matched.group()
    return matchedDes[:3] + "****" + matchedDes[-3:]

def func5() :
    tmp = dd
    num0 = re.sub(p1, "****", tmp, 0); print("3.1", "num=", num0)
    num0 = re.sub(p1, __re_sub_refl, tmp, 0); print("3.2", "num=", num0)
    num0 = re.sub(p1, "****", tmp, 1); print("3.3", "num=", num0)
    num0 = re.sub(p1, "****", tmp, 2); print("3.4", "num=", num0)
    num0 = re.sub(p1, __re_sub_refl, tmp, 2); print("3.5", "num=", num0)

# re, compile
def func6() :
    d = "IDCNO of client was '211221200108072110' was incorrect, his IDCNO was '211224200408037041'. '211221200108072110' should be replaced with '211224200408037041'"
    patterndes = r"([1-6][1-9]|50)\d{4}(18|19|20)\d{2}((0[1-9])|10|11|12)(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]"
    p = re.compile(patterndes, re.U)
    print("4.1", p.match(d))
    print("4.2", p.search(d))
    print("4.3", p.findall(d))
    print("4.4", p.findall(d)[0])
    for piter in p.finditer(d) : print("4.5", piter)
    print("4.6", re.split(patterndes, d))
