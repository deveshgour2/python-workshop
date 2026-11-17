# set methods 5
# s1 = {10,20,30}
# print(s1)
# s1.add(40)
# print(s1)
#s1.pop()
#s1.remove(20)
#s1.remove(200)
# s1.discard(200)

s1= {10,20,30}
s2 = {11,12,13,10}
# s3 = s1.difference(s2)
# s3 = s1.intersection(s2)
# s3 = s1.union(s2)
print(s1)
s1.update(s2)
print(s1)
del s1
# print(s1) #nameError