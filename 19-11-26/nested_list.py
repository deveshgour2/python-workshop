a = [[1,2],[1,2],[3,4]]
print(a)
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)