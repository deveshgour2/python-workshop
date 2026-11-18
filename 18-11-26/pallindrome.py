def pallindrome(n):
    rev = 0
    temp = n
    while n > 0:
        rev = rev * 10
        rev += n % 10
        n = n // 10
    if temp  == rev:
        print("pallindrome")
    else:
        print("not a pallindrome")
(pallindrome(int(input("enter the number: "))))