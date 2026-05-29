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
2. 缩进错误：print要定格写，否则就报错
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

```python
# 定义字符串变量
name = "Alice"
greeting = 'Hello, ' + name + '!' # 字符串连接
print(greeting) # 输出Hello, Alice!
```

字符串切片可以使用索引来获取字符串的部分内容：

```python   
name = "Alice"
print(name[0]) # 输出第一个字符A
print(name[1:4]) # 输出从索引1到索引3的字符lice
print(name[-1]) # 输出最后一个字符e
```


