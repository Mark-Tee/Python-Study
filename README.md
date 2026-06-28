# 🐍 Python 学习笔记

> 从零开始学 Python，面向对象解释型高级编程语言。适合入门查阅和快速复习。

---

## 📑 目录

1. [了解 Python](#1-了解-python)
2. [注释与输出](#2-注释与输出)
3. [变量与标识符](#3-变量与标识符)
4. [数值与字符串](#4-数值与字符串)
5. [运算符](#5-运算符)
6. [输入与转义](#6-输入与转义)
7. [if 条件判断](#7-if-条件判断)
8. [if 分支与嵌套](#8-if-分支与嵌套)
9. [while 循环](#9-while-循环)
10. [for 循环](#10-for-循环)
11. [字符串编码与操作](#11-字符串编码与操作)
12. [字符串方法](#12-字符串方法)
13. [列表](#13-列表)
14. [元组](#14-元组)
15. [字典](#15-字典)
16. [集合](#16-集合)
17. [函数基础](#17-函数基础)
18. [类型转换](#18-类型转换)
19. [深浅拷贝与可变/不可变类型](#19-深浅拷贝与可变不可变类型)
20. [速查表与常见面试题](#20-速查表与常见面试题)

---

## 1. 了解 Python

### Python 简介

> **编程语言**是用来定义计算机程序的语言，用来向计算机发出指令。

> **Python** 是一种**面向对象**的**解释型**高级编程语言。它是强类型的动态脚本语言。

| 特性 | 说明 |
|------|------|
| 面向对象 | 一切皆对象，支持封装、继承、多态 |
| 解释型 | 无需编译，解释器逐行执行 |
| 强类型 | 不同类型之间操作需显式转换 |
| 动态语言 | 变量无需声明类型，运行时确定 |

### 编译型 vs 解释型语言

| | 编译型 (C/C++/Go) | 解释型 (Python/JS/Ruby) |
|---|---|---|
| **执行方式** | 先编译为机器码，再运行 | 运行时逐行翻译执行 |
| **运行速度** | 快 | 相对慢 |
| **跨平台** | 需分别编译 | 一次编写，到处运行（需对应解释器） |
| **调试** | 编译时发现错误 | 运行时发现错误 |

### 编写第一个程序

```python
print("Hello World")
```

> ⚠️ **常见错误**

| 错误类型 | 说明 | 示例 |
|----------|------|------|
| 输入错误 | 符号必须使用**英文模式** | `print（"Hello"）` ❌ → `print("Hello")` ✅ |
| 缩进错误 | `print` 必须顶格写 | `  print("Hello")` ❌ → `print("Hello")` ✅ |
| 语法错误 | 每条语句独立一行，`SyntaxError` 说明语法有问题 | — |
| 命名错误 | 字符串必须加引号（单引号或双引号均可） | `print(Hello)` ❌ → `print("Hello")` ✅ |

---

## 2. 注释与输出

### 注释

注释可以放在任意位置，内容不会被程序执行。

```python
# 这是一个单行注释，使用 # 符号开头

"""
这是一个多行注释（文档字符串）
使用三个双引号或三个单引号包裹
可以写多行内容
"""

'''
这也是多行注释
使用三个单引号
'''
```

> 💡 **最佳实践**：复杂逻辑务必写注释，注释解释"为什么这样做"而非"做了什么"。

### 输出函数 `print()`

`print()` 用于将内容输出到控制台，可以输出字符串、数字、变量等。

```python
print("Hello World")   # 输出字符串
print(123)             # 输出数字
name = "Alice"
print(name)            # 输出变量
```

### 核心参数详解

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `sep` | 多个值之间的分隔符 | `" "` (空格) |
| `end` | 输出结束时的字符 | `"\n"` (换行) |

```python
# sep 参数：指定多个输出值之间的分隔符
print("Hello", "World", sep="-")   # → Hello-World
print("Hello", "World", sep="")    # → HelloWorld
print(2024, 6, 6, sep="/")         # → 2024/6/6

# end 参数：指定输出结束时的字符（默认为换行符 \n）
print("Hello", end="")   # 不换行
print("World")           # 继续在同一行 → HelloWorld

print("Loading", end="...")
print("Done!")           # → Loading...Done!

# 组合使用
print("A", "B", "C", sep=", ", end=".\n")  # → A, B, C.
```

---

## 3. 变量与标识符

### 变量

> 变量是用来**存储数据的容器**，可以在程序中使用变量来保存和操作数据。

**变量的作用：**
- 存储不同类型的数据（数字、字符串、布尔值等）
- 在程序中被修改和更新
- 提高代码的可读性和可维护性
- 在函数之间传递数据

```python
name = "Alice"     # 字符串变量
age = 30           # 整数变量
height = 1.75      # 浮点数变量
is_student = True  # 布尔变量

print(name)        # Alice
print(age)         # 30
print(height)      # 1.75
```

> ⚠️ **变量命名规则**

| 规则 | 正确示例 | 错误示例 |
|------|----------|----------|
| 以字母或下划线开头 | `name`, `_count` | `1name`, `@var` |
| 不能使用保留字 | `my_if` | `if`, `for`, `while` |
| 区分大小写 | `Name` ≠ `name` | — |
| 先定义后使用 | `x = 1; print(x)` | `print(x)` (未定义) |

```python
name = "Alice"
print(name)       # Alice
name = "Bob"      # 修改变量的值
print(name)       # Bob
```

> 💡 **Python 保留字速查**：`False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield`

### 标识符

> 标识符是用来命名**变量、函数、类**等的名称。

**命名规则与变量相同**（见上表），额外强调：标识符应该具有描述性，能清晰表达用途。

### 常用命名方法（编码习惯）

| 命名法 | 规则 | 适用场景 | 示例 |
|--------|------|----------|------|
| **下划线分割法** (snake_case) | 小写字母 + 下划线 | 变量、函数 | `my_variable`, `get_user_name()` |
| **大驼峰命名法** (PascalCase) | 每个单词首字母大写 | 类名 | `MyClass`, `StudentManager` |
| **小驼峰命名法** (camelCase) | 首单词小写，其余首字母大写 | 不推荐 Python 中使用 | `myFunction` |

```python
# ✅ Python 推荐写法
my_variable = 42                     # snake_case 用于变量
def calculate_average(scores):       # snake_case 用于函数
    pass

class StudentRecord:                 # PascalCase 用于类
    pass
```

---

## 4. 数值与字符串

### 数值类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `int` | 整数（无大小限制） | `30`, `-5`, `0` |
| `float` | 浮点数（双精度） | `1.75`, `-0.5`, `3.14` |
| `complex` | 复数 | `2 + 3j`, `1 - 4j` |
| `bool` | 布尔值（`int` 的子类） | `True`(1), `False`(0) |

```python
age = 30
height = 1.75
is_student = True
c1 = 2 + 3j
c2 = 1 + 4j

print(age)              # 30
print(height)           # 1.75
print(c1 + c2)          # (3+7j)
print(is_student)       # True

# 布尔值可参与数学运算
print(True + 1)         # 2 (True 当作 1)
print(False * 100)      # 0 (False 当作 0)
```

> ⚠️ **注意**
> - 整数和浮点数混合运算结果为**浮点数**
> - 布尔值必须首字母大写 `True` / `False`
> - 使用 `type()` 函数检测变量类型

```python
print(type(30))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>
print(type(2 + 3j))   # <class 'complex'>
```

### 字符串

> 字符串是由一系列字符组成的文本数据，使用单引号、双引号或三引号定义。

```python
s1 = 'Hello'           # 单引号
s2 = "Hello"           # 双引号
s3 = '''多行
字符串'''             # 三引号（可跨行）
s4 = """也是多行
字符串"""
```

> ⚠️ **注意**：多行注释（三引号未被赋值）vs 多行字符串（三引号被赋值给变量），前者不执行，后者是字符串数据。

```python
# 字符串连接
name = "Alice"
greeting = "Hello, " + name + "!"   # → Hello, Alice!

# ❌ 常见错误：忘记加引号
# name1 = xuduo   → NameError: name 'xuduo' is not defined
```

### 格式化输出

### 方法一：% 占位符格式化

| 占位符 | 说明 | 示例 |
|--------|------|------|
| `%s` | 字符串 | `"Hello, %s" % "Alice"` |
| `%d` | 整数 | `"Age: %d" % 30` |
| `%f` | 浮点数（默认6位小数） | `"Pi: %f" % 3.14` |
| `%.nf` | 保留 n 位小数（四舍五入） | `"Pi: %.2f" % 3.14159` → `3.14` |
| `%nd` | 整数占 n 个字符宽度 | `"%4d" % 5` → `   5` |
| `%%` | 输出百分号本身 | `"%.1f%%" % 99.9` → `99.9%` |

```python
name = "Alice"
age = 30
print("Hello, %s! You are %d years old." % (name, age))
# → Hello, Alice! You are 30 years old.

pi = 3.1415926535
print("Pi: %.2f" % pi)      # → Pi: 3.14
print("Age: %4d" % 5)        # → Age:    5
print("%.1f%%" % 99.9)       # → 99.9%
```

### 方法二：`str.format()`

```python
name = "Alice"
age = 30
print("Hello, {}! You are {} years old.".format(name, age))
print("Hello, {1}! You are {0} years old.".format(age, name))   # 按索引
print("Hello, {n}! You are {a} years old.".format(n=name, a=age))  # 按关键字
```

### 方法三：f-string ⭐ (Python 3.6+，最推荐)

```python
name = "Alice"
age = 30
print(f"Hello, {name}! You are {age} years old.")
# → Hello, Alice! You are 30 years old.

pi = 3.1415926535
print(f"Pi: {pi:.2f}")       # → Pi: 3.14

# f-string 中还可以写表达式
print(f"Next year: {age + 1}")   # → Next year: 31
```

> 💡 **推荐**：格式化优先使用 **f-string**，简洁高效，可读性最佳。

---

## 5. 运算符

### 算数运算符

| 运算符 | 说明 | 示例 (`a=10, b=3`) | 结果 |
|--------|------|---------------------|------|
| `+` | 加法 | `a + b` | `13` |
| `-` | 减法 | `a - b` | `7` |
| `*` | 乘法 | `a * b` | `30` |
| `/` | 除法 | `a / b` | `3.333...` (始终为 float) |
| `//` | 取整除（向下取整） | `a // b` | `3` |
| `%` | 取模（余数） | `a % b` | `1` |
| `**` | 幂运算 | `a ** b` | `1000` |

```python
a, b = 10, 3
print(a / b)    # 3.3333333333333335
print(a // b)   # 3    ← 注意：向下取整
print(-10 // 3) # -4   ← 向下取整，不是 -3！
print(a % b)    # 1
print(a ** b)   # 1000

# 优先级：** > * / // % > + -
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20   ← 用括号明确优先级
```

### 赋值运算符

> 赋值运算符**必须连着写**，不能分开。

| 运算符 | 等价于 | 示例 (`x=5`) | 结果 |
|--------|--------|---------------|------|
| `=` | 基本赋值 | `x = 5` | `5` |
| `+=` | `x = x + n` | `x += 3` | `8` |
| `-=` | `x = x - n` | `x -= 2` | `6` |
| `*=` | `x = x * n` | `x *= 4` | `24` |
| `/=` | `x = x / n` | `x /= 6` | `4.0` |
| `//=` | `x = x // n` | `x //= 2` | `2` |
| `%=` | `x = x % n` | `x %= 3` | `2` |
| `**=` | `x = x ** n` | `x **= 3` | `8` |

```python
x = 5
x += 3   # x = 8
x -= 2   # x = 6
x *= 4   # x = 24
x /= 6   # x = 4.0
print(x) # 4.0
```

---

## 6. 输入与转义

### 输入函数 `input()`

> `input()` 从用户获取输入，**始终返回字符串类型**。

```python
name = input("请输入你的名字：")    # 用户输入 → 返回字符串
age = input("请输入你的年龄：")     # 用户输入 → 返回字符串
age = int(age)                      # 转换为整数
print(f"你好，{name}！你今年 {age} 岁。")
```

> ⚠️ **注意**
> - `input()` 会**暂停程序**，等待用户输入并按下回车
> - 返回值**默认是字符串**，需要时进行类型转换
> - `int()` / `float()` 转换失败会抛出 `ValueError`

```python
# 类型转换
age = int(input("年龄："))         # 一步到位：输入 → 转整数
height = float(input("身高(m)："))  # 输入 → 转浮点数
score = eval(input("分数："))       # eval 自动推断类型（有安全风险，慎用）
```

### 转义字符

> 转义字符以 `\` 开头，表示特殊含义。

| 转义字符 | 说明 |
|----------|------|
| `\n` | 换行 |
| `\t` | 水平制表符 (Tab) |
| `\\` | 反斜杠本身 |
| `\'` | 单引号 |
| `\"` | 双引号 |
| `\r` | 回车 |
| `\uXXXX` | Unicode 字符 (如 `中` → 中) |

```python
print("Hello\nWorld")          # 两行输出
print("Name:\tAlice")          # Name:    Alice
print("Path: C:\\Users\\me")   # Path: C:\Users\me
print('It\'s a nice day!')     # It's a nice day!

# 原始字符串（raw string）：\ 不被转义
print(r"Hello\nWorld")         # Hello\nWorld （原样输出）
```

---

## 7. if 条件判断

### if 判断

```python
if 条件:
    代码块     # 条件为 True 时执行
```

```python
age = 25
if age < 18:
    print("未成年")
elif age < 65:
    print("成年")
else:
    print("老年")
```

> ⚠️ **注意**：条件表达式返回 `True` 或 `False`；代码块必须**缩进**（通常 4 个空格）；条件中空容器、`0`、`None` 视为 `False`。

### 比较运算符

| 运算符 | 说明 | 示例 (`a=10,b=5`) |
|--------|------|--------------------|
| `==` | 等于 | `a == b` → `False` |
| `!=` | 不等于 | `a != b` → `True` |
| `>` | 大于 | `a > b` → `True` |
| `<` | 小于 | `a < b` → `False` |
| `>=` | 大于等于 | `a >= b` → `True` |
| `<=` | 小于等于 | `a <= b` → `False` |
| `is` | 身份判断（是否为同一对象） | `a is None` |
| `in` | 成员判断 | `"a" in "abc"` → `True` |

> 💡 链式比较：`1 < x < 10` 等价于 `x > 1 and x < 10`

### 逻辑运算符

| 运算符 | 说明 | 短路行为 |
|--------|------|----------|
| `and` | 逻辑与（全真才真） | 左边为 `False` 时右边不执行 |
| `or` | 逻辑或（有真即真） | 左边为 `True` 时右边不执行 |
| `not` | 逻辑非（取反） | — |

> 优先级：`not` > `and` > `or`。不确定时用括号！

```python
age = 25
is_student = True

if age < 30 and is_student:
    print("年轻的学生")

if age < 30 or is_student:
    print("年轻或者是学生")   # 总会执行

if not is_student:
    print("不是学生")

# 短路行为实战
name = ""
default_name = name or "Anonymous"   # → "Anonymous"（name 为空串等价 False）
print(default_name)

# 复杂条件用括号明确意图
if (age < 30 and is_student) or age > 60:
    print("年轻学生或老年人")
```

---

## 8. if 分支与嵌套

### if-else

```python
if 条件:
    代码块1      # 条件为 True
else:
    代码块2      # 条件为 False
```

### if-elif（多分支）

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"成绩等级：{grade}")   # B
```

> ⚠️ **条件顺序很重要**：从最具体到最一般排列。如果把 `score >= 60` 放在最前面，后面的分支永远不会执行！

### if 嵌套

```python
age = 25
is_student = True

if age < 30:
    if is_student:
        print("年轻的学生")
    else:
        print("年轻的成年人")
else:
    print("30岁以上")
```

> 💡 **最佳实践**：嵌套层次不要超过 3 层，否则应使用逻辑运算符简化或提取函数。

```python
# ❌ 深层嵌套
if a:
    if b:
        if c:
            do_something()

# ✅ 用逻辑运算符扁平化
if a and b and c:
    do_something()

# ✅ 提前返回（在函数中）
def check(age, is_student):
    if age >= 30:
        return "30岁以上"
    if is_student:
        return "年轻的学生"
    return "年轻的人"
```

---

## 9. while 循环

### while 循环

```python
while 条件:
    代码块     # 条件为 True 时重复执行
```

```python
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
# → 0 1 2 3 4
```

> ⚠️ **避免死循环**：确保循环条件最终会变为 `False`。

### while-else

```python
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("循环正常结束")   # 未被 break 打断时执行
```

| 场景 | else 是否执行 |
|------|---------------|
| 条件自然变为 False | ✅ 执行 |
| `break` 退出 | ❌ 不执行 |

### 循环嵌套

```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
# 输出 6 行：每个 i 对应 2 个 j
```

> 💡 嵌套循环的时间复杂度是 **O(n × m)**，注意性能。善用函数封装内层循环提高可读性。

---

## 10. for 循环

### for 循环

```python
for 变量 in 可迭代对象:
    代码块
```

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "Python":
    print(char, end=" ")   # → P y t h o n
```

### for-else：循环未被 `break` 打断时执行 else

```python
for fruit in fruits:
    print(fruit)
else:
    print("遍历完毕")
```

### `range()` 函数

| 用法 | 说明 |
|------|------|
| `range(stop)` | 0 → stop-1 |
| `range(start, stop)` | start → stop-1 |
| `range(start, stop, step)` | start → stop-1，步长为 step |

```python
for i in range(5):            # 0, 1, 2, 3, 4
    print(i, end=" ")

for i in range(1, 5):         # 1, 2, 3, 4
    print(i, end=" ")

for i in range(1, 10, 2):     # 1, 3, 5, 7, 9
    print(i, end=" ")

# 倒序
for i in range(10, 0, -1):    # 10, 9, 8, ..., 1
    print(i, end=" ")
```

### `break` 与 `continue`

| 关键字 | 作用 |
|--------|------|
| `break` | 立即**终止**整个循环（不执行 else） |
| `continue` | 跳过当前迭代剩余代码，进入**下一次**循环 |

```python
# break：遇到 5 就停止
for i in range(1, 10):
    if i == 5:
        break
    print(i, end=" ")    # → 1 2 3 4

# continue：跳过偶数
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i, end=" ")    # → 1 3 5 7 9
```

> ⚠️ `break` 和 `continue` 只作用于**最近一层**循环，不影响外层。

### 练习常见错误

**❌ 错误 1：`return` 写在循环里面**

遍历检查时，`return 0` 写在 `for` 里面会导致只检查第一个元素就返回：

```python
# ❌ return 0 在循环里面 → 第一个不匹配就返回了
def check_upper(password):
    for char in password:
        if char.isupper():
            return 2
        return 0        # ← 跟 if 对齐 = 在循环体里！

# ✅ return 0 在循环外面（和 for 对齐）→ 全部遍历完再返回
def check_upper(password):
    for char in password:
        if char.isupper():
            return 2
    return 0            # ← 和 for 对齐 = 循环结束后才执行
```

> 💡 **重点**：`return` 会立即结束整个函数。循环中找到目标就 `return`，找不到就等循环跑完后 `return 0`。

**❌ 错误 2：循环中的 else 导致重复输出**

不要把"没找到"的提示写在循环内部，否则每个不匹配的元素都输出一次：

```python
# ❌ 遍历中每个不匹配项都打印"没有结果"
for name, phone in contacts.items():
    if keyword in name:
        print(f"匹配：{name}")
    else:
        print("没有结果")       # ← 匹配一个，打印 N-1 次"没有结果"

# ✅ 先收集匹配项，循环结束后再一次性判断
results = []
for name, phone in contacts.items():
    if keyword in name or keyword in phone:
        results.append((name, phone))

if results:
    for name, phone in results:
        print(f"匹配：{name}")
else:
    print("没有结果")            # ← 只输出一次
```

---

## 11. 字符串编码与操作

### 字符串编码

> Python 3.x 默认使用 **Unicode (UTF-8)** 编码，支持全球字符。

```python
text = "你好，世界！"

# 编码：字符串 → 字节串 (bytes)
encoded = text.encode("utf-8")
print(encoded)   # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'

# 解码：字节串 → 字符串
decoded = encoded.decode("utf-8")
print(decoded)   # 你好，世界！
```

> ⚠️ **编码和解码必须使用同一编码方式**，否则出现乱码（典型：UTF-8 vs GBK）。

```python
# 文件读写务必指定编码
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("这是一个示例文本文件。")

with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### 字符串常见操作

```python
# 连接
s = "Hello" + " " + "World"      # → Hello World

# 重复
s = "Hi! " * 3                   # → Hi! Hi! Hi!

# 成员检查
print("Hello" in "Hello, World!")       # True
print("Python" not in "Hello, World!")  # True

# 切片 [start:stop:step]
s = "Hello, World!"
print(s[0:5])     # Hello  （索引 0~4，左闭右开）
print(s[7:])      # World! （从索引 7 到末尾）
print(s[:5])      # Hello  （从开头到索引 4）
print(s[::-1])    # !dlroW ,olleH （反转字符串）

# 查找
s = "Hello, World!"
print(s.find("World"))    # 7  （首次出现索引，找不到返回 -1）
print(s.rfind("o"))       # 8  （从右侧查找）

# 替换
s = "Hello, World!"
print(s.replace("World", "Python"))  # → Hello, Python!
```

> 💡 **切片口诀**：`[起点:终点:步长]`，左闭右开，省略起点默认 0，省略终点默认末尾。

### 文件读写

> `open()` 打开文件，`with` 自动关闭。`"r"` 读，`"w"` 写，`encoding="utf-8"` 防乱码。

**读文件的固定模板：**

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()      # 去掉 \n，必做！
        if not line:             # 跳过空行
            continue
        # 处理 line...
```

**写文件的固定模板：**

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("内容\n")            # 手动加 \n
```

**读 → 处理 → 写 完整流水线：**

```python
# 1. 读
students = []
with open("scores.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, score = line.split(",")          # "张三,85" → name="张三", score="85"
        students.append((name, int(score)))    # 字符串转整数

# 2. 处理
total = len(students)
score_sum = sum(x[1] for x in students)        # 提取第二列求和
top_name, top_score = max(students, key=lambda x: x[1])

# 3. 写
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("=== 报告 ===\n")
    f.write(f"总人数: {total}\n")
    f.write(f"总分: {score_sum}\n")
    f.write(f"最高分: {top_name} ({top_score}分)\n")
```

| 模式 | 写法 | 场景 |
|------|------|------|
| 提取元组第 N 列 | `[x[N] for x in list]` | 总分、平均分 |
| 最大值 + 字段 | `max(list, key=lambda x: x[N])` | 最高分、最低分 |
| 条件计数 | `len([x for x in list if 条件])` | 及格人数 |
| 逐行拆开 | `name, score = line.split(",")` | CSV 解析（[拆包](#14-元组)） |
| 字符串转整数 | `int("85")` → `85` | 读入数值数据 |

---

## 12. 字符串方法

### 字符串查找

| 方法 | 找到返回值 | 找不到返回值 |
|------|------------|--------------|
| `find(sub)` | 起始索引 | `-1` |
| `rfind(sub)` | 最后一次出现索引 | `-1` |
| `index(sub)` | 起始索引 | 抛出 `ValueError` |
| `rindex(sub)` | 最后一次出现索引 | 抛出 `ValueError` |
| `count(sub)` | 出现次数 | `0` |
| `in` 运算符 | `True` | `False` |

```python
s = "Hello, World!"

# find：安全查找，找不到返回 -1
print(s.find("World"))         # 7
print(s.find("Python"))        # -1
print(s.find("o", 5, 10))      # 8  （在索引 5~9 范围内查找）

# index：找不到抛异常
try:
    s.index("Python")
except ValueError:
    print("未找到子字符串")

# in：成员检查（最常用）
if "Hello" in s:
    print("包含 Hello")

# 忽略大小写查找
print(s.lower().find("world"))  # 7
```

### 字符串判断

| 方法 | 判断内容 | 空字符串 |
|------|----------|----------|
| `isalpha()` | 是否全是字母 | `False` |
| `isdigit()` | 是否全是数字 | `False` |
| `isalnum()` | 是否全是字母或数字 | `False` |
| `isspace()` | 是否全是空白字符 | `False` |
| `isupper()` | 是否全是大写 | `False` |
| `islower()` | 是否全是小写 | `False` |
| `istitle()` | 是否标题格式（首字母大写） | `False` |
| `startswith(prefix)` | 是否以 prefix 开头 | — |
| `endswith(suffix)` | 是否以 suffix 结尾 | — |

```python
"Hello".isalpha()          # True
"123".isdigit()            # True
"Hello123".isalnum()       # True
"   ".isspace()            # True
"HELLO".isupper()          # True
"hello".islower()          # True
"Hello.txt".endswith(".txt")  # True
```

### 字符串修改

> ⚠️ 字符串**不可变**！以下方法都**返回新字符串**，原字符串不变。如需修改原变量，必须重新赋值。

| 方法 | 作用 | 示例 |
|------|------|------|
| `replace(old, new)` | 替换子字符串 | `"abc".replace("a","x")` → `"xbc"` |
| `strip()` | 去除两端空白 | `" hi ".strip()` → `"hi"` |
| `lstrip()` / `rstrip()` | 去除左/右空白 | — |
| `split(sep)` | 按分隔符分割为列表 | `"a,b".split(",")` → `["a","b"]` |
| `join(iterable)` | 用字符串连接可迭代对象 | `",".join(["a","b"])` → `"a,b"` |
| `upper()` | 转大写 | `"hi".upper()` → `"HI"` |
| `lower()` | 转小写 | `"HI".lower()` → `"hi"` |
| `capitalize()` | 首字母大写，其余小写 | `"hELLO".capitalize()` → `"Hello"` |
| `title()` | 每个单词首字母大写 | `"hello world".title()` → `"Hello World"` |
| `swapcase()` | 大小写翻转 | `"AbC".swapcase()` → `"aBc"` |

```python
s = "  Hello, World!  "

print(s.strip())               # "Hello, World!"
print(s.replace(" ", ""))      # "Hello,World!" （去掉所有空格）
print(s.split(","))            # ['  Hello', ' World!  ']
print(",".join(["A", "B"]))    # "A,B"
print(s.upper())               # "  HELLO, WORLD!  "
print(s.lower())               # "  hello, world!  "

# 注意：原字符串未改变
print(s)                       # "  Hello, World!  "
```

> 💡 **字符串不可变**意味着每次修改都创建新对象。大量拼接时用 `"".join()` 比 `+` 高效得多。

### 练习常见错误

**❌ 模糊搜索用 `==` 而不是 `in`**

```python
# ❌ 精确匹配：只能找到完全相同的
keyword = "张"
if keyword == name:        # ← "张" == "张三" → False，找不到！
    ...

# ✅ 模糊匹配：子串包含即可
keyword = "张"
if keyword in name:        # ← "张" in "张三" → True，找到了！
    ...
```

> 💡 `in` 做子串匹配（模糊搜索），`==` 做完全相等判断。

---

## 13. 列表

### 列表

> 列表是**有序、可变**的集合，使用 `[]` 定义，元素可以是任意类型。

```python
fruits = ["apple", "banana", "cherry"]
```

### 增删改查速查表

| 操作 | 方法 | 说明 |
|------|------|------|
| **增** | `append(x)` | 末尾添加一个元素 |
| | `insert(i, x)` | 在索引 i 处插入 |
| | `extend(iterable)` | 末尾批量添加 |
| **删** | `remove(x)` | 删除第一个匹配值 |
| | `pop(i)` | 删除并返回索引 i 的元素（默认最后一个） |
| | `del list[i]` | 按索引删除 |
| | `clear()` | 清空所有元素 |
| **改** | `list[i] = x` | 按索引修改 |
| **查** | `list[i]` | 按索引访问 |
| | `index(x)` | 查找值首次出现索引 |
| | `count(x)` | 统计出现次数 |
| | `in` | 成员判断 |

```python
# 增
fruits = ["apple", "banana"]
fruits.append("cherry")            # ['apple', 'banana', 'cherry']
fruits.insert(1, "grape")          # ['apple', 'grape', 'banana', 'cherry']
fruits.extend(["kiwi", "melon"])   # ['apple', 'grape', 'banana', 'cherry', 'kiwi', 'melon']

# 删
fruits.remove("banana")            # 删除第一个 "banana"
popped = fruits.pop()              # 弹出最后一个元素
popped = fruits.pop(1)             # 弹出索引为 1 的元素
del fruits[0]                      # 删除第一个元素
fruits.clear()                     # 清空 → []

# 查
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits[0])            # apple
print(fruits[-1])           # banana（最后一个）
print(fruits.index("banana"))  # 1（首次出现）
print(fruits.count("banana"))  # 2
print("apple" in fruits)       # True
```

### 列表切片

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])     # [1, 2, 3]      索引1~3
print(nums[:3])      # [0, 1, 2]      开头到索引2
print(nums[3:])      # [3, 4, 5]      索引3到末尾
print(nums[::2])     # [0, 2, 4]      步长2
print(nums[::-1])    # [5, 4, 3, 2, 1, 0]  反转
```

### 排序

```python
nums = [3, 1, 4, 1, 5, 9]
nums.sort()                # 原地升序 → [1, 1, 3, 4, 5, 9]
nums.sort(reverse=True)    # 原地降序 → [9, 5, 4, 3, 1, 1]

# sorted() 返回新列表，原列表不变
sorted_nums = sorted(nums)
sorted_desc = sorted(nums, reverse=True)
```

### 列表推导式 ⭐

```python
# 基本语法：[表达式 for 变量 in 可迭代对象 if 条件]

# 1~10 偶数
even = [x for x in range(1, 11) if x % 2 == 0]  # [2, 4, 6, 8, 10]

# 平方数
squares = [x**2 for x in range(1, 6)]            # [1, 4, 9, 16, 25]

# 带条件转换
labels = ["Pass" if s >= 60 else "Fail" for s in [55, 78, 90]]
# → ['Fail', 'Pass', 'Pass']

# 嵌套循环
pairs = [(x, y) for x in range(2) for y in range(3)]
# → [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]
```

### 列表嵌套

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])        # [1, 2, 3]
print(matrix[1][2])     # 6

# 遍历二维列表
for row in matrix:
    for item in row:
        print(item, end=" ")
```

> ⚠️ **常见错误**：`fruits[3]` 索引超出范围 → `IndexError`

### 练习常见错误

**❌ 用 `list(生成器)` 代替列表推导式**

```python
# ❌ 写法别扭：生成器表达式套 list()
result = list(x for x in products if x[1] > 20)

# ✅ 标准列表推导式：括号直接变成方括号
result = [x for x in products if x[1] > 20]
```

> 💡 效果一样，但 `[...]` 是列表推导式的**原生语法**，更简洁直观。看到方括号一眼就知道在造列表。

---

## 14. 元组

> 元组是**有序、不可变**的集合，使用 `()` 定义。

```python
point = (3, 4)
mixed = (1, "hello", True, [1, 2, 3])   # 可包含不同类型
single = (5,)      # ⚠️ 单元素元组必须加逗号！
not_tuple = (5)    # 这是整数 5，不是元组！
```

### 基本操作

```python
# 访问
print(point[0])      # 3
print(point[-1])     # 4

# 切片（返回新元组）
print(point[0:2])    # (3, 4)

# 连接与重复
t1, t2 = (1, 2), (3, 4)
print(t1 + t2)       # (1, 2, 3, 4)
print(t1 * 3)        # (1, 2, 1, 2, 1, 2)

# 成员检查
print(2 in t1)       # True
```

### 解包 (Unpacking)

> 拆包就是**去掉容器，直接获取里面的值**。元组、列表、函数返回值都能拆。

```python
# 方式一：一一对应（变量数和元素数必须相等）
x, y = (3, 4)               # x=3, y=4
a, b, c, d = (1, 2, 3, 4)   # ❌ 变量和元组个数不一致 → ValueError

# 方式二：带 * 的变量收走剩余全部
a, *b = (1, 2, 3, 4)        # a=1, b=[2, 3, 4]
*a, b = (1, 2, 3, 4)        # a=[1, 2, 3], b=4

# 方式三：函数调用时用 * 展开元组/列表
def func(a, b, *args):       # *args 收走多余的位置参数
    print(a, b)
    print(args)

func(1, 2, 3, 4, 5)
# 1 2
# (3, 4, 5)

arg = (1, 2, 3, 4, 5)
func(*arg)                   # * 展开元组，等价于 func(1, 2, 3, 4, 5)
```

> 💡 **两种 * 的区别**：定义时 `def f(*args)` 是**打包**——多余参数收进元组；调用时 `f(*tup)` 是**拆包**——把元组展开成独立参数。

**拆包的常见应用场景：**

```python
# 1. 函数返回多个值 → 拆包接收
def get_min_max(nums):
    return min(nums), max(nums)
mn, mx = get_min_max([3, 1, 4, 1, 5])   # mn=1, mx=5

# 2. max/min 返回元组 → 拆包取字段
top_name, top_score = max(scores, key=lambda x: x[1])

# 3. split(",") 返回列表 → 拆包取值
name, score = "张三,85".split(",")       # name="张三", score="85"

# 4. 遍历字典 → 键值拆包
for key, value in {"a": 1, "b": 2}.items():
    print(key, value)
```

| 场景 | 写法 | 拆前 | 拆后 |
|------|------|------|------|
| 元组 | `a, b = tup` | `(1, 2)` | `a=1, b=2` |
| 星号收尾 | `a, *b = tup` | `(1, 2, 3, 4)` | `a=1, b=[2,3,4]` |
| 展开调用 | `func(*tup)` | `(1, 2, 3)` | `func(1, 2, 3)` |
| 函数返回 | `a, b = func()` | `return 1, 2` | `a=1, b=2` |
| split | `a, b = s.split(",")` | `["张三","85"]` | `a="张三", b="85"` |
| 遍历字典 | `for k, v in d.items()` | `("a",1)` | `k="a", v=1` |

### 元组 vs 列表

| | 列表 (list) | 元组 (tuple) |
|---|---|---|
| **可变性** | 可变 | **不可变** |
| **语法** | `[1, 2, 3]` | `(1, 2, 3)` |
| **性能** | 较慢 | **更快**（内存优化） |
| **作为字典键** | ❌ 不允许 | ✅ 允许 |
| **适用场景** | 需频繁增删改的数据 | 固定不变的数据（坐标、配置） |
| **安全性** | 可被意外修改 | 数据保护，防止误改 |

### 元组典型应用

```python
# 1. 作为字典的键
locations = {(1, 2): "点A", (3, 4): "点B"}

# 2. 函数返回多个值（本质是返回元组）
def get_min_max(nums):
    return min(nums), max(nums)

mn, mx = get_min_max([3, 1, 4, 1, 5])   # 解包

# 3. 格式化输出后面的 () 本质是元组
print("Name: %s, Age: %d" % ("Alice", 30))

# 4. 数据不可被修改，保护数据安全
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
```

---

## 15. 字典

> 字典是**键值对**的集合，使用 `{}` 定义。Python 3.7+ 保持插入顺序。

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

### 增删改查

```python
# 查
print(person["name"])          # Alice（键不存在 → KeyError）
print(person.get("name"))     # Alice
print(person.get("email"))    # None（键不存在返回 None，安全！）
print(person.get("email", "N/A"))  # N/A（设置默认值）

# 改 / 增
person["city"] = "LA"         # 修改已有键
person["email"] = "a@x.com"   # 添加新键（键不存在则新增）

# 删
del person["age"]             # 删除键值对
email = person.pop("email")   # 删除并返回值
person.pop("xxx", None)       # 键不存在返回默认值，不抛异常
last = person.popitem()       # 弹出最后一个键值对 (Python 3.7+)
person.clear()                # 清空
```

### 遍历

```python
person = {"name": "Alice", "age": 30}

# 遍历键
for key in person:
    print(key)

for key in person.keys():
    print(key)

# 遍历值
for value in person.values():
    print(value)

# 遍历键值对（最常用）
for key, value in person.items():
    print(f"{key}: {value}")
```

### 常用方法速查

| 方法 | 说明 |
|------|------|
| `dict[key]` | 访问值（键不存在抛 KeyError） |
| `dict.get(key, default)` | 安全访问（键不存在返回 default） |
| `dict[key] = value` | 添加/修改 |
| `dict.update({k:v})` | 批量更新 |
| `dict.keys()` | 返回所有键 |
| `dict.values()` | 返回所有值 |
| `dict.items()` | 返回所有 (键, 值) 对 |
| `dict.pop(key, default)` | 删除键并返回值 |
| `in` | 检查键是否存在 |
| `len(dict)` | 键值对数量、长度 |
| `dict = {}` | 定义空字典 |

### 字典推导式

```python
# {键表达式: 值表达式 for 变量 in 可迭代对象 if 条件}
squares = {x: x**2 for x in range(1, 6)}
# → {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 反转键值对
original = {"a": 1, "b": 2}
reversed_dict = {v: k for k, v in original.items()}
# → {1: 'a', 2: 'b'}
```

> ⚠️ **关键限制**：字典的键必须是**不可变类型**（字符串、数字、元组等），不能用列表或字典作为键。

### 练习常见错误

**❌ "先占位再回滚" vs "先验证再提交"**

```python
# ❌ 先加进去，校验失败再删掉（多一步回滚，有风险）
contacts[name] = ''          # 先占位
if 校验手机号失败:
    del contacts[name]       # 再回滚 → 万一回滚前崩溃，脏数据留在字典里

# ✅ 先验证，都通过了再加（更安全）
name = input("姓名: ").strip()
if name in contacts:
    print("姓名已存在")
    return                   # 压根没加，不需要清理

phone = input("手机号: ").strip()
if not (phone.isdigit() and len(phone) == 11):
    print("手机号错误")
    return                   # 也没加，干净退出

contacts[name] = phone       # 一切 OK 才写入
```

> 💡 **原则**：先校验所有输入，全部通过后再写入。这个习惯在数据库、文件操作中更为重要——写一半再回滚代价很大。

**❌ 用 `dict(生成器)` 代替字典推导式**

```python
products = [("苹果", 8.5), ("西瓜", 23.0)]

# ⚠️ 能跑，dict() 吃了 (键, 值) 对
result = dict(x for x in products)
# → {'苹果': 8.5, '西瓜': 23.0}

# ✅ 标准字典推导式：显式控制键值关系
result = {name: price for name, price in products}
# → {'苹果': 8.5, '西瓜': 23.0}
```

> 💡 `dict()` 能接受 `(key, value)` 对是侥幸，但字典推导式能**显式指定**哪个做键哪个做值，更易读，也更灵活（比如键值互换 `{v: k for ...}`）。

---

## 16. 集合

> 集合是**无序、不重复**元素的集合，使用 `{}` 或 `set()` 定义。

```python
# 定义
fruits = {"apple", "banana", "cherry"}
empty = set()              # 定义空集合⚠️ {} 是空字典，不是空集合！
nums = set([1, 2, 2, 3])  # → {1, 2, 3} 自动去重
```

### 基本操作

```python
s = {1, 2, 3}

# 增删
s.add(4)          # {1, 2, 3, 4}
s.remove(2)       # {1, 3, 4}（元素不存在 → KeyError）
s.discard(5)      # 删除（元素不存在不报错）
s.pop()           # 随机删除一个
s.clear()         # 清空

# 成员检查（O(1) 时间复杂度，比列表的 O(n) 快得多）
print(3 in s)     # True
```

### 集合运算（交并差）

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # 并集：{1, 2, 3, 4, 5, 6}
print(a & b)   # 交集：{3, 4}
print(a - b)   # 差集：{1, 2}  （a 有但 b 没有）
print(a ^ b)   # 对称差：{1, 2, 5, 6}  （不同时属于两个集合的）
```

### 集合推导式

```python
squares = {x**2 for x in range(1, 6)}
# → {1, 4, 9, 16, 25}

# 去重
nums = [1, 2, 2, 3, 3, 3]
unique = {x for x in nums}   # {1, 2, 3}
```

### 典型应用

```python
# 1. 去重
unique = list(set([1, 2, 2, 3, 3]))   # [1, 2, 3]

# 2. 成员检查（比列表快得多）
if "target" in large_set:   # O(1) vs 列表 O(n)
    pass

# 3. 找共同元素
common = set(list1) & set(list2)
```

---

## 17. 函数基础

> 函数是组织好的、可重复使用的代码块，用 `def` 关键字定义。

### 定义与调用

```python
def greet(name):
    """向用户打招呼（这是文档字符串 docstring）"""
    return f"Hello, {name}!"

# 调用
result = greet("Alice")
print(result)   # Hello, Alice!
```

### 参数类型

```python
# 1. 位置参数
def add(a, b):
    return a + b

# 2. 默认参数（必须放在非默认参数后面）
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Hello, Alice!
print(greet("Bob", "Hi"))          # Hi, Bob!

# 3. 关键字参数
print(greet(greeting="Hey", name="Charlie"))  # Hey, Charlie!

# 4. 可变参数 *args（元组）和 **kwargs（字典）
def func(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

func(1, 2, 3, name="Alice", age=30)
# args: (1, 2, 3)
# kwargs: {'name': 'Alice', 'age': 30}
```

> ⚠️ **参数顺序**：`位置参数, *args, 关键字参数, **kwargs`

### 返回值

```python
# 单个返回值
def square(x):
    return x ** 2

# 多个返回值（本质是返回元组）
def min_max(nums):
    return min(nums), max(nums)

mn, mx = min_max([3, 1, 4, 1, 5])  # mn=1, mx=5
```

### 变量作用域

| 作用域 | 说明 |
|--------|------|
| **局部变量** | 在函数内定义，只在函数内可见 |
| **全局变量** | 在模块级别定义，全模块可见 |
| `global` | 在函数内声明使用全局变量 |
| `nonlocal` | 在嵌套函数中声明使用外层函数的变量 |

```python
x = 10   # 全局变量

def modify():
    global x     # 声明要修改全局变量
    x = 20

modify()
print(x)         # 20
```

**nonlocal — 修改外层函数的局部变量：**

```python
def outer():
    count = 0           # 外层函数的局部变量

    def inner():
        nonlocal count  # 声明 count 是外层变量（非全局）
        count += 1
        return count

    return inner        # 返回 inner 函数本身（不是调用结果）

f = outer()             # f 现在就是 inner 函数
print(f())   # 调用 inner() → 1
print(f())   # 调用 inner() → 2（count 被 inner 记住了）
```

> ⚠️ **注意**：`nonlocal` 只能在嵌套函数中使用，声明的变量必须是外层函数的局部变量，不能是全局变量。

### 函数嵌套

> 在一个函数内部定义另一个函数，称为函数嵌套（或内部函数）。

```python
def outer():
    print("外层函数")

    def inner():
        print("内层函数")

    inner()            # 在正确的位置调用内层函数

outer()
# 输出：
# 外层函数
# 内层函数
```

> ⚠️ **常见错误**：不要把内层函数的调用写在定义之前，否则永远执行不到。

```python
# ❌ 调用在定义之前 → 永远执行不到
def outer():
    inner()            # 此时 inner 还未定义！
    def inner():
        print("内层函数")

# ❌ 在内层函数中调用外层函数 → 死循环
def outer():
    def inner():
        outer()        # 无限递归，直到超过递归最大深度
```

> 💡 **使用场景**：封装辅助逻辑、实现闭包、作为装饰器的基础。

### 闭包

> 闭包 = 外部函数（盒子）+ 内部函数（按钮）。外部函数把变量保护起来，内部函数是操作变量的唯一入口。

**为什么需要闭包？** 普通函数每次调用，局部变量都重新初始化。如果想"记住"上一次的值，用全局变量又怕被意外修改。闭包把变量藏起来，安全又可累加。

```python
# ❌ 普通函数：每次调用 count 都归零
def counter():
    count = 0
    count += 1
    return count
print(counter())   # 1
print(counter())   # 1   ← 永远是 1

# ❌ 全局变量：count 暴露在外，谁都能改
count = 0
def counter():
    global count
    count += 1
    return count
# count = 999  ← 随时可能被意外修改！

# ✅ 闭包：count 藏起来，只能通过 inner 操作
def make_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c1 = make_counter()   # 一个独立的计数器，count=0
c2 = make_counter()   # 另一个独立的计数器，count=0
print(c1())   # 1
print(c1())   # 2
print(c2())   # 1   ← c1 和 c2 互不影响
```

| 方式 | 状态保留 | 数据安全 | 独立性 |
|------|---------|---------|--------|
| 普通函数局部变量 | ❌ 每次归零 | ✅ | — |
| 全局变量 | ✅ | ❌ 谁都能改 | — |
| **闭包** | ✅ | ✅ | ✅ 每次 `make_counter()` 创建独立副本 |

> 💡 **一句话**：闭包就是"有记忆的函数"。它记住了创建时那一层变量的状态。

### 匿名函数 lambda

> lambda 是一种简短的函数定义方式，适用于**简单、一次性**的逻辑。

```python
# 语法：lambda 形参 : 返回值（表达式）
add = lambda a, b: a + b
print(add(3, 5))   # 8
```

> ⚠️ `lambda` 不需要 `return`，表达式本身的结果就是返回值。

```python
# 无参数
greet = lambda: "Hello!"
print(greet())          # Hello!

# 一个参数
square = lambda x: x ** 2
print(square(5))        # 25

# 默认参数（必须放在非默认参数后面）
info = lambda name, age=18: (name, age)
print(info("Alice"))       # ('Alice', 18)
print(info("Bob", 25))     # ('Bob', 25)

# 关键字参数（**kwargs）
print_info = lambda **kwargs: kwargs
print(print_info(name="Alice", age=30))
# → {'name': 'Alice', 'age': 30}

# lambda 结合 if-else
compare = lambda a, b: "a小" if a < b else "a大于等于b"
print(compare(8, 5))   # a大于等于b
print(compare(3, 9))   # a小
```

> ⚠️ lambda 只能写**一行表达式**。`if-else` 可以，但 `if-elif-else` 多分支会非常长，此时应该用 `def`。

### lambda vs def

| | `def` 函数 | `lambda` 匿名函数 |
|---|---|---|
| **定义方式** | `def name():` | `name = lambda:` |
| **代码行数** | 多行语句 | 只能一行表达式 |
| **可读性** | 高（适合复杂逻辑） | 低（适合简单逻辑） |
| **return** | 显式写 `return` | 自动返回表达式结果 |
| **适用场景** | 复杂业务逻辑、可复用模块 | 简单计算、`sorted`/`filter` 的 key 参数 |

```python
# 典型用法：作为 sorted 的排序键
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda x: x[1])   # 按分数排序
# → [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

**sorted + lambda 的核心原理**：`key` 告诉 `sorted` 按什么排序。排序时，`lambda` 的参数 `x` 依次代表列表中每个元素，lambda 返回什么，sorted 就按什么排。

```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# 按成绩从高到低（x[0]=姓名, x[1]=成绩）
sorted(students, key=lambda x: x[1], reverse=True)
# → [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# 按姓名长度排序（len(x[0]) = 姓名字符数）
sorted(students, key=lambda x: len(x[0]))
# → [('Bob', 92), ('Alice', 85), ('Charlie', 78)]   # Bob=3, Alice=5, Charlie=7

# 按成绩的个位数排序
sorted(students, key=lambda x: x[1] % 10)
# → [('Bob', 92), ('Alice', 85), ('Charlie', 78)]   # 2 < 5 < 8
```

| 需求 | `key=lambda x: ...` | 原理 |
|------|---------------------|------|
| 按元组第 N 项排序 | `x[N]` | 取值直接比较 |
| 按字符串长度排序 | `len(x[0])` | 返回长度比较 |
| 按计算结果排序 | `表达式` | 返回计算结果比较 |
| 降序 | 加 `reverse=True` | 从大到小 |

**x 为什么代指元组？——sorted 内部原理**

`x` 不是我们定义的变量，而是 **sorted 硬塞给 key 函数的参数**。列表中装什么，`x` 就是什么：

```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

sorted(students, key=lambda x: len(x[0]))
```

sorted 内部等价于做这些事：

```python
# sorted 依次取列表中的每个元素，塞给 key 函数
x = ("Alice", 85)    # 第 1 个元素 → len(x[0]) = len("Alice")  = 5
x = ("Bob", 92)      # 第 2 个元素 → len(x[0]) = len("Bob")    = 3
x = ("Charlie", 78)  # 第 3 个元素 → len(x[0]) = len("Charlie") = 7

# 然后按返回值排序：3 → 5 → 7，短的在前
```

**`x` 叫什么无所谓**，叫 `stu`、`item` 效果一样：

```python
sorted(students, key=lambda stu: len(stu[0]))   # 照样跑
sorted(students, key=lambda a: len(a[0]))        # 照样跑
```

> 💡 **一句话**：列表里装什么类型，`lambda x` 的 `x` 就是什么类型。装元组 `x` 就是元组，装字符串 `x` 就是字符串。是 **sorted 把它推进来的**，不是我们定义的。

### zip — 并行打包

> `zip()` 将多个可迭代对象"拉链式"配对，返回元组的迭代器。

```python
names = [1, 2, 3]
chars = ['a', 'b', 'c']

# 迭代取出
for pair in zip(names, chars):
    print(pair)
# (1, 'a')
# (2, 'b')
# (3, 'c')

# 转列表查看
print(list(zip(names, chars)))
# → [(1, 'a'), (2, 'b'), (3, 'c')]
```

> ⚠️ 如果各列表长度不一致，按**最短的**那个截断。

### reduce — 累积计算

> `reduce()` 从前两个元素开始，逐步累积到后面所有元素。需要 `from functools import reduce`。

```python
from functools import reduce

# 累加：1+2=3 → 3+3=6 → 6+4=10
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))   # 10

# 累乘：1×2=2 → 2×3=6 → 6×4=24
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))   # 24
```

**执行过程：**
```
第 1 步：取 1, 2 → 1+2=3
第 2 步：取 3, 3 → 3+3=6
第 3 步：取 6, 4 → 6+4=10
```

> ⚠️ `reduce(func, seq)` 中的函数**必须接收两个参数**——第一个是累积值，第二个是下一个元素。

### min / max 的 key 参数

> 和 `sorted` 一样，`min` / `max` 也可以用 `key=` 指定比较依据。

```python
# 直接比较 → 最大是 5
max(5, -8, 3)   # 5

# 按绝对值比较 → 绝对值最大的是 -8
max(5, -8, 3, key=abs)   # -8
```

### 内置函数补充

| 函数 | 作用 | 示例 |
|------|------|------|
| `abs(x)` | 返回绝对值 | `abs(-5)` → `5` |
| `sum(iterable)` | 求和（内部放可迭代对象） | `sum([1, 2, 3])` → `6` |
| `min(x, key=...)` | 最小值，可按 key 转换后比较 | `min(5, -8, key=abs)` → `5` |
| `max(x, key=...)` | 最大值，同上 | `max(5, -8, key=abs)` → `-8` |
| `zip(a, b)` | 并行打包成元组 | `zip([1,2],['a','b'])` |
| `dir(module)` | 查看模块所有属性 | `dir(__builtins__)` |

### 练习常见错误

**❌ 错误 1：lambda 不写参数，用固定索引取元素**

```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# ❌ 没写参数 x，直接拿 students[0][2] → 永远取第一个元素且索引用错
sorted(students, key=lambda: students[0][2])

# ✅ x 是占位符，依次代表每个元组，x[1] 就是每个学生的成绩
sorted(students, key=lambda x: x[1])
```

> 💡 `lambda x` 的 `x` 不是固定变量名，排序时它**轮流等于列表中每个元素**。不写参数 = 没东西可换 = 永远取固定索引。

**❌ 错误 2：按姓名长度和按姓名混淆**

```python
# ❌ 按姓名首字母排（"Alice" vs "Bob" vs "Charlie"）
sorted(students, key=lambda x: x[0])

# ✅ 按姓名长度排（5 vs 3 vs 7）
sorted(students, key=lambda x: len(x[0]))
```

> 💡 要长度就 `len()`，不要漏掉。`x[0]` 返回字符串本身，`len(x[0])` 返回字符串长度。

**❌ 错误 3：不敢用字典做 `+=` 统计**

```python
result = {}
for s in scores:
    grade = to_grade(s)        # 算出等级
    if grade in result:
        result[grade] += 1     # 已有 → 次数 +1
    else:
        result[grade] = 1      # 第一次 → 初始化为 1
```

> 💡 `result[grade] += 1` 就是 `result[grade] = result[grade] + 1`，和 `x += 3` 一回事。先取出当前值 → +1 → 存回去。字典的修改和变量赋值本质完全相同。

**❌ 错误 4：map 忘了返回所需结构**

```python
products = [("苹果", 8.5), ("西瓜", 23.0)]

# ❌ 只返回价格 → 丢了名称和原价
map(lambda x: x[1] * 0.8, products)
# → [6.8, 18.4]  名称呢？原价呢？

# ✅ 返回完整三元组
map(lambda x: (x[0], x[1], round(x[1] * 0.8, 1)), products)
# → [('苹果', 8.5, 6.8), ('西瓜', 23.0, 18.4)]
```

> 💡 `map` 返回什么就得到什么。想保留原始字段，就在 lambda 里把它们包进元组一起返回。

**❌ 错误 5：忘记 filter/map 返回的是迭代器，要用 list() 看结果**

```python
# ❌ 直接打印看不到内容
print(filter(lambda x: x[1] > 20, products))
# → <filter object at 0x...>

# ✅ list() 转列表
print(list(filter(lambda x: x[1] > 20, products)))
# → [('西瓜', 23.0), ('草莓', 35.0)]
```

> 💡 `filter()` 和 `map()` 返回的是**迭代器**（懒加载），不会自动展开。`list()` 强制它计算并转成可见的列表。

## 18. 类型转换

> 类型转换是将一种数据类型转换为另一种数据类型，使用内置的类型转换函数实现。

### 常用类型转换函数一览

| 函数 | 作用 | 可转换的输入 | 失败时抛出 |
|------|------|-------------|------------|
| `int(x)` | 转整数 | 数字字符串、浮点数 | `ValueError` |
| `float(x)` | 转浮点数 | 整数、数字字符串 | `ValueError` |
| `str(x)` | 转字符串 | 任意对象 | — |
| `bool(x)` | 转布尔值 | 任意对象 | — |
| `list(x)` | 转列表 | 字符串、可迭代对象 | `TypeError` |
| `tuple(x)` | 转元组 | 字符串、可迭代对象 | `TypeError` |
| `set(x)` | 转集合 | 可迭代对象 | `TypeError` |
| `dict(x)` | 转字典 | 键值对序列 | `ValueError` |
| `eval(x)` | 字符串求值 | 合法 Python 表达式 | `SyntaxError` |

### `int(x)` — 转整数

```python
# 字符串转整数（仅限数字字符串）
print(int("123"))     # 123
print(int("-456"))    # -456
print(int("+789"))    # 789

# ❌ 错误示例
# int("12.34")        # ValueError: 非数字字符串（含小数点）
# int("abc")          # ValueError: 非数字字符串
# int("123abc")       # ValueError: 含非数字字符
# int("123-")         # ValueError: 符号不能写在后面

# 浮点数转整数（直接截断，非四舍五入）
print(int(3.14))      # 3
print(int(-3.9))      # -3（注意：不是 -4，是直接截断！）
print(int(9.99))      # 9
```

> ⚠️ **注意**：`int()` 对浮点数是**直接截断**小数部分，不是四舍五入。如需四舍五入，用 `round()`。

### `float(x)` — 转浮点数

```python
# 整数转浮点数
print(float(10))       # 10.0
print(float(-5))       # -5.0

# 字符串转浮点数
print(float("3.14"))   # 3.14
print(float("-0.5"))   # -0.5
print(float("1e-3"))   # 0.001  （支持科学计数法）

# ❌ 错误示例
# float("abc")         # ValueError
# float("12.34.56")    # ValueError: 多个小数点
# float("$100")        # ValueError: 含货币符号
```

### `str(x)` — 转字符串

```python
# 任意类型都可转字符串
print(str(123))            # "123"
print(str(3.14))           # "3.14"
print(str(True))           # "True"
print(str([1, 2, 3]))      # "[1, 2, 3]"
print(str(None))           # "None"

# str() 与 repr() 的区别
import datetime
d = datetime.date(2024, 6, 6)
print(str(d))              # "2024-06-06"  （可读）
print(repr(d))             # "datetime.date(2024, 6, 6)"  （给开发者看的）
```

> ⚠️ **注意**：`float` 转 `str` 会去除末尾的 `.0`。如 `str(10.0)` → `"10.0"`（保留 `.0`），但某些情况会自动简化。如需精确控制小数位，使用 f-string 格式化。

### `list(x)` / `tuple(x)` — 转列表/元组

```python
# 字符串 → 每个字符为一个元素
print(list("abc"))         # ['a', 'b', 'c']
print(tuple("abc"))        # ('a', 'b', 'c')

# 可迭代对象互相转换
print(list((1, 2, 3)))     # [1, 2, 3]   元组 → 列表
print(tuple([1, 2, 3]))    # (1, 2, 3)   列表 → 元组
print(list({"a": 1, "b": 2}))   # ['a', 'b']   字典 → 键的列表
print(list({"a": 1, "b": 2}.values()))  # [1, 2]

# ❌ 非可迭代对象会报错
# list(123)               # TypeError: 'int' object is not iterable
```

### `eval(x)` — 字符串求值

> `eval()` 将字符串当作 Python 表达式执行并返回结果。

```python
# 计算数学表达式
print(eval("1 + 2 * 3"))       # 7
print(eval("3 ** 4"))          # 81

# 还原数据结构（最常用）
print(eval("[1, 2, 3]"))       # [1, 2, 3]   列表
print(eval("{'a': 1, 'b': 2}")) # {'a': 1, 'b': 2}   字典
print(eval("(1, 2, 3)"))       # (1, 2, 3)   元组
print(eval("{1, 2, 3}"))       # {1, 2, 3}   集合
```

> ⚠️ **安全警告**：`eval()` 可执行**任意代码**，包括删除文件等危险操作！当输入来自不可信来源时，可能导致代码注入攻击。

```python
# ❌ 危险示例！千万不要对用户输入使用 eval()
# user_input = "__import__('os').system('rm -rf /')"
# eval(user_input)   # 会执行系统命令！

# ✅ 安全替代：使用 ast.literal_eval()
import ast
safe_result = ast.literal_eval("[1, 2, 3]")     # [1, 2, 3]
safe_result = ast.literal_eval("{'a': 1}")       # {'a': 1}
# ast.literal_eval("__import__('os')")           # ❌ ValueError，拒绝危险代码
```

> 💡 **原则**：只在信任的数据源上使用 `eval()`；对用户输入或外部数据**始终**使用 `ast.literal_eval()`。

---

## 19. 深浅拷贝与可变/不可变类型

### 可变类型 (Mutable) vs 不可变类型 (Immutable)

> 理解可变/不可变是理解深浅拷贝的前提。

| | 可变类型 | 不可变类型 |
|---|---|---|
| **特征** | 值可被修改，内存地址不变 | 值不可修改，修改即创建新对象 |
| **常见类型** | `list`, `dict`, `set`, `bytearray` | `int`, `float`, `str`, `tuple`, `bool`, `frozenset` |
| **修改行为** | 原地修改 | 创建新对象并改变引用 |
| **id() 变化** | 不变 | 改变 |

```python
# 可变类型：原地修改，id 不变
a = [1, 2, 3]
addr_before = id(a)
a.append(4)                   # 修改列表内容
addr_after = id(a)
print(addr_before == addr_after)  # True，同一个对象！

# 不可变类型：修改 = 创建新对象，id 改变
x = 10
addr_before = id(x)
x += 5                        # 看似"修改"，实际创建了新 int 对象
addr_after = id(x)
print(addr_before == addr_after)  # False，不同对象！
```

> 💡 **为什么要区分？** 因为深浅拷贝只对**可变类型**有意义。不可变类型不存在被意外修改的问题，赋值时直接共享同一对象即可。

### 三种"复制"方式对比

| | 赋值 `=` | 浅拷贝 | 深拷贝 |
|---|---|---|---|
| **外层对象** | 共享（同一个） | **新建（独立）** | **新建（独立）** |
| **内层嵌套对象** | 共享 | **共享** | **新建（独立）** |
| **数据独立性** | 完全不独立 | **半独立**（只有第一层） | **完全独立** |
| **方法** | `b = a` | `copy.copy(a)` / `a.copy()` / `a[:]` | `copy.deepcopy(a)` |
| **性能** | 最快 | 中等 | 最慢（递归复制所有层） |

### 赋值 `=` — 完全共享

```python
a = [[1, 2], [3, 4]]
b = a           # 赋值：a 和 b 指向完全相同的对象

a[0][0] = 'X'
print(b)        # [['X', 2], [3, 4]]  ← 受影响！
print(a is b)   # True（同一个对象）
```

### 赋值 `=` 易混点：局部修改 vs 整体赋值

赋值后 `a` 和 `b` 指向同一对象。但 **`a[0]` 改的是对象内部，`a = ...` 改的是变量指向**：

```python
a = [1, 2, 3]
b = a           # a 和 b 都指向 [1, 2, 3]
                #   a ──→ [1, 2, 3] ←── b

# === 局部修改：改对象内部 → b 跟着变（同一个对象）===
a[0] = 'X'      #   a ──→ ['X', 2, 3] ←── b
print(b)        # ['X', 2, 3]          ← b 变了！

a.append(4)     #   a ──→ ['X', 2, 3, 4] ←── b
print(b)        # ['X', 2, 3, 4]       ← b 也变了！

# === 整体赋值：改变 a 指向谁 → b 不变（各指各的）===
a = [100, 200]  #   a ──→ [100, 200]    b ──→ ['X', 2, 3, 4]
print(b)        # ['X', 2, 3, 4]       ← b 没变！
print(a is b)   # False（不同对象了）
```

> 💡 **核心**：看等号左边是 **`a[索引]`** 还是 **`a`**。前者改对象内部（b 可见），后者改变量指向（b 不可见）。

### 浅拷贝 (Shallow Copy) — 半共享

> 创建新对象，拷贝第一层数据，**嵌套层仍指向原地址**。就像只换了外壳，里面的东西还是原来的。

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)   # 浅拷贝

# 修改内层 → 浅拷贝受影响（内层共享同一对象）
original[0][0] = 'X'
print(shallow)   # [['X', 2], [3, 4]]  ← 受影响！

# 修改外层 → 浅拷贝不受影响（外层独立）
original[0] = ['Y', 2]          # 替换整个第一层元素
print(shallow)   # [['X', 2], [3, 4]]  ← 不受影响！
```

> 📐 **图解**：浅拷贝后，外层列表地址不同，但 `[1, 2]` 和 `[3, 4]` 这两个内层列表仍指向原来地址。改内层 = 动原地址 = 两边都受影响。

**浅拷贝的三种写法：**

```python
# 方法 1：copy 模块
import copy
b = copy.copy(a)

# 方法 2：对象自身的 copy() 方法（列表和字典有）
b = a.copy()

# 方法 3：全切片（仅列表）
b = a[:]
```

> 💡 **适用场景**：对象只有一层（简单列表）时，浅拷贝就足够了，效率更高。

### 深拷贝 (Deep Copy) — 完全独立

> 递归复制对象的所有层级，内外全部创建新内存地址。**修改原对象对深拷贝副本零影响**。

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)         # 浅拷贝
deep = copy.deepcopy(original)        # 深拷贝

original[0][0] = 'X'
print(shallow)   # [['X', 2], [3, 4]]  ← 浅拷贝受影响
print(deep)      # [[1, 2], [3, 4]]    ← 深拷贝完全不受影响
```

> 💡 **适用场景**：嵌套结构（列表套列表、字典套列表等）且需要完全独立副本时用深拷贝。

### 总结：选哪种方式？

```python
# 📋 决策速查
# 不可变类型（int、str、tuple）→ 直接赋值即可，不需要拷贝
# 一层列表/字典             → 浅拷贝（.copy() 或 [:]）
# 嵌套结构 + 需完全独立     → 深拷贝（copy.deepcopy()）
# 嵌套结构 + 不需要完全独立  → 浅拷贝（效率高）

# ✅ 典型场景
a = [1, 2, 3]
b = a.copy()            # 浅拷贝就够了（一层列表）

matrix = [[1, 2], [3, 4]]
backup = copy.deepcopy(matrix)   # 嵌套 → 深拷贝
```

> ⚠️ **核心规则**：深浅拷贝只针对**可变类型**。对于不可变类型（int、str、tuple），赋值时直接共享同一对象即可，Python 不会为其创建多余副本。

---

> 📌 **学习建议**：多动手敲代码，遇到错误先看最后一行报错信息。善用 `print()` 和 `type()` 调试，不懂就查官方文档或 `help()` 函数。

*最后更新：2026-06-13*

---

## 20. 速查表与常见面试题

### 数据类型速查

| 类型 | 可变 | 有序 | 语法 | 去重 | 适用 |
|------|------|------|------|------|------|
| `str` | ❌ | ✅ | `"text"` | — | 文本 |
| `list` | ✅ | ✅ | `[1, 2]` | ❌ | 可变序列 |
| `tuple` | ❌ | ✅ | `(1, 2)` | ❌ | 不可变序列/字典键 |
| `dict` | ✅ | ✅(3.7+) | `{"k":"v"}` | 键唯一 | 键值映射 |
| `set` | ✅ | ❌ | `{1, 2}` | ✅ | 去重/成员检查 |

### 常用内置函数速查

| 函数 | 作用 |
|------|------|
| `len(x)` | 获取长度 |
| `type(x)` | 获取类型 |
| `int(x)`, `float(x)`, `str(x)` | 类型转换 |
| `list(x)`, `tuple(x)`, `set(x)` | 转为对应容器 |
| `range(...)` | 生成整数序列 |
| `enumerate(x)` | 带索引遍历 |
| `zip(a, b)` | 并行迭代 |
| `sorted(x, key=..., reverse=...)` | 按 key 返回值排序，reverse=True 降序 |
| `max(x,key=...)`, `min(x,key=...)`, `sum(x)` | 最大/最小（支持 key 参数）/ 求和 |
| `abs(x)` | 绝对值 |
| `round(x, n)` | 四舍五入到 n 位 |
| `isinstance(x, type)` | 类型检查 |

### 常见面试题

**1. 列表 vs 元组？**
> 列表可变，元组不可变。元组性能更好，可作为字典键。需要修改数据用列表，固定数据用元组。

**2. `is` vs `==`？**
> `==` 比较**值**是否相等，`is` 比较**是否为同一个对象**（内存地址）。

```python
a = [1, 2]
b = [1, 2]
print(a == b)   # True  （值相同）
print(a is b)   # False （不同对象）

a = b = [1, 2]
print(a is b)   # True  （同一对象）
```

**3. 深拷贝 vs 浅拷贝？**
> 详见 [第 19 节](#19-深浅拷贝与可变不可变类型)。简单来说：浅拷贝只复制第一层（内层仍共享），深拷贝递归复制所有层（完全独立）。赋值 `=` 则不复制，直接共享同一对象。

**4. `*args` 和 `**kwargs` 的区别？**
> `*args` 接收位置参数为**元组**；`**kwargs` 接收关键字参数为**字典**。

**5. Python 是值传递还是引用传递？**
> Python 的传递方式是"传对象引用"。不可变对象（整数、字符串、元组）表现为值传递；可变对象（列表、字典）表现为引用传递。

**6. 如何反转一个字符串/列表？**
```python
s = "hello"
print(s[::-1])              # "olleh"

lst = [1, 2, 3]
print(lst[::-1])            # [3, 2, 1]
print(list(reversed(lst)))  # [3, 2, 1]
```

**7. 闭包是什么？有什么作用？**
> 闭包 = 外部函数（盒子）+ 内部函数（按钮）。外部函数保护变量，内部函数是操作变量的唯一入口。作用是**让函数"记住"状态**，避免用全局变量。

```python
def make_counter():         # 盒子
    count = 0
    def inner():            # 按钮
        nonlocal count
        count += 1
        return count
    return inner

c = make_counter()
print(c())   # 1
print(c())   # 2  ← count 被记住了
```

**8. lambda 和 def 的区别？**
| | `def` | `lambda` |
|---|---|---|
| **语法** | `def name():` 多行 | `name = lambda: 表达式` 一行 |
| **return** | 必须写 | 自动返回表达式结果 |
| **可读性** | 高 | 低（仅适合简单逻辑） |
| **场景** | 复杂业务、复用 | `sorted`/`filter` 的 `key` 参数 |

**9. global 和 nonlocal 的区别？**
> `global` 声明操作**全局变量**；`nonlocal` 声明操作**外层函数的局部变量**（仅在嵌套函数中使用，不能是全局变量）。

```python
x = 10         # 全局变量
def outer():
    y = 20     # 外层局部变量
    def inner():
        global x      # 改全局 x
        nonlocal y    # 改外层 y
```

**10. `sorted` 的 `key` 参数怎么用？**
> `key` 告诉 `sorted` 按什么排序。`lambda x` 的 `x` 依次是列表中每个元素，返回什么就按什么排。

```python
data = [("Alice", 85), ("Bob", 92)]
sorted(data, key=lambda x: x[1], reverse=True)  # 按成绩从高到低
sorted(data, key=lambda x: len(x[0]))            # 按姓名长度
```
