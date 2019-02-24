#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
print("hello world")

if True:
    print("true")
else:
    print(false)

'''

'''
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
'''

# 第一个注释


'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

'''
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
x="a"
y="b"
# 换行输出
print(x)
print(y)
'''

'''
a = b = c = 1
a, b, c = 1, 2, "john"
print(a)
'''

'''
Python有五个标准的数据类型：
Numbers（数字）
    int/long/float/complex
String（字符串）
    h e l l o
    0 ~ len-1
    -(len) ~ -1
    
    [head:tail]
List（列表）
    [a1,a2...]
    0 ~ len-1
    -(len) ~ -1
    [head:tail]
Tuple（元组）
    (a1, a2, a3)
    0 ~ len-1
    -(len) ~ -1
    [head:tail]
    
    read-only
Dictionary（字典）
'''

'''
a = 10
#del a
print(a)
'''

'''
str = 'hello'
print(str[1])
print(str[1:])
print(str[1:2])  #  right is open
print(str[0:2])
'''

'''
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)
print(list[1:])
print(list[1:3]) # right is open
print(list[:3])
'''

'''
tuple = ('runoob', 786, 2.23, 'john', 70.2)
print(tuple)  # 输出完整元组
print(tuple[1:])  # 输出完整元组
print(tuple[1:3])  # 输出完整元组
print(tuple[:3])  # 输出完整元组
tuple[0] = 'hello'##error
'''

'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值
'''


'''
python operator
    math
        + - * / & ** //
    compare
        == != <> > < >= <=
    assign
        = += -= *= /= %= **= //=
    logical
        and or not
    bits
        & | ^ ~ >> <<
    
    member
        in
        not in
    identify(addr)
        is 
        is not
    priority
'''

'''
print(3.0/2)
print(-3.0/2)

print(3.0//2)
print(-3.0//2)
'''


'''
condition statement 

if condition:
    operation
elif condition:
    operation
else:
    operation
'''

'''
num = 5
if num == 3:
    print("==3")
elif num == 4:
    print("==4")
elif num == 5:
    print("==5")
else:
    print("nothing")
'''

'''
python not support switch
'''

'''
python loop

while condition:
    operation


for iter_var in sequence
   opt
   

loop control:
    break
    continue
    pass #placeholder
'''

'''
count = 0
while count < 9:
   print('The count is:', count)
   count = count + 1

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print('当前水果 :', fruit)

for index in range(len(fruits)):
   print('当前水果 :', fruits[index])
'''


'''
python-number
    integer
    long integer
    float
    complex
math-module
    for float compute
cmath-module
    for complex compute
    
math-const
    pi
    e
'''

'''
var = 10
print(var)
del var
print(var) #error for not defined
'''

'''
import math
import cmath
print(dir(math))
print(dir(cmath))
print(math.pi)
print(math.e)
'''

'''
python-string
    var = 'sdf'
    var = "sdf"
escape-char

string-operator
    + * [] [:]
    in 
    not in
    r/R: raw data
    %: format string
    
    string.xxx
'''

'''
var = "hello world"
print(var[1])
print(var[1:5])

var = var[2:]
print(var)

str1 = "hello \n world"
str2 = r"hello \n world"
str3 = u"hello \n world"
print(str1)
print(str2)
print(str3)
print("str1[%s], str2[%s], str3[%s]" % (str1, str2, str3))
'''

'''
python-list
    [a1,a2,a3]
    [pos1:pos2]
    .append
    del list[pos1:pos2]
    len(list)
    +
    *
    in, not in
    max, min
    list(seq)
    
    
    list.xxx
'''
'''
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print(list1[0])
print(list2[0:3])

list2.append(8)
print(list2)
del list2[0]
print(list2)
'''


'''
python-table
    {key1 : val1, key2 : val2, key3:val3}
    del dict[key]
    dict.clear()
    del dict
    
    cmp/len/str/type
    
    dict.xxxx
'''

'''
dict = {'a': 1, 'b': 2, 'c': '3'}
print(dict)
#print(dict["noval"]) #error
dict['a'] = 'hello'
print(dict)

del dict['a']
print(dict)

dict.clear()
print(dict)

del dict
print(dict)
'''

'''
import time

print(time.time())
localtime = time.localtime(time.time())
print(localtime)
'''


'''
def function-name(parameters)
    "function_doc_str"
    function_suite
    return [expression]

function-param
    immutable(val)
    mutable(reference)
        list, dict
param-type
    must-param
        def funcname(param1)
    default-param
        def funcname(param1 = 10)
    keyword-param
        call funcname(param1 = 4)
    variable-param
        def funcname([formal_args], *var_args_tuple)
'''


'''
def HelloWorld():
    print('hello world')
    return

HelloWorld()
'''

'''

def changeInt(var):
    var = 10

var = 3
print(var)
changeInt(var)
print(var)

def changeList(list):
    list.append("hello world")

list = [1, 2, 3]
print(list)
changeList(list)
print(list)
changeList(list)
print(list)
'''

'''
def printinfo(arg1, *vartuple):
    print("arg1[%d]" %(arg1))
    for var in vartuple:
        print(var)
    return

printinfo(10, 'a', 'b', 'c')
printinfo(10, 'a', 'b')
'''

'''
python-lambda
    lambda [arg1 [,arg2, .. argn]]: expression
'''

'''
sum = lambda arg1, arg2: arg1 + arg2
print(sum(1, 2))
print(sum(1.1, 2.2))
'''


'''
local-var
global-var
'''

'''
total  = 10
def hello():
    total = 100

hello()
print(total)
'''

'''
python-module
    import module-name
    module-name.member
    
    from module-name import symbol1, symbol2
    from module-name import *
    symbolxx
'''

'''
#import support
#support.print_func()

from support import print_func
print_func()
'''

'''
namespace and scope
    local 
    global
'''

'''
money = 10

def addMoney():
    global money #if not global, then error
    money += 100

print(money)
addMoney()
print(money)
'''

'''
python-symbol
    dir
    locals
    globals
'''

'''
import math
print(dir(math))

def Hello1():
    var = 'world'
    print(locals())
    print(globals())

Hello1()
'''

'''
reload-module
'''

'''
python-input
    raw-input
file-opt
    open
    write
    read
    seek(offset[, from])
    
    file.closed
    file.mode
    file.name
    file.softspace 
    
    os.rename
    os.remove
    os.mkdir
    os.chdir
    os.getcwd
    
    os.rmdir
'''

'''
str = input("请输入：")
print(str)
'''

'''
fo = open("test.txt", "w")
print(fo.name, fo.closed, fo.mode)

fo.close()
print(fo.name, fo.closed, fo.mode)
'''

'''
import os
os.getcwd()
'''


'''
Exception handle
    Exception
    Assert

try:
    statement
except except-class:
    opt
except except-class, data:
    opt 
else:
    opt
finally:


trigger-exception
    raise
    raise [Exception [, args [, traceback]]] 

user-defined exception

'''

'''
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
finally:
    print("finally got here")
'''


'''
import os
python-os/directory
    access/chdir/chflags/chmod/chown/chroot/
    close/closerange/dup/dup2
    fchdir/fchmod/fchown/fdatasync/fdopen/fpathconf
    fstat/fstatvfs/fsync
    getcwd/getcwdu/...
'''

'''
python-builtin-function
    abs
'''
'''
print(abs(-1))
print(abs(1))
'''


'''
python-ooa&ood

attr-opt
    hasattr/getattr/setattr/delattr
builtin-attr
    __dict__
    __doc__
    __name__
    __module__
    __bases__
object-gc
    count-reference-gc
    loop-gc
    
python-inherit
    isinstance
    issubclass
    
    overwrite

basic-override method
    __init__
    __del__
    __repr__
    __repr__
    __str__
    __cmp__
class property and method
    private-property
        __private_attrs
        print(obj._Classname__privateattr)
    class-method
        def class_method(self):
    private-method
        def __private_method
'''

'''
class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def __del__(self):
        print("classname[%s]" %(self.__class__.__name__))

    def displayCouont(self):
        print("Total Employee[%d]" %(Employee.empCount))

    def displayEmployee(self):
        print("name[%s], salary[%f]" %(self.name, self.salary))

emp1 = Employee("goldbeef1", 1)
emp2 = Employee("goldbeef2", 2)

emp1.displayEmployee()
emp2.displayEmployee()

hasattr(emp1, 'age')

#add attr
emp1.age = 10
print(getattr(emp1, 'age'))

setattr(emp1, 'age', 20)
print(getattr(emp1, 'age'))

delattr(emp1, 'age')
#print(getattr(emp1, 'age'))#error for no-attr

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)


print("___gc_test")
print(id(emp1))
print(id(emp2))
del emp1
del emp2
'''

'''
class Parent:
    parentAttr = 100

    def __init__(self):
        print("Parent::init")

    def myMethod(self):
        print("Parent:myMethod")

    def parentMethod(self):
        print("Parent::method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("ParentAttr[%d]" %(Parent.parentAttr))

class Child(Parent):
    def __init__(self):
        print("Child::init")

    def myMethod(self):
        print("Child:myMethod")

    def childMehtod(self):
        print("Child::childMethod")

c = Child()
c.childMehtod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

print(issubclass(Child, Parent))
print(isinstance(c, Parent))
print(isinstance(c, Child))

c.myMethod()
'''

'''
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1

    def __count(self):
        self.__secretCount += 1
        self.publicCount += 1

counter = JustCounter()

counter.count()
#counter.__count() #error for private method

print(counter.publicCount)
#print(counter.__secretCount) #error for private method
print(counter._JustCounter__secretCount) #some way to access private-method

counter._JustCounter__secretCount = 100 #some way to access private-method
print(counter._JustCounter__secretCount) #some way to access private-method
'''

'''
import math
import cmath

#math.sqrt(-1) #error
print(cmath.sqrt(-1)) #ok for complex-number support
'''

"sdfsf"

seq = [None]*10
print(seq)


