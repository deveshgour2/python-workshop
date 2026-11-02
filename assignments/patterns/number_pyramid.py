size = int(input("enter the size: "))

num = 1

for i in range(1, size+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()