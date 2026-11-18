# Types of Functions in Python

### 1. No Return Type, No Argument List Function

**Definition:** A function that does not accept any arguments and does not return any value. It performs operations inside the function.

**Syntax:**
```python
def function_name():
    # statements

function_name()
```

### 2. No Return Type, With Argument List Function

**Definition:** A function that accepts arguments from the function call but does not return any value. It performs operations using the received arguments.

**Syntax:**
```python
def function_name(a, b):
    # statements

function_name(value1, value2)
```

### 3. With Return Type, Without Argument List Function

**Definition:** A function that does not accept any arguments but returns a value after performing an operation.

**Syntax:**
```python
def function_name():
    # statements
    return value

result = function_name()
```

### 4. With Return Type, With Argument List Function

**Definition:** A function that accepts arguments, performs operations using them, and returns the result to the calling statement.

**Syntax:**
```python
def function_name(a, b):
    # statements
    return value

result = function_name(value1, value2)
```

### 5. Default Argument Function

**Definition:** A function in which arguments are assigned default values in the function definition. If values are not provided during the function call, the default values are used.

**Syntax:**
```python
def function_name(a=10, b=20):
    # statements

function_name()
function_name(value1)
function_name(value1, value2)
```

### 6. Arbitrary Argument List Function (`*args`)

**Definition:** A function that accepts any number of positional arguments. Python collects all received positional arguments into a tuple.

**Syntax:**
```python
def function_name(*args):
    # statements

function_name(value1, value2, value3)
```

### 7. Keyword Argument List Function (`**kwargs`)

**Definition:** A function that accepts any number of keyword arguments. Python collects all received keyword arguments into a dictionary.

**Syntax:**
```python
def function_name(**kwargs):
    # statements

function_name(name="laptop", price=50000, color="black")
```

========================================================

# module in python:- 
 a module is simply a python file containing python code. inside module we can define functions, classes and variables that can be used in other python programs. module file name extension is ".py"


# types of modules:- 
1. custom module/ user defined module:- 
    a module which is design as per our program needs called user defined module.

2. predefined/ system-defined/ system defined module:-
    a module which is already available in python library called predefined module.
exp:- copy, sys, math, keyword, os, date, time, etc

this module file is access on other file using 
1. import keyword
2. as keyword for renaming a module
3. from keyword 
=====================================================

# note:- 
__pycache__ it is a folder
custom_module.cpython-314.pyc
where custom_module is a file name
.c is compiled python file
314 is pyhton version
pyc is compiled file extension

=====================================================

1. wap to check pallindrome no
2. wap for check string pallindrome or not
3. wap for reverse of any digit no
4. wap for check year is leap or not 
5. wap for generate fibonacci series 
