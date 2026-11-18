# 1. no return type no argument list function
# def addition():
#     a = int(input("enter the value of a: "))
#     b = int(input("enter the value of b: "))
#     print(a+b)

# addition()

# 2. no return type with arguments list function
# def addition(a, b):
#     print(a+b)

# addition( 10, 23)
# addition( 10.45, 23.23)
# addition( "new ", "Delhi")

# 3. with return type without argumnet list function
# def addition():
#     return(12 + 35)

# result = addition()
# print(result)

# def findMax():
#     x = 30
#     y = 20
#     if(x>y):
#         return(x)
#     else:
#         return(y)
# print("max no is - ", findMax())


# 4. function with return type with argumnet 
# def findMax(x, y):
#     if(x>y):
#         return(x)
#     else:
#         return(y)
# print("max no is - ", findMax(2, 5))


# 5. Default argument list function
# def addition(a=10, b=20, c=30):
#     print(a+b+c)

# addition()
# addition(100)
# addition(100,200)
# addition(100,200,300)


# 6. arbitrary argument list function
# def addition(*a):
#     print(type(a))
#     print((a))

# addition(100)
# addition(100,200)
# addition(100,200,300)
# addition(100,200,300,400)

# 7. keyword argument list function
# def product(name, code):
#     print("code- ", code)
#     print("name- ", name)
# product(name = "laptop", code = 100)

def product(**p):
    print(p) # its type is dictionary

product(name = "laptop", code = 100, price = 50000, color = "black")
