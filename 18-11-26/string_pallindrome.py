def string_pallindrome(s):
    rev = ""
    for i in s:
        rev = i + rev
    if s == rev:
        print("pallindrome")
    else:
        print("not a pallindrome")
string_pallindrome(input("enter the string: "))