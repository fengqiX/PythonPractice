"""类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算----类型和运算"""

obj = list()
#-- help checking
dir(obj) #simply list all methods included in object obj, return a list
help(obj) #qurey obj.func about introdaction and way to use it

L = list()
#-- type checking
if type(L) == type([]):
    print("L is list")
if type(L) == list:
    print('L is list')
if isinstance(L, list): # recommended
    print('L is list')

#-- Python data type: hashable & unhashable
    ##hashable,  if it has a hash value which never changes during its lifetime , and can be compared to other objects
    "数字类型：int, float, decimal.Decimal, fractions.Fraction, complex"
    "字符串类型：str, bytes"
    "元组：tuple"
    "冻结集合：frozenset" # ?
    "布尔类型：True, False"
    "None"

#-- numbers
1234 #integer
1.23, 3.14e-10 #float
0o177, 0x9ff,0X9FF, 0b01010 #hex,oct,bin
3+4j, 3.0+4.0j #complex
hex(I), oct(I) , bin(I) #convert decimal to hex,oct,binary in string
int(string, base)

#-- expression
yield x # generator key word
lambda args:expression # anonymous function
x if y else z # 三元选择表达式
-x, +x, ~x                                   ## 一元减法、识别、按位求补（取反）
x[i], x[i:j:k]                               ## 索引、分片、调用

#-- integer could use bit_length to test the lenght when convert to binary number
a =1
a.bit_length() #1
a=1024
a.bit_length() #11

#-- difference between __repr()__ and __str()__
"""
repr格式：默认的交互模式回显，产生的结果看起来它们就像是代码。
str格式：打印语句，转化成一种对用户更加友好的格式。
"""

#-- number related modules
    #math
    # Decimal
    import decimal
    from decimal import Decimal
    Decimal("0.01") +Decimal("0.01") #return Decimal("0.03")
    decimal.getcontext().prec=4 ## 设置全局精度为4 即小数点后边4位
    # Fraction
    from fractions import Fraction
    x = Fraction(4,6)            #4/6
    x = Fraction(".25")          #1/4

#-- 集合set
    """
    set是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素。
    set支持union(联合), intersection(交), difference(差)和symmetric difference(对称差集)等数学运算。
    set支持x in set, len(set), for x in set。
    set不记录元素位置或者插入点, 因此不支持indexing, slicing, 或其它类序列的操作
    """
    s = set([3,5,8,5])
    t = set("hello") #return set {'H', 'o', 'l', 'e'}
    a = t|s;  a  = t.union(s)
    b = t&s; t.intersection(s)
    c = t-s; t.difference(s)
    d = t^s; t.symmetric_difference(s)
    t.add("x")
    t.remove("H") # if the element in the set, it will raise an error
    t.update([13,3])
    s.issubset(t) ; s<=t
    s.issuperset(t) ; s>=5
    x in s; x not in s #x has to be a single element instead of a set
    s.copy()
    s.dsicard(x) # will not raise an error if the element not in the set
    s.clear()
    {x**2 for x in [1,2,3,4]}
    {x for x in 'spam'}

#-- frozenset ??
    a = set([1,2,3])
    b = set()
    b.add(a)
    b.add(frozenset(a))  ##???

#-- dynamic type
"""
变量名通过引用，指向对象。
Python中的“类型”属于对象，而不是变量，每个对象都包含有头部信息，比如"类型标示符" "引用计数器"等
"""
# 共享引用及在原处修改：对于可变对象，要注意尽量不要共享引用！
# 共享引用和相等测试：
L = [1] , M = [1] , L is M # return false
L = M = [1] , L is M # return true, 共享引用 - shared reference ?
# 增强赋值和共享引用：普通+号会生成新的对象，而增强赋值+=会在原处修改
L = M = [1, 2]
L = L + [3, 4]  # L = [1, 2, 3, 4], M = [1, 2]
L += [3, 4]  # L = [1, 2, 3, 4], M = [1, 2, 3, 4]

# string
S= ''
S="spam's"
S="s\np\ta\x00m"
S="""spam"""
S=r"\temp"   # Raw字符串，不会进行转义，抑制转义
S = b"Spacm"   # Python3中的字节字符串
'a %s parrot' % 'kind'  # 字符串格式化表达式
'a {1} {0} parrot'.format('kind', 'red')# 字符串格式化方法
','.join(['a','b','c']) #use join keyword to output string

#build-in str func
str1= "stringobject"
str1.upper();str1.lower();str1.swapcase();str1.capitalize();str1.title()
str1.ljust(29) # 获取固定长度，左对齐，右边不够用空格补齐
str1.rjust(29) # 获取固定长度，右对齐，左边不够用空格补齐
str1.center(29)   # 获取固定长度，中间对齐，两边不够用空格补齐
str1.zfill(29) # 获取固定长度，右对齐，左边不足用0补齐

str1.find("t",start,end)
str1.rfind("T")
#上面所有方法都可用index代替，不同的是使用index查找不到会抛异常，而find返回-1
str1.replace('old','new')
str1.strip()  #delete space on left and right
str1.strip('d') # 删除str1字符串中开头、结尾处，位于 d 删除序列的字符
str1.lstrip();
str1.lstrip('d');  # 删除str1字符串中开头处，位于 d 删除序列的字符
str1.rstrip();
str1.rstrip('d')  # 删除str1字符串中结尾处，位于 d 删除序列的字符
str1.startswith("start")
str1.endswith("end")
str1.isalnum(); str1.isnumeric();str1.islower();str1.isupper()
#-- 三重引号编写多行字符串块，并且在代码折行处嵌入换行字符\n
mantra = """hello world
            hello python
            hello my friend"""
    # mantra为"""hello world \n hello python \n hello my friend"""

#-- index & slice
S[0], S[len(S)-1],S[-1]
S[1:3], S[1:],S[:-1],S[1:10:2]  # 分片，第三个参数指定步长，如`S[1:10:2]`是从1位到10位没隔2位获取一个字符。

#-- parsing
int('42'), str(42)
float('4.12'),str(4.12)
#Given a string representing one Unicode character, return an integer representing the Unicode code point of that character.
ord('s'),chr(115)    # 返回(115, 's')
int('1001',2) # 将字符串作为二进制数字，转化为数字，返回9
bin(13), oct(13), hex(13)               # 将整数转化为二进制/八进制/十六进制字符串，返回('0b1101', '015', '0xd')

#-- concatnate
name = "wang" "hong"
name = "wang"\               
    "hong"   #does not work

#-- Python中的字符串格式化实现1--字符串格式化表达式
    """
    基于C语言的'print'模型，并且在大多数的现有的语言中使用。
    通用结构：%[(name)][flag][width].[precision]typecode
    """
"this is %d %s bird" % (1,"dead")
"%s--%s--%s" % (42,3.14,[1,2,3])
"%d....%6d....%-6d....%06d" % (1234,1234,1234,1234)
x=1.23456789
"%e | %f | %g" % (x,x,x)
"%6.2f*%-6.2f*%06.2f*%+6.2f" % (x,x,x,x)
"%(name1)d----%(name2)s" % {"name1":23, "name2":"value2"}
"%(name)s is %(age)d" % vars()   ##???

#-- Python中的字符串格式化实现2--字符串格式化调用方法
import sys
#normal
"{0}, {2} and {1}".format('spam', 'ham','eggs')
"{}, {} and {}".format('spam', 'ham','eggs')
"{motto} and {pork}".format(motto='spam',pork='ham')
"{motto} and {0}".format('ham',motto="spam")
"my {1[spam]} runs {0.prefix}, and {1[pork]}".format(sys ,{'spam':'laptop', "pork" : 'ham'})
"{config[spam]} {sys.platform}".format(sys=sys, config= {'spam':'laptop', "pork" : 'ham'})
"first = {0[0]}, and second = {0[1]}".format(["A",'B','C'])
#specific
"{0[0]:e}, {0[1]:.3e}, {1:g}".format([3.141592,3.141592],3.141592)

# 说明:
"{fieldname:format_spec}".format(......)
"""
    fieldname是指定参数的一个数字或关键字, 后边可跟可选的".name"或"[index]"成分引用
    format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
    fill        ::=  <any character>              #填充字符
    align       ::=  "<" | ">" | "=" | "^"        #对齐方式
    sign        ::=  "+" | "-" | " "              #符号说明
    width       ::=  integer                      #字符串宽度
    precision   ::=  integer                      #浮点数精度
    type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""
'={0:10} ={1:<10.3b}'.format('spam',123.456)
'={0:>10}='.format('test')  # 输出'=      test='
'={0:<10}='.format('test')  # 输出'=test      ='
'={0:^10}='.format('test')  # 输出'=   test   ='
'{0:X}, {1:o}, {2:b}'.format(255, 255, 255)  # 输出'FF, 377, 11111111'
'My name is {0:{1}}.'.format('Fred', 8)  # 输出'My name is Fred    .'  动态指定参数

#-- 常用列表常量和操作
L=[[1,2],'String',{}]
L = list('spam')
L=list(range(0,4))
list(map(ord,'spam')) # 列表解析
L.count("1")
L.append([1,2])  #add object which could be other type
L.inset(index, obj)
L.extend([1,2]) #add the element of the another list
L.index('1',0,4)  # search for '1', start from position 0, end before 4
L.pop(),L.pop(index)
L.remove(value)
L.reverse()
L.sort(cmp=None,key=None,reverse=False) ##??

a = [1,2,3], b=a[10:]   # 注意，这里不会引发IndexError异常，只会返回一个空的列表[]
a = [], a += [1]  # 这里实在原有列表的基础上进行操作，即列表的id没有改变
a = [], a = a + [1]  # 这里最后的a要构建一个新的列表，即a的id发生了变化

#-- use slice to delete part of list
a = [1, 2, 3, 4, 5, 6, 7]
a[1:4]=[]
del a[::2] # 去除偶数项(偶数索引的)

#--dict
D={}, D=dict()
D={'spam':2,'tol':{'ham',1}}
D=dict.fromkeys(['s','t'],8)
D=dict(name='tom',age=12)
D=dict([('name','tom'),('age',13)])
D=dict(zip(['name','tom'],['age',12]))  ## zip
D.keys(), D.values(), D.items()
D.get(key), D[key]
D.update(D_other)
D.pop(key,default_return_value)
D.popitem()
D.setdefault(key[,value])
del D
del D[key]
D[(1,2,3)] = 2   # tuple作为字典的key

#--
D={k:None for k in ['s','t']}
#-- 字典的特殊方法__missing__：当查找找不到key时，会执行该方法
    class Dict(dict):
        def __missing__(self, key):
            self[key] = []
            return self[key]

dct = dict()
dct["foo"].append(1)  # 这有点类似于collections.defalutdict #not working in py 3.7
dct["foo"]  # [1]

a=[1,2,3] #list
a=(1,2,3) #tuple
a = ([1, 2])  # a[0][1] = 0, OK
a = [(1, 2)]  # a[0][1] = 0, Error

# -- 文件基本操作
# need to go through again carefully
output = open(r'C:\spam', 'w')  # 打开输出文件，用于写
input = open('data', 'r')  # 打开输入文件，用于读。打开的方式可以为'w', 'r', 'a', 'wb', 'rb', 'ab'等
fp.read([size])  # size为读取的长度，以byte为单位
fp.readline([size])  # 读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size])  # 把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长。
fp.readable()  # 是否可读
fp.write(str)  # 把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq)  # 把seq的内容全部写到文件中(多行一次性写入)
fp.writeable()  # 是否可写
fp.close()  # 关闭文件。
fp.flush()  # 把缓冲区的内容写入硬盘
fp.fileno()  # 返回一个长整型的”文件标签“
fp.isatty()  # 文件是否是一个终端设备文件（unix系统中的）
fp.tell()  # 返回文件操作标记的当前位置，以文件的开头为原点
fp.next()  # 返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[, whence])  # 将文件打开操作标记移到offset的位置。whence为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。
fp.seekable()  # 是否可以seek
fp.truncate([size])  # 把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。
for line in open('data'):
    print(line)  # 使用for语句，比较适用于打开比较大的文件
with open('data') as file:
    print(file.readline())  # 使用with语句，可以保证文件关闭
with open('data') as file:
    lines = file.readlines()  # 一次读入文件所有行，并关闭文件
open('f.txt', encoding='latin-1')  # Python3.x Unicode文本文件
open('f.bin', 'rb')  # Python3.x 二进制bytes文件
# 文件对象还有相应的属性：buffer closed encoding errors line_buffering name newlines等

# -- 其他
# Python中的真假值含义：1. 数字如果非零，则为真，0为假。 2. 其他对象如果非空，则为真
# 通常意义下的类型分类：1. 数字、序列、映射。 2. 可变类型和不可变类型


"""语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句----语法和语句"""

# -- 赋值语句的形式
spam = 'spam'  # 基本形式
spam, ham = 'spam', 'ham'  # 元组赋值形式
[spam, ham] = ['s', 'h']  # 列表赋值形式
a, b, c, d = 'abcd'  # 序列赋值形式
a, *b, c = 'spam'  # 序列解包形式（Python3.x中才有）
spam = ham = 'no'  # 多目标赋值运算，涉及到共享引用
spam += 42  # 增强赋值，涉及到共享引用

#-- 序列赋值 序列解包
    [a, b, c] = (1, 2, 3)                  # a = 1, b = 2, c = 3
    a, b, c, d = "spam"                    # a = 's', b = 'p', c = 'a', d = 'm'
    a, b, c = range(3)                     # a = 0, b = 1, c = 2
    a, *b = [1, 2, 3, 4]                   # a = 1, b = [2, 3, 4]
    *a, b = [1, 2, 3, 4]                   # a = [1, 2, 3], b = 4
    a, *b, c = [1, 2, 3, 4]                # a = 1, b = [2, 3], c = 4
    # 带有*时 会优先匹配*之外的变量 如 ##
    a, *b, c = [1, 2]                      # a = 1, c = 2, b = []

#-- print()
print(value,...,sep=' ',end='\n',file=sys.stdout,flush=False)
print('hello world') #equals to sys.stdout.write('hello world')
sys.stdout = open('log.log', 'a')  # 流的重定向
print('hello world')  # 写入到文件log.log
sys.stdout.close()
sys.stdout = temp  # 原有流的复原

1 or 2 or 3  # 返回 1, result is true then return the first true value, result if false then return the last false value.
1 and 2 and 3  # 返回 3, result is true then return the last true value, result if false then return the first false value.

#-- if/else三元表达符（if语句在行内）
    A = 1 if X else 2
    A = 1 if X else (2 if Y else 3)
    # 也可以使用and-or语句（一条语句实现多个if-else）
    a = 6
    result = (a > 20 and "big than 20" or a > 10 and "big than 10" or a > 5 and "big than 5")    # 返回"big than 5"

#-- Python的while语句或者for语句可以带else语句 当然也可以带continue/break/pass语句
    while a > 1:
        anything
    else:
        anything
    # else语句会在循环结束后执行，除非在循环中执行了break，同样的还有for语句
    for i in range(5):
        anything
    else:
        anything

M = [[1,2,3],[4,5,6],[7,8,9]]
res = [sum(num) for num in M]
res = [c*2 for c in 'spam']
res = [a*b for a in [1,2] for b in [4,5,6]]
res = [a for a in [1,3,5] if a<2]
res = [a if a>0 else 0 for a in [-1,0,1]]
for teama,teamb in zip(["Packers", "49ers"], ["Ravens", "Patriots"]):
    print(teama + " vs. " + teamb)
    # with index, enumerate
for index, team in enumerate(["Packers", "49ers", "Ravens", "Patriots"]):
    print(index, team)

#-- generator
G = (sum(row) for row in M)
G= {sum(row) for row in M}
G={i:sum(M[i]) for i in range(3)}

#-- 文档字符串:出现在Module的开端以及其中函数或类的开端 使用三重引号字符串
    """
    module document
    """
    def func():
        """
        function document
        """
        print()
    class Employee(object):
        """
        class document
        """
        print()
    print(func.__doc__)                # 输出函数文档字符串
    print(Employee.__doc__)            # 输出类的文档字符串

#-- 命名惯例:
    """
    以单一下划线开头的变量名(_X)不会被from module import*等语句导入
    前后有两个下划线的变量名(__X__)是系统定义的变量名，对解释器有特殊意义
    以两个下划线开头但不以下划线结尾的变量名(__X)是类的本地(私有)变量
    """

#-- manully delete variable
del X

#-- get subset for a list
x=[1,2,3,4,5,6]
x[:3] #456
x[1:5] #2345
x[-3:] #456
x[::2] #135
x[1::2] #246

#-- 手动迭代：iter和next
    L = [1, 2]
    I = iter(L)                        # I为L的迭代器
    I.next()                           # 返回1
    I.next()                           # 返回2
    I.next()                           # Error:StopIteration

#-- 函数相关的语句和表达式
    myfunc('spam')                     # 函数调用
    def myfunc():                      # 函数定义
    return None                        # 函数返回值
    global a                           # 全局变量
    nonlocal x                         # 在函数或其他作用域中使用外层（非全局）变量
    yield x                            # 生成器函数返回
    lambda                             # 匿名函数

#-- Python函数变量名解析:LEGB原则，即:
    """
    local(functin) --> encloseing function locals --> global(module) --> build-in(python)
    说明:以下边的函数maker为例 则相对于action而言 X为Local N为Encloseing
    """
#-- 嵌套函数举例:工厂函数
    def maker(N):
        def action(X):
            return X ** N
        return action
    f = maker(2)                       # pass 2 to N
    f(3)                               # 9, pass 3 to X

#-- 嵌套函数举例:lambda实例
    def maker(N):
        action = (lambda X: X**N)
        return action
    f = maker(2)                       # pass 2 to N
    f(3)                               # 9, pass 3 to X

#-- nonlocal key word indicate that the variable is not for the inner nested function instead it will reference to the outter function
#-- nonlocal和global语句的区别
    # nonlocal应用于一个嵌套的函数的作用域中的一个名称 例如:
    start = 100
    def tester(start):
        def nested(label):
            nonlocal start             # 指定start为tester函数内的local变量 而不是global变量start
            print(label, start)
            start += 3
        return nested
    # global为全局的变量 即def之外的变量
    def tester(start):
        def nested(label):
            global start               # 指定start为global变量start
            print(label, start)
            start += 3
        return nested

def f(a,b,c):print(a,b,c)
f(1,2,3)
f(1,c=2,b=5)
def f(a,b=1,c=2):print(a,b,c)
f(1)
f(1,2)
f(a=1,b=4)
def keyOnly(a, *b, c): print(c)  # c就为keyword-only匹配 必须使用关键字c = value匹配
keyOnly(1,c=5) # output:5
def keyOnly(a, *, b, c): ......  # b c为keyword-only匹配 必须使用关键字匹配
def keyOnly(a, *, b=1): ......  # b有默认值 或者省略 或者使用关键字参数b = value

#-- use *, ** as parameters
#  * take positional parameters
def f(*args):print(args)
f(1,2,3)
# ** take keyword parameters
def f(**args):print(args)
f(a=1,b=45)

def f(a,*b,**c):print(a,b,c)
f(1, 2, 3, x=4, y=5)
f(1)
f(1,x=1)
f(x=1) #would not work, for positional argument should not follow keyword argument

# -- 函数调用时的参数解包: * 和 ** 分别解包元组和字典
func(1, *(2, 3)) <= = > func(1, 2, 3)
func(1, **{'c': 3, 'b': 2}) <= = > func(1, b=2, c=3)
func(1, *(2, 3), **{'c': 3, 'b': 2}) <= = > func(1, 2, 3, b=2, c=3)

# -- 函数属性:(自己定义的)函数可以添加属性
def func(): .....

func.count = 1  # 自定义函数添加属性
print.count = 1  # Error 内置函数不可以添加属性


#-- 函数注解: 编写在def头部行 主要用于说明参数范围、参数类型、返回值类型等
# 编写注解的同时 还是可以使用函数默认值 并且注解的位置位于=号的前边
def func(a:'spam'='a',b:(1,10)=2,c:float=1.1) -> int:
    func.d=5
    print(a,b,c,func.d)
 func.__annotations__               # {'c':<class 'float'>, 'b':(1, 10), 'a':'spam', 'return':<class 'int'>}

f = lambda x,y,z:x+y-z
f = lambda x=1,y=1:x+y
f = lambda: a if xxx() else b  ##?? 无参数lambda func

list(map(lambda x:x>0,[1,2,3,4]))  #[True, True, True, True]
list(map(lambda x:x+1,[1,2,3,4]))  #[2, 3, 4, 5]
list(filter(lambda x:x>0,range(-4,4))) #[1, 2, 3]
list(filter(lambda x:x+1,range(-4,4))) #[-4, -3, -2, 0, 1, 2, 3]
functools.reduce((lambda x,y:x+y),[1,2,3]) ##??

#-- 生成器函数:yield VS return
def gensquare(N):
    for i in range(N):
        yield i** 2
for i in gensquare(5):
    print(i,end=',')
x=gensquare(3)
next(x)
next(x)
next(x)
next(x)

#-- 生成器表达式:小括号进行列表解析
G = (x ** 2 for x in range(3))  # 使用小括号可以创建所需结果的生成器generator object
next(G), next(G), next(G)  # 和上述中的生成器函数的返回值一致
# （1）生成器(生成器函数/生成器表达式)是单个迭代对象
G = (x ** 2 for x in range(4))
I1 = iter(G)  # 这里实际上iter(G) = G
next(I1)  # 输出0
next(G)  # 输出1
next(I1)  # 输出4
# （2）生成器不保留迭代后的结果
gen = (i for i in range(4))
2 in gen  # 返回True
3 in gen  # 返回True
1 in gen  # 返回False，其实检测2的时候，1已经就不在生成器中了，即1已经被迭代过了，同理2、3也不在了

#-- 本地变量是静态检测的
X=22
def test():
    print(X)  # 如果没有下一语句 则该句合法 打印全局变量X
    X = 88  # 这一语句使得上一语句非法 因为它使得X变成了本地变量 上一句变成了打印一个未定义的本地变量(局部变量)
    if False:  # 即使这样的语句 也会把print语句视为非法语句 因为:
        X = 88  # Python会无视if语句而仍然声明了局部变量X

def tset():
    global X
    print(X)
    X=222

#-- 函数的默认值是在函数定义的时候实例化的 而不是在调用的时候 例子:
def foo(numbers=[]):
    numbers.append(9)
    print(numbers)
foo()  # first time, like before, [9]
foo()  # second time, not like before, [9, 9]
foo()  # third time, not like before too, [9, 9, 9]

def foo(numbers=None):
    if numbers is None: numbers = []
    numbers.append(9)
    print(numbers)

# 另外一个例子 参数的默认值为不可变的:
def foo(count=0):  # 这里的0是数字, 是不可变的
    count += 1
    print(count)
foo()  # 输出1
foo()  # 还是输出1
foo(3)  # 输出4
foo()  # 还是输出1

#--math
abs(x)
complex(1,5)
divmod(100.1,7)    #100.1 / 7, 100.1%7
float('3'),float(3)
int(5.1), int('11111111',2)
long([x[, base]])
pow(x,y) # 返回x的y次幂
range(1,10,2) #return generator/iterable
round(1.1)
sum(range(1,10,2),1)
oct(x)  # 将一个数字转化为8进制字符串
hex(x)  # 将一个数字转换为16进制字符串
chr(i)  # 返回给定int类型对应的ASCII字符
unichr(i)  # 返回给定int类型的unicode
ord(c)  # 返回ASCII字符对应的整数
bin(x)  # 将整数x转换为二进制字符串
bool([x])  # 将x转换为Boolean类型







