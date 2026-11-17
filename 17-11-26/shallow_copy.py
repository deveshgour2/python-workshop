import copy 
a = [[1,2,3], [4,5,6]]
print(a)

b = copy.copy(a)
print(b)

b[0][0] = 99
print("b= ",b)
print("a= ",a)