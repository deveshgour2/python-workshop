num = int(input("enter the number: "))

fact = 1
sum = 0
a = 1

while(a <= num):
    fact = fact * a
    sum = sum + fact
    a += 1
print(sum)