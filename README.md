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
| \\ | 反斜杠，表示在字符串中插入一个反斜杠 |
| \' | 单引号，表示在字符串中插入一个单引号 |
| \" | 双引号，表示在字符串中插入一个双引号 |

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

