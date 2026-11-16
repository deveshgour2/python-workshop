# # # s = """python is a programming language. Python has collection of modules"""
# # # print(s)
# # # print(s.upper())
# # # print(s.lower())
# # # print(s.capitalize())
# # # print(s.title())

# # # s1 = "PYTHON"
# # # print(s1.swapcase())

# # # s = "  test  "
# # # print(len(s))
# # # s2 = s.strip()
# # # print(len(s2))

# # # s = """python is a programming language. python has collection of modules"""
# # # print(s)
# # # s1 = s.replace("python", "java", 1)
# # # print(s1)

# # # dt1 = "16/11/2026"
# # # print(dt1)
# # # a=dt1.split("/")
# # # print(a)
# # # s= a[2] + "-" + a[1] + "-" + a[0]
# # # print(s)

# # # s = "sunset.jpg"
# # # print(s)
# # # a = s.split(".")
# # # a[0] = "logo"
# # # s1 = a[0] + "."+ a[1]
# # # print(s1)

# # # #join method
# # # a = ["test", "string"]
# # # print(a)
# # # print("-".join(a))

# # # s = "abc"
# # # #s[0] = "X" #immutable :TypeError
# # # #print(s)

# # # list1 = list(s)
# # # list1[0] = "x"
# # # print(list1)
# # # s1 = "".join(list1)
# # # print(s1)

# # # s = "abc"
# # # s2 = s.replace("a", "x")
# # # print(s2)

# # # s = "test data"
# # # print(s.find("data"))
# # # print(s.find("abc"))

# # s = input("enter the string: ")
# # vowels = "aeiouAEIOU"
# # consonant = 0
# # count  = 0
# # for i in s:
# #     if i in vowels:
# #         count += 1
# #     else:
# #         consonant += 1
# # print("no of vowels= ",count)
# # print("no of consonant= ", consonant)

# # reverse string
# s = input("enter any string: ")
# print("before reverse:- ", s)
# rev = ""
# for i in s:
#     rev = i + rev
# print("after reverse:- ",rev)
    

#string pallindrome
s = input("enter the string: ")
rev = ""
for i in s:
    rev = i + rev
if(rev == s):
    print("string is pallindrome")
else:
    print("string is not pallindrome")