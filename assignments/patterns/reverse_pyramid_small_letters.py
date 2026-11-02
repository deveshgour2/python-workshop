num = int(input("enter the size: "))

for i in range(num, 0, -1):
    for j in range(i):
        print(chr(97 + j), end=" ")
    print()
