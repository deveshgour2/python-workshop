size = int(input("enter the size: "))

for i in range(1, size+1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()