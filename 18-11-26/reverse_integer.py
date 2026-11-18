def reverse_integer(n):
    rev = 0 
    while n > 0:
        rev = rev * 10 
        rev += n % 10
        n = n // 10
    return rev

print(reverse_integer(int(input("enter the number: "))))