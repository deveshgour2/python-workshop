import copy 
a = [[1,2,3], [4,5,6]]
print(a)

b = copy.deepcopy(a)
print(b)

b[0][0] = 99
a[0][0] = 1000
print("b= ",b)
print("a= ",a)