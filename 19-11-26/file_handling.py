# create a new file
# fp = open("myfile.txt", "w")
# data = input("enter data to write into file: ")
# fp.write(data)
# print("file created successfully")

# fp = open("myfile.txt", "w")
# print(type(fp))
# print("mode: ",fp.mode)
# print("file name: ",fp.name)
# print("file status: ",fp.closed)

# data = input("enter data to write into file: ")
# fp.write(data)
# fp.close()
# print("file status: ",fp.closed)
# print("file closed successfully")

# read a file
# fp = open("myfile.txt", "r")
# # s = fp.read()
# s = fp.read(5)
# print("data in file: ", s)
# fp.close()

# append data into file
fp = open("myfile.txt", "a")
data = input("enter data to write into file: ")
fp.write(data)
print("file created successfully")

fp = open("myfile.txt", "a")
print(type(fp))
print("mode: ",fp.mode)
print("file name: ",fp.name)
print("file status: ",fp.closed)

# read a file
fp = open("myfile.txt", "r")
# s = fp.read()
s = fp.read(5)
print("data in file: ", s)
fp.close()