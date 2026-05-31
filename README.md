# Python

## <span style="color:rgb(255, 146, 18)">了解python</span>

### <span style="color:rgb(144,120,249)"> Python简介</span>

 <span style="color:rgb(4, 206, 41)">编程语言</span>是用来定义计算机程序的语言，用来向计算机发出指令

 <span style="color:rgb(4, 206, 41)">Python语言</span>是一种<span style="color:red">面向对象</span>的<span style="color:red">解释型</span>高级编程语言

 python是强类型的动态脚本语言


### <span style="color:rgb(144,120,249)">编译型和解释型语言的</span><span style="color:rgb(144,120,249)">区别</span>
1. 编译型语言编译后就可以在平台运行，解释型语言在运行期间才编译

2. 一般来说，编译型语言运行速度快

3. 解释型语言跨平台特性比编译型语言好

### <span style="color:rgb(144,120,249)">编写第一个程序</span>

```python
print("Hello World")
```

#### <span style="color: rgb(255, 0, 0);" >注意</span>

1. 输入错误：python中的符号都是要用英文模式下的
2. 缩进错误：print要顶格写，否则就报错
3. 语法错误：一个print必须单独写一行，错误信息遇到Syntax说明语法有问题
4. 命名错误：字符串必须加上引号，单引号或双引号都可

## <span style="color:rgb(255, 146, 18)">注释与输出函数</span>
### <span style="color:rgb(144,120,249)">注释</span>
注释可以放在任意位置，但是注释的内容不会被程序执行
```python
# 这是一个单行注释，使用#符号开头
"""
这是一个多行注释，使用三个双引号或三个单引号包裹
可以写多行内容
"""
```

### <span style="color:rgb(144,120,249)">输出函数print()</span>

print()函数可以输出字符串、数字、变量等内容

```python
print("Hello World") # 输出字符串
print(123) # 输出数字
name = "Alice"
print(name) # 输出变量
```

print(字符串，end="后面拼接的值") 最后输出的结果：第一个print中的字符串+后面拼接的值

```python
print("Hello", "World") # 输出多个内容，默认用空格分隔
print("Hello" + "World") # 输出多个内容，使用字符串连接符
```

sep参数可以指定输出多个内容时的分隔符，默认为空格

```python
print("Hello", "World", sep="-") # 输出Hello-World
print("Hello", "World", sep="") # 输出HelloWorld
```

end参数可以指定输出结束时的字符，默认为换行符\n
print(字符串，end="后面拼接的值") 最后输出的结果：第一个print中的字符串+后面拼接的值

```python
print("Hello", end="") # 输出字符串，结尾不换行
print("World") # 输出字符串，继续在同一行输出
```

## <span style="color:rgb(255, 146, 18)">变量与标识符</span>
###  <span style="color:rgb(144,120,249)">变量</span> 
变量的概念：
变量是用来存储数据的容器，可以在程序中使用变量来保存和操作数据
变量的作用：
1. 变量可以存储不同类型的数据，如数字、字符串、布尔值等
2. 变量可以在程序中被修改和更新，方便数据的处理和计算
3. 变量可以提高代码的可读性和可维护性，使用有意义的变量名可以让代码更易于理解
4. 变量可以在函数之间传递数据，实现数据的共享和交流
变量的定义和使用：
```python
name = "Alice" # 定义一个字符串变量
age = 30 # 定义一个整数变量
height = 1.75 # 定义一个浮点数变量
print(name) # 输出变量的值
print(age)
print(height)
```
#### <span style="color: rgb(255, 0, 0);" >注意</span> 
1. 变量名必须以字母或下划线开头，后面可以跟字母、数字或下划线
2. 变量名不能使用Python的保留字，如if、for、while等
3. 变量名区分大小写，name和Name是两个不同的变量
4. 变量可以在定义后被修改，但必须先定义后使用，否则会报错
```python
name = "Alice" # 定义变量
print(name) # 输出变量的值
name = "Bob" # 修改变量的值
print(name) # 输出修改后的变量值
``` 

### <span style="color:rgb(144,120,249)">标识符</span>
标识符是用来命名变量、函数、类等的名称，必须遵守一定的命名规则：
1. 标识符必须以字母或下划线开头，后面可以跟字母、数字或下划线
2. 标识符不能使用Python的保留字，如if、for、while等
3. 标识符区分大小写，name和Name是两个不同的标识符
4. 标识符应该具有描述性，能够清晰地表达其用途和意义

```python
# 定义一个函数，使用标识符my_function
def my_function():
    print("This is a function")
# 定义一个类，使用标识符MyClass
class MyClass:
    def __init__(self, name):
        self.name = name
# 定义一个变量，使用标识符my_variable
my_variable = 42
```

常用的命名方法（一种习惯，没有绝对性）
1. 下划线分割法：多个单子组成的名称，使用小写字母，单词与单词之间使用下划线分开
2. 大驼峰命名法：多个单词组成的名称，每个单词的首字母大写，其余字母小写
3. 小驼峰命名法：第一个单词首字母小写，后面单词首字母大写，其余字母小写

```python
# 下划线分割法
my_variable = 42
# 大驼峰命名法
MyClass = MyClass()
# 小驼峰命名法
myFunction = my_function()
```

## <span style="color:rgb(255, 146, 18)">数值类型、字符串与格式化输出</span>
### <span style="color:rgb(144,120,249)">数值类型</span>
Python中的数值类型主要包括整数（int）和浮点数（float）。整数是没有小数部分的数字，而浮点数是有小数部分的数字。Python还支持复数（complex）类型、布尔值（bool）类型等其他数值类型。复数由实部和虚部组成，使用j或J表示虚部。

```python
# 定义整数变量
age = 30
# 定义布尔变量
is_student = True
# 定义浮点数变量
height = 1.75
# 定义复数变量，2是实部，3是虚部
complex_number1 = 2 + 3j
complex_number2 = 1 + 4j
print(age) # 输出整数
print(height) # 输出浮点数
print(complex_number1) # 输出复数
print(complex_number1 + complex_number2) # 输出复数的加法结果3 + 7j
print(is_student) # 输出布尔值
``` 
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. 整数和浮点数可以进行各种数学运算，如加、减、乘、除等
2. 整数和浮点数之间的运算会得到一个浮点数
3. 复数可以进行加、减、乘、除等运算，但需要使用复数的实部和虚部进行计算
4. 布尔值只能取True或False，可以用于条件判断和逻辑运算，必须使用大写的True和False，否则会被当作变量名，导致错误
5. 布尔值可以当作整型对待，True被当作1，False被当作0，可以参与数学运算

检测变量类型可以使用type()函数：
```python   
age = 30
height = 1.75
print(type(age)) # 输出<class 'int'>
print(type(height)) # 输出<class 'float'>
``` 

### <span style="color:rgb(144,120,249)">字符串</span>
字符串是由一系列字符组成的文本数据，可以使用单引号、双引号或三引号来定义字符串。字符串支持各种操作，如连接、切片、格式化等。

#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. 多行注释和三引号定义的字符串是不同的，前者是注释，不会被程序执行，而后者是字符串，可以被程序使用
2. 字符串连接可以使用加号（+）运算符，但要注意字符串必须加上引号，否则会被当作变量名，导致错误

```python
# 定义字符串变量
name = "Alice"
name1 = xuduo # 报错，没有引号，xuduo被当作变量名，但没有定义，所以会报错
greeting = 'Hello, ' + name + '!' # 字符串连接
print(greeting) # 输出Hello, Alice!
```

### <span style="color:rgb(144,120,249)">格式化输出</span>
格式化输出是指将变量的值插入到字符串中的特定位置，以便更方便地显示和输出信息。Python提供了多种格式化输出的方法，如百分号（%）格式化、str.format()方法和f-string（格式化字符串字面量）。

#### <span style="color: rgb(170, 206, 62);" >占位符</span>
占位符只占据位置，并不会被输出

| 占位符 | 说明 |
| --- | --- |
| %s | 字符串 |
| %d | 整数 |
| %f | 浮点数 |

%4d表示输出的整数至少占4个字符宽度，如果整数不足4位，则在前面补空格；如果少于4位，则在前面补空格；如果超过4位，则按照实际宽度输出。
```python
name = "Alice"
age = 30
greeting = "Hello, %s! You are %d years old." % (name, age) # 使用占位符进行格式化输出
print(greeting) # 输出Hello, Alice! You are 30 years old.
print("Age: %4d" % age) # 输出Age:   30，整数占4个字符宽度，前面补空格
print("Age: %4d" % 5) # 输出Age:    5，整数占4个字符宽度，前面补空格
print("Age: %4d" % 12345) # 输出Age: 12345，整数超过4个字符宽度，按照实际宽度输出
```

%f表示输出的浮点数默认保留6位小数，遵循四舍五入规则，可以使用%.nf的格式来指定保留n位小数。
```python
pi = 3.141592653589793
print("Pi: %f" % pi) # 输出Pi: 3.141593，浮点数保留6位小数，遵循四舍五入规则
print("Pi: %.2f" % pi) # 输出Pi: 3.14，浮点数保留2位小数，遵循四舍五入规则
```

%%表示输出一个百分号（%），因为%在格式化字符串中有特殊意义，所以需要使用%%来表示一个普通的百分号。
```python
discount = 0.2
print("Discount: %.2f%%" % (discount * 100)) # 输出Discount: 20.00%，浮点数保留2位小数，遵循四舍五入规则
```

f格式化字符串字面量（f-string）是Python 3.6引入的一种格式化字符串的方法，使用f或F前缀来定义字符串，并在字符串中使用花括号{}来插入变量的值。
```python
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old." # 使用f-string进行格式化输出
print(greeting) # 输出Hello, Alice! You are 30 years old.
pi = 3.141592653589793
print(f"Pi: {pi:.2f}") # 输出Pi: 3.14
```

## <span style="color:rgb(255, 146, 18)">算数与赋值运算符</span>
### <span style="color:rgb(144,120,249)">算数运算符</span>
算数运算符用于执行数学运算，包括加法、减法、乘法、除法、取模、幂运算和取整除等。    
| 运算符 | 说明 |
| --- | --- |
| + | 加法 |
| - | 减法 |
| * | 乘法 |
| / | 除法，结果为浮点数 |
| // | 取整除，结果为整数，向下取整 |
| % | 取模，返回除法的余数 |
| ** | 幂运算，返回第一个数的第二个数次幂 |

```python
a = 10
b = 3
print(a + b) # 输出13，10加3等于13
print(a - b) # 输出7，10减3等于7
print(a * b) # 输出30，10乘3等于30
print(a / b) # 输出3.3333333333333335，10除以3等于3.3333333333333335
print(a // b) # 输出3，10取整除以3等于3
print(a % b) # 输出1，10取模3等于1
print(a ** b) # 输出1000，10的3次幂等于1000
```

### <span style="color:rgb(144,120,249)">赋值运算符</span>
赋值运算符用于将一个值赋给一个变量，除了基本的赋值运算符（=）外，还有一些复合赋值运算符，如+=、-=、*=、/=等，这些运算符在执行赋值的同时还会进行相应的算数运算。

赋值运算符必须连着写，不能分开写，否则会报错
| 运算符 | 说明 |
| --- | --- |
| = | 基本赋值，将右边的值赋给左边的变量 |
| += | 加法赋值，将右边的值加到左边的变量上，并将结果赋给左边的变量 |
| -= | 减法赋值，将右边的值从左边的变量中减去，并将结果赋给左边的变量 |
| *= | 乘法赋值，将左边的变量与右边的值相乘，并将结果赋给左边的变量 |
| /= | 除法赋值，将左边的变量除以右边的值，并将结果赋给左边的变量 |

```python
x = 5
x += 3 # x = x + 3，x的值变为8
x -= 2 # x = x - 2，x的值变为6
x *= 4 # x = x * 4，x的值变为24
x /= 6 # x = x / 6，x的值变为4.0
print(x) # 输出4.0
```

## <span style="color:rgb(255, 146, 18)">输入函数与转义字符</span>
### <span style="color:rgb(144,120,249)">输入函数input()</span>
input()函数用于从用户输入获取数据，默认返回一个字符串类型的值，可以使用int()、float()等函数将输入的字符串转换为其他类型。

```python
name = input("请输入你的名字：") # 提示用户输入名字
age = input("请输入你的年龄：") # 提示用户输入年龄
age = int(age) # 将输入的年龄字符串转换为整数
print(f"你好，{name}！你今年{age}岁。") # 输出用户输入的信息
``` 
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. input()函数会暂停程序的执行，等待用户输入数据并按下回车键
2. input()函数返回的值默认是字符串类型，如果需要其他类型的数据，需要进行类型转换
3. 在使用input()函数时，可以在括号内添加提示信息，帮助用户理解需要输入什么内容
4. 在Python 2.x版本中，input()函数会将输入的内容当作Python代码执行，存在安全风险，建议使用raw_input()函数来获取用户输入的字符串 

### <span style="color:rgb(144,120,249)">转义字符</span>
转义字符是用来表示一些特殊字符的符号，通常以反斜杠（\）开头，后面跟一个字符来表示特定的含义。常见的转义字符包括：
| 转义字符 | 说明 |
| --- | --- |
| \n | 换行符，表示在字符串中换行 |
| \t | 制表符，表示在字符串中插入一个水平制表符 |
| \\\ | 反斜杠，表示在字符串中插入一个反斜杠 |
| \\' | 单引号，表示在字符串中插入一个单引号 |
| \\" | 双引号，表示在字符串中插入一个双引号 |

```python
print("Hello\nWorld") # 输出Hello和World在两行
print("Name:\tAlice") # 输出Name:    Alice，制表符插入一个水平制表符
print("This is a backslash: \\") # 输出This is a backslash: \，反斜杠插入一个反斜杠
print('She said, "Hello!"') # 输出She said, "Hello!"，双引号插入一个双引号
print('It\'s a nice day!') # 输出It's a nice day!，单引号插入一个单引号
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. 转义字符只能在字符串中使用，不能在其他类型的数据中使用
2. 转义字符会被解释为特殊的含义，而不是普通的字符，如果需要在字符串中表示一个反斜杠，需要使用两个反斜杠（\\）来转义
3. 在使用转义字符时，要注意字符串的引号类型，如果字符串使用单引号定义，那么在字符串中使用单引号时需要转义；如果字符串使用双引号定义，那么在字符串中使用双引号时需要转义
4. 在Python 3.6及以上版本中，可以使用原始字符串（raw string）来避免转义字符的解释，原始字符串以r或R前缀定义，字符串中的反斜杠将被视为普通字符，不会被解释为转义字符。
```python
print(r"Hello\nWorld") # 输出Hello\nWorld，原始字符串中的转义字符不会被解释
``` 

## <span style="color:rgb(255, 146, 18)">if判断、比较运算符与逻辑运算符</span>
### <span style="color:rgb(144,120,249)">if判断</span>
if语句用于根据条件执行不同的代码块，基本的if语句结构如下
```python
if 条件:
    代码块
``` 
if语句可以与elif和else语句结合使用，形成多分支的条件判断结构
```python
if 条件1:
    代码块1
elif 条件2:
    代码块2
else:
    代码块3
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. if语句中的条件必须是一个表达式，返回值为True或False
2. if语句中的代码块必须缩进，通常使用4个空格进行缩进
3. if语句可以嵌套使用，即在一个if语句的代码块中再使用另一个if语句
4. elif和else语句是可选的，可以根据需要选择使用
5. if语句的条件可以使用比较运算符和逻辑运算符来组合多个条件
```python
age = 25
if age < 18:
    print("你是未成年人")
elif age < 65:
    print("你是成年人")
else:
    print("你是老年人")
```
### <span style="color:rgb(144,120,249)">比较运算符</span>
比较运算符用于比较两个值之间的关系，返回一个布尔值（True或False）。常见的比较运算符包括：
| 运算符 | 说明 |
| --- | --- |
| == | 等于，判断两个值是否相等 |
| != | 不等于，判断两个值是否不相等 |
| > | 大于，判断左边的值是否大于右边的值 |
| < | 小于，判断左边的值是否小于右边的值 |
| >= | 大于等于，判断左边的值是否大于或等于右边的值 |
| <= | 小于等于，判断左边的值是否小于或等于右边的值 |

```python   
a = 10
b = 5
print(a == b) # 输出False，10不等于5
print(a != b) # 输出True，10不等于5
print(a > b) # 输出True，10大于5
print(a < b) # 输出False，10小于5
print(a >= b) # 输出True，10大于等于5
print(a <= b) # 输出False，10小于等于5
```
### <span style="color:rgb(144,120,249)">逻辑运算符</span>
逻辑运算符用于组合多个条件，返回一个布尔值（True或False）。常见的逻辑运算符包括：
| 运算符 | 说明 |
| --- | --- |
| and | 逻辑与，只有当两个条件都为True时，结果才为True |
| or | 逻辑或，只有当两个条件都为False时，结果才为False |
| not | 逻辑非，取反运算，将True变为False，将False变为True |

```python
age = 25
is_student = True
if age < 30 and is_student:
    print("你是年轻的学生")
if age < 30 or is_student:
    print("你是年轻的学生或是学生")
if not is_student:
    print("你不是学生")
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. 逻辑运算符的优先级：not > and > or，在使用多个逻辑运算符时，可以使用括号来明确运算顺序
2. 逻辑运算符的短路行为：在使用and运算符时，如果第一个条件为False，第二个条件将不会被评估；在使用or运算符时，如果第一个条件为True，第二个条件将不会被评估
3. 逻辑运算符可以与比较运算符结合使用，形成更复杂的条件判断
```python
age = 25
is_student = True
if (age < 30 and is_student) or age > 60:
    print("你是年轻的学生或是老年人")
```

## <span style="color:rgb(255, 146, 18)">if-else、if-elif与if嵌套</span>
### <span style="color:rgb(144,120,249)">if-else</span>
if-else语句用于在条件不满足时执行另一段代码，基本的if-else语句结构如下：
```python
if 条件:
    代码块1
else:
    代码块2
```
```python
age = 25
if age < 18:
    print("你是未成年人")
else:
    print("你是成年人")
```
### <span style="color:rgb(144,120,249)">if-elif</span>
if-elif语句用于在多个条件之间进行选择，基本的if-elif语句结构如下：
```python
if 条件1:
    代码块1
elif 条件2:
    代码块2
elif 条件3:
    代码块3
else:
    代码块4
```
```python
age = 25
if age < 18:
    print("你是未成年人")
elif age < 65:
    print("你是成年人")
else:
    print("你是老年人")
```
### <span style="color:rgb(144,120,249)">if嵌套</span>
if嵌套是指在一个if语句的代码块中再使用另一个if语句，可以实现更复杂的条件判断。基本的if嵌套结构如下：
```python
if 条件1:
    代码块1
    if 条件2:
        代码块2
    else:
        代码块3
else:
    代码块4
```
```python
age = 25
is_student = True
if age < 30:
    if is_student:
        print("你是年轻的学生")
    else:
        print("你是年轻的成年人")
else:
    print("你是老年人")
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. if-else语句只能处理两种情况，而if-elif语句可以处理多种情况，if嵌套可以处理更复杂的条件判断
2. 在使用if-elif语句时，条件的顺序很重要，应该从最具体的条件到最一般的条件进行排列，以确保正确的逻辑判断
3. 在使用if嵌套时，要注意代码的缩进，确保每个if语句的代码块正确地嵌套在一起，以避免逻辑错误和语法错误
4. 在编写复杂的条件判断时，可以考虑使用逻辑运算符来简化代码，避免过多的嵌套层次，提高代码的可读性和维护性
```python
age = 25
is_student = True
if age < 30 and is_student:
    print("你是年轻的学生")
elif age < 30 and not is_student:
    print("你是年轻的成年人")
else:
    print("你是老年人")
```

## <span style="color:rgb(255, 146, 18)">while循环与循环嵌套</span>
### <span style="color:rgb(144,120,249)">while循环</span>
while循环用于在满足条件的情况下重复执行一段代码，基本的while循环结构如下：
```python
while 条件:
    代码块
```
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. while循环会一直执行，直到条件不满足为止，因此要确保循环条件最终会变为False，否则会导致死循环
2. 在while循环中，可以使用break语句来提前退出循环，使用continue语句来跳过当前循环的剩余代码，进入下一次循环
3. while循环可以与else语句结合使用，当循环正常结束（即条件变为False）时，else语句中的代码会被执行
```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("循环结束")
```
### <span style="color:rgb(144,120,249)">循环嵌套</span>
循环嵌套是指在一个循环的代码块中再使用另一个循环，可以实现更复杂的循环结构。基本的循环嵌套结构如下：
```python
while 条件1:
    代码块1
    while 条件2:
        代码块2
```
```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. 循环嵌套会增加代码的复杂性，要注意代码的缩进和逻辑关系，确保每个循环的代码块正确地嵌套在一起，以避免逻辑错误和语法错误
2. 在编写循环嵌套时，可以考虑使用函数来封装内层循环的代码，以提高代码的可读性和维护性
3. 在使用循环嵌套时，要注意循环变量的命名，避免不同层次的循环使用相同的变量名，以免造成混淆和错误
```python
def inner_loop(j):
    while j <= 2:
        print(f"j={j}")
        j += 1
i = 1
while i <= 3:
    j = 1
    inner_loop(j)
    i += 1
```

## <span style="color:rgb(255, 146, 18)">for循环与break、continue关键字</span>
### <span style="color:rgb(144,120,249)">for循环</span>
for循环用于遍历一个序列 <i style="color:rgb(28, 122, 210)">（如列表、字符串、元组等）</i>或其他可迭代对象，基本的for循环结构如下：
```python  
for 变量 in 可迭代对象:
    代码块
```
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
``` 
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. for循环会依次遍历可迭代对象中的每个元素，将当前元素赋值给变量，并执行代码块
2. 在for循环中，可以使用break语句来提前退出循环，使用continue语句来跳过当前循环的剩余代码，进入下一次循环
3. for循环可以与else语句结合使用，当循环正常结束（即遍历完所有元素）时，else语句中的代码会被执行
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("循环结束")
```

### <span style="color:rgb(144,120,249)">range函数</span>
range()函数用于生成一个整数序列，常用于for循环中指定循环的次数或范围。range()函数有三种常用的用法：
1. range(stop)：生成从0到stop-1的整数序列
2. range(start, stop)：生成从start到stop-1的整数序列
3. range(start, stop, step)：生成从start到stop-1的整数序列，步长为step
```python
for i in range(5):
    print(i) # 输出0、1、2、3、4
```
```python
for i in range(1, 5):
    print(i) # 输出1、2、3、4
```
```python
for i in range(1, 10, 2):
    print(i) # 输出1、3、5、7、9
```


### <span style="color:rgb(144,120,249)">break、continue关键字</span>
break语句用于提前退出循环，无论循环条件是否满足，都会立即终止循环
```python
for i in range(1, 10):
    if i == 5:
        break # 当i等于5时，退出循环
    print(i)
```
continue语句用于跳过当前循环的剩余代码，进入下一次循环
```python
for i in range(1, 10):
    if i % 2 == 0:
        continue # 当i是偶数时，跳过当前循环的剩余代码
    print(i) # 输出1、3、5、7、9
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. break语句会立即终止循环，不再执行循环中的任何代码，包括else语句中的代码
```python
for i in range(1, 10):
    if i == 5:
        break # 当i等于5时，退出循环
    print(i)
else:
    print("循环结束") # 不会被执行，因为循环被break语句提前终止了
```
2. continue语句会跳过当前循环的剩余代码，进入下一次循环，但不会终止循环
```python
for i in range(1, 10):
    if i % 2 == 0:
        continue # 当i是偶数时，跳过当前循环的剩余代码
    print(i) # 输出1、3、5、7、9
```
3. 在使用break和continue时，要注意代码的逻辑关系，确保它们在正确的条件下被触发，以避免逻辑错误和语法错误
```python
for i in range(1, 10):
    if i == 5:
        break # 当i等于5时，退出循环
    if i % 2 == 0:
        continue # 当i是偶数时，跳过当前循环的剩余代码
    print(i) # 输出1、3
```

## <span style="color:rgb(255, 146, 18)">字符串编码与字符串常见操作</span>
### <span style="color:rgb(144,120,249)">字符串编码</span>
字符串编码是指将字符串转换为计算机可以理解和处理的二进制数据的过程。常见的字符串编码方式包括ASCII、UTF-8、UTF-16等。Python 3.x默认使用UTF-8编码来处理字符串，可以支持全球范围内的字符集。

#### <span style="color: rgb(170, 206, 62);" >encode</span>
encode()方法用于将字符串编码为指定的字节串，常用的编码方式是UTF-8。

#### <span style="color: rgb(170, 206, 62);" >decode</span>
decode()方法用于将字节串解码回字符串，必须使用与编码时相同的编码方式进行解码。

```python
# 定义一个包含中文字符的字符串
greeting = "你好，世界！"
# 将字符串编码为UTF-8字节串
encoded_greeting = greeting.encode("utf-8")
print(encoded_greeting) # 输出b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'
# 将UTF-8字节串解码回字符串
decoded_greeting = encoded_greeting.decode("utf-8")
print(decoded_greeting) # 输出你好，世界！
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. 在Python 3.x中，字符串是以Unicode编码的，可以包含各种语言的字符，而在Python 2.x中，字符串默认使用ASCII编码，无法直接处理非ASCII字符
2. 在处理字符串编码时，要确保使用正确的编码方式进行编码和解码，以避免出现乱码或错误
3. 在文件操作中，读取和写入文本文件时也需要指定正确的编码方式，以确保文件内容的正确处理
```python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("这是一个示例文本文件。")
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content) # 输出这是一个示例文本文件。
```
### <span style="color:rgb(144,120,249)">字符串常见操作</span>
字符串常见的操作包括连接、切片、格式化、查找、替换等。以下是一些常见的字符串操作示例：

```python
# 字符串连接
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result) # 输出Hello World
# 字符串重复
s = "Hi! "* 3
print(s) # 输出Hi! Hi! Hi!
# 成员检查
s = "Hello, World!"
print("Hello" in s) # 输出True，"Hello"是s的子字符串
print("Python" not in s) # 输出True，"Python"不是s的子字符串
# 字符串切片
s = "Hello, World!"
print(s[0:5]) # 输出Hello，切片从索引0到索引4
print(s[7:]) # 输出World!，切片从索引7到字符串末尾
# 字符串格式化
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old."
print(greeting) # 输出Hello, Alice! You are 30 years old.
# 字符串查找
s = "Hello,World!"
index = s.find("World")
print(index) # 输出6，"World"在字符串中的起始索引位置
print(s.find("o",3,4)) # 输出-1，在索引3到4之间没有找到"o"
print(s.find("o",4,9)) # 输出4，在索引4到9之间找到"o" 
# 字符串替换
s = "Hello, World!"
new_s = s.replace("World", "Python")
print(new_s) # 输出Hello, Python!
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. 字符串连接可以使用加号（+）运算符，但要注意字符串必须加上引号，否则会被当作变量名，导致错误
2. 字符串切片的索引从0开始，切片的结束索引是非包含性的，即切片不包括结束索引位置的字符(巧记：左包右不包)
3. 字符串格式化可以使用f-string、str.format()方法或百分号（%）格式化，根据需要选择合适的方式进行格式化输出
```python
name = "Alice"
age = 30
greeting1 = f"Hello, {name}! You are {age} years old." # 使用f-string进行格式化输出
greeting2 = "Hello, {}! You are {} years old.".format(name, age) # 使用str.format()方法进行格式化输出
greeting3 = "Hello, %s! You are %d years old." % (name, age) # 使用百分号（%）格式化进行格式化输出
print(greeting1) # 输出Hello, Alice! You are 30 years old.
print(greeting2) # 输出Hello, Alice! You are 30 years old.
print(greeting3) # 输出Hello, Alice! You are 30 years old.
```
4. 字符串查找可以使用find()方法，如果要查找的子字符串不存在，find()方法会返回-1
```python
s = "Hello, World!"
index = s.find("Python")
print(index) # 输出-1，"Python"在字符串中不存在
```
5. 字符串替换可以使用replace()方法，返回一个新的字符串，原字符串保持不变
```python
s = "Hello, World!"
new_s = s.replace("Python", "Java")
print(new_s) # 输出Hello, World!，因为"Python"在字符串中不存在，所以没有进行替换
```

## <span style="color:rgb(255, 146, 18)">字符串的查找、判断、修改</span>
### <span style="color:rgb(144,120,249)">字符串的查找</span>
字符串的查找可以使用find()方法、index()方法和in运算符等来实现。find()方法返回子字符串在字符串中的起始索引位置，如果子字符串不存在，则返回-1；index()方法与find()方法类似，但如果子字符串不存在，会抛出ValueError异常；in运算符用于检查子字符串是否存在于字符串中，返回True或False。

```python
s = "Hello, World!"
# 使用find()方法查找子字符串
index = s.find("World")
print(index) # 输出7，"World"在字符串中的起始索引位置
# 使用index()方法查找子字符串
try: # 如果"Python"在字符串中不存在，会抛出ValueError异常
    index = s.index("Python")
    print(index)
except ValueError: # 捕获ValueError异常，表示子字符串不存在
    print("子字符串不存在") # 输出子字符串不存在，"Python"在字符串中不存在
# 使用in、not in运算符检查子字符串是否存在
print("Hello" in s) # 输出True，"Hello"是s的子字符串
print("Python" not in s) # 输出True，"Python"不是s的子字符串
```
#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. find()方法和index()方法的区别在于当子字符串不存在时，find()方法返回-1，而index()方法会抛出ValueError异常，<i style="color: rgb(28, 122, 210);">因此在使用index()方法时需要进行异常处理</i> 
2. in运算符用于检查子字符串是否存在于字符串中，返回True或False，可以用于条件判断中
```python
s = "Hello, World!"
if "Hello" in s:
    print("字符串中包含Hello") # 输出字符串中包含Hello
else:
    print("字符串中不包含Hello")
```
3. 字符串的查找操作是区分大小写的，如果需要进行不区分大小写的查找，可以将字符串转换为统一的大小写后再进行查找
```python
s = "Hello,World!"
index = s.lower().find("world")
print(index) # 输出6，"world"在字符串中的起始索引位置，忽略大小写
```
### <span style="color:rgb(144,120,249)">count计数</span>
count()方法用于统计子字符串在字符串中出现的次数，返回一个整数值。
```python
s = "Hello, World! Hello!"
count = s.count("Hello")
print(count) # 输出2，"Hello"在字符串中出现了两次
```

### <span style="color:rgb(144,120,249)">字符串的判断</span>
字符串的判断可以使用isalpha()方法、isdigit()方法、isspace()方法等来实现。
1. isalpha()方法用于判断字符串是否只包含字母字符；
2. isdigit()方法用于判断字符串是否只包含数字字符；
3. isspace()方法用于判断字符串是否只包含空白字符。
```python
s1 = "Hello"
s2 = "12345"
s3 = "   "
# 判断字符串是否只包含字母字符
print(s1.isalpha()) # 输出True，s1只包含字母字符
print(s2.isalpha()) # 输出False，s2包含数字字符
# 判断字符串是否只包含数字字符
print(s1.isdigit()) # 输出False，s1包含字母字符
print(s2.isdigit()) # 输出True，s2只包含数字字符
# 判断字符串是否只包含空白字符
print(s1.isspace()) # 输出False，s1包含字母字符
print(s3.isspace()) # 输出True，s3只包含空白字符
```
4. startwith()方法用于判断字符串是否以指定的子字符串开头；
```python
print(s1.startswith("He")) # 输出True，s1以"He"开头
print(s1.startswith("he")) # 输出False，s1不以"he"开头，区分大小写
print(s1.startswith("he",3,6)) # 输出False，在索引3到6（不包括6）之间s1不以"he"开头
```
5. endwith()方法用于判断字符串是否以指定的子字符串结尾。
```python
print(s1.endswith("lo")) # 输出True，s1以"lo"结尾
print(s1.endswith("LO")) # 输出False，s1不以"LO"结尾，区分大小写
print(s1.endswith("LO",0,5)) # 输出False，在索引0到5（不包括5）之间s1不以"LO"结尾
```
6. isupper()方法用于判断字符串是否只包含大写字母字符；
```python
s1 = "Hello"
print(s1.isupper()) # 输出False，s1不只包含大写字母字符
```
7. islower()方法用于判断字符串是否只包含小写字母字符。
```python
s1 = "Hello"
print(s1.islower()) # 输出False，s1不只包含小写字母
```


#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. isalpha()方法、isdigit()方法和isspace()方法都是字符串对象的方法，只能用于字符串类型的数据，如果对非字符串类型的数据调用这些方法，会抛出AttributeError异常
```python
num = 12345
print(num.isdigit()) # 会抛出AttributeError异常，因为num不是字符串类型
```
2. 这些方法的判断是基于字符串中的每个字符进行的，如果字符串中包含非字母、非数字或非空白字符，这些方法将返回False
```python
s = "Hello123"
print(s.isalpha()) # 输出False，s包含数字字符
print(s.isdigit()) # 输出False，s包含字母字符
```
3. 这些方法对于空字符串的判断结果是False，因为空字符串不包含任何字符
```python   
s = ""
print(s.isalpha()) # 输出False，空字符串不包含字母字符
print(s.isdigit()) # 输出False，空字符串不包含数字字符
print(s.isspace()) # 输出False，空字符串不包含空白字符
``` 
### <span style="color:rgb(144,120,249)">字符串的修改</span>
字符串的修改可以使用replace()、strip()、split()、upper()、lower()、capitalize()等方法来实现。
replace()方法用于替换字符串中的指定子字符串；
```python
s = "Hello, World!"
new_s = s.replace("World", "Python")
print(new_s) # 输出Hello, Python!
```

strip()方法用于去除字符串两端的空白字符；
```python
s = "  Hello, World!  "
stripped_s = s.strip()
print(stripped_s) # 输出Hello, World!
```

split()方法用于将字符串分割成一个列表，默认以空白字符为分隔符；
```python
s = "Hello, World!"
split_s = s.split(',') # 以逗号为分隔符进行分割
print(split_s) # 输出['Hello,', 'World!']
print(s.split()) # 以空白字符为分隔符进行分割，输出['Hello,', 'World!']
print(s.split('o')) # 以字母'o'为分隔符进行分割，输出['Hell', ', W', 'rld!']
print(s.split('o', 1)) # 以字母'o'为分隔符进行分割，最多分割一次，输出['Hell', ', World!']
``` 

upper()方法用于将字符串转换为大写字母；
```python
s = "  Hello, World!  "
upper_s = s.upper()
print(upper_s) # 输出  HELLO, WORLD!
```

lower()方法用于将字符串转换为小写字母。
```python
s = "  Hello, World!  "
lower_s = s.lower()
print(lower_s) # 输出  hello, world!
```
capitalize()方法用于将字符串的首字母转换为大写，其他字母转换为小写。
```python
s = "hELLO, wORLD!"
capitalized_s = s.capitalize()
print(capitalized_s) # 输出Hello, world!
```

#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. replace()方法返回一个新的字符串，原字符串保持不变，如果要修改原字符串，需要将返回的新字符串赋值给原变量
```python
s = "Hello, World!"
s = s.replace("World", "Python") # 将替换后的字符串赋值给原变量s
print(s) # 输出Hello, Python!
```
2. strip()方法只会去除字符串两端的空白字符，如果需要去除字符串中间的空白字符，可以使用replace()方法将空白字符替换为空字符串
```python
s = "  Hello, World!  "
stripped_s = s.strip() # 去除两端的空白字符
print(stripped_s) # 输出Hello, World!
no_space_s = s.replace(" ", "") # 去除字符串中所有的空白字符
print(no_space_s) # 输出Hello,World!
```
3. upper()方法和lower()方法返回一个新的字符串，原字符串保持不变，如果要修改原字符串，需要将返回的新字符串赋值给原变量
```python
s = "Hello, World!"
s = s.upper() # 将字符串转换为大写字母并赋值给原变量s
print(s) # 输出HELLO, WORLD!
s = s.lower() # 将字符串转换为小写字母并赋值给原变量s
print(s) # 输出hello, world!
```

## <span style="color:rgb(255, 146, 18)">列表</span>
列表是一种有序、可变的集合类型，可以包含任意类型的元素。列表使用方括号（[]）定义，元素之间用逗号分隔。以下是一些常见的列表操作示例：

```python
# 定义一个列表
fruits = ["apple", "banana", "cherry"]
# 查找列表元素
print("banana" in fruits) # 输出True，"banana"是fruits列表的元素
print("orange" not in fruits) # 输出True，"orange"不是fruits列表的元素

# 访问列表元素
print(fruits[0]) # 输出apple，访问列表的第一个元素
print(fruits[1]) # 输出banana，访问列表的第二个元素
print(fruits[-1]) # 输出cherry，访问列表的最后一个元素

# 修改列表元素
fruits[1] = "blueberry" # 将列表的第二个元素修改为"blueberry"
print(fruits) # 输出['apple', 'blueberry', 'cherry']

# 添加元素到列表
fruits.append("orange") # 在列表末尾添加一个元素"orange"
print(fruits) # 输出['apple', 'blueberry', 'cherry', 'orange']
fruits.insert(1, "grape") # 在列表的索引1位置插入元素"grape"
print(fruits) # 输出['apple', 'grape', 'blueberry', 'cherry', 'orange']

# 删除列表元素
fruits.remove("blueberry") # 删除列表中的元素"blueberry"
print(fruits) # 输出['apple', 'grape', 'cherry', 'orange']
del fruits[0] # 删除列表中的第一个元素
print(fruits) # 输出['grape', 'cherry', 'orange']

# 列表切片
print(fruits[0:2]) # 输出['grape', 'cherry']，切片从索引0到索引1（不包括2）
print(fruits[1:3]) # 输出['cherry', 'orange']，切片从索引1到索引2（不包括3）
print(fruits[:2]) # 输出['grape', 'cherry']，切片从列表开头到索引1（不包括2）
print(fruits[1:3]) # 输出['cherry', 'orange']，切片从索引1到索引2（不包括3）
print(fruits[1:4]) # 输出['cherry', 'orange']，切片从索引1到索引3（不包括4）

# 列表是可迭代的，可以使用for循环遍历列表中的元素
for fruit in fruits:
    print(fruit) # 输出grape、cherry、orange

# index、count方法，跟字符串的用法一样
print(fruits.index("cherry")) # 输出0，"cherry"在列表中的索引位置
print(fruits.count("orange")) # 输出1，"orange"在列表中出现了1次

#列表排序sort()
fruits.sort() # 对列表进行升序排序
print(fruits) # 输出['cherry', 'grape', 'orange']
fruits.sort(reverse=True) # 对列表进行降序排序
print(fruits) # 输出['orange', 'grape', 'cherry']
```
### <span style="color:rgb(144,120,249)">列表推导式</span>
列表推导式是一种简洁的语法，用于创建新的列表。它可以通过一个表达式和一个可迭代对象来生成一个新的列表。基本的列表推导式结构如下：
```python
new_list = [表达式 for 变量 in 可迭代对象 if 条件] 
#in后面不仅可以是列表，还可以是range()函数生成的序列、字符串等可迭代对象
```

```python
# 创建一个包含1到10之间偶数的列表
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers) # 输出[2, 4, 6, 8, 10]
``` 
### <span style="color:rgb(144,120,249)">列表嵌套</span>
列表嵌套是指在一个列表中包含另一个列表，可以实现更复杂的数据结构。基本的列表嵌套结构如下：
```python  
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0]) # 输出[1, 2, 3]，访问嵌套列表的第一个元素
print(nested_list[1][2]) # 输出6，访问嵌套列表中的第二个列表的第三个元素
```

#### <span style="color: rgb(255, 0, 0);" >注意</span>
1. 列表中的元素可以是任意类型，包括数字、字符串、布尔值、列表等，列表可以包含不同类型的元素
2. 列表是有序的集合类型，元素的顺序是固定的，可以通过索引访问和修改列表中的元素
3. 列表是可变的集合类型，可以修改列表中的元素，添加新的元素或删除现有的元素
4. 列表的索引从0开始，负数索引表示从列表的末尾开始访问元素，-1表示最后一个元素，-2表示倒数第二个元素，以此类推
5. 在使用列表操作时，要注意索引的范围，避免出现IndexError异常
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[3]) # 会抛出IndexError异常，因为索引3超出列表的范围
``` 
