# zero division error
# try:
#     x = 10
#     y = 0
#     z = x/y
#     print(z)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")


# Name Error
# try:
#     a = 4
#     print(x)
# except NameError:
#     print("variable is not defined")


# index error
# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except IndexError:
#     print("Error: Index out of range.")


# key error
# try:
#     student = {
#         "roll_no": 44,
#         "name":"devesh"
#     }
#     print(student["city"])
# except KeyError:
#     print("key not found")


# try:
#     x = int(input("Enter a number: "))
#     y = int(input("Enter a number: "))
#     z = x/y

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# else:
#     print(z)

# finally:
#     print("Execution completed.")



# FileNotFoundError
# try:
#     fp = open("students1.txt", "r")
#     s = fp.read()
    
# except FileNotFoundError:
#     print("file not found")

# else:
#     print("file content is: ", s)


# ModuleNotFoundError
try:
    import math1
    math1.sqrt(16)
except ModuleNotFoundError:
    print("module not found")
    