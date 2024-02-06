'''the following examples refers to: 「页面」Python基础语法 | 菜鸟教程  https://www.runoob.com/python/python-basic-syntax.html'''

# about list
def exList1() :
    list1 = ["number", 'string', '''list''', 'tuple', 'dictionary']
    list2 = ["整型", '字符串', '列表', '元组', '字典']
    print(list1)               # 输出完整列表
    print(list1[0])            # 输出列表的第一个元素
    print(list1[1:3])          # 输出第二个至第三个元素 
    print(list1[2:])           # 输出从第三个开始至列表末尾的所有元素
    print(list2 * 2)       # 输出列表两次
    print(list1 + list2)   # 打印组合的列表

# about list(1)
def exList2() :
    list1 = ["number", 'string', '''list''', 'tuple', 'dictionary', 1, 2, [1.0, 2.0, 3.0 ], ("Item1", 2, "item3"), {"iPhone": 13.4, "Android": 17.632} ]
    print(list1)               # 输出完整列表
    print(list1[7])               # 输出完整列表
