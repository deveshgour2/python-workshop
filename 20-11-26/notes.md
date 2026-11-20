# os module:- 
import os 

1. os.path.exists("filename"):- for check file exists or not on specified path.

2. os.remove():- for remove a file
os.remove("filename")

3. os.rmdir():- for remove folder.
os.rmdir("foldername")


===================================

# exception handling in python:- 
    error and exception can lead to program failure or unexpected behaviour, here python comes with a set of tools to manage exception. both error and exception occurs during the execution of program.

    we can handle exception by try and except block

* try :- inside the try block we can write any statement or business logic.

* except:- if the code contain any exception it will catch by except block.

* else:- if code not contain any exception than else block will be executed.(optional block)

* finally:- this block executes the code always.(optional block)


# syntax:- 
try:
    # statement or logic

except <exception_name>:
    # statement 

else: #OPTIONAL BLOCK
    # statement or logic 

finally: # optional block
    # statement


# types of exception classes:- 

1. ZeroDivisionError:- this exception is occurs when the number is divided by 0

2. NameError:- this exception is occurs when refernece/variable is undefined.

3. IndexError:- this exception is occurs when index is out of range

4. KeyError:- this exception is occura when key/index is not found in given collection.

5. IdentationError:- when identation is missing.

6. FileNotFoundError:- when file does not exists in the specified path this exception occurs.

7. ModuleNotFoundError:- if the given module is not in the python.


