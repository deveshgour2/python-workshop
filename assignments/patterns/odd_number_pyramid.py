size = int(input("enter the size: "))

for i in range(1, size + 1):
    num = 1
    for j in range(i):
        print(num , end=" ")
        num += 2
    print()