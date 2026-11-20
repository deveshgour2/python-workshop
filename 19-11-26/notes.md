# fromkeys():- 
    this method removes duplicate data from list.

# file 
    by using file handling we can store any info in form of file.
=> for file handling python provides function.
1. open():- by this function we can create a new file or open an existing file.

* filepointer = open("path", mode)

filemode
w - for write
r - for read
a - for append


2. write() for writing content in a file.

filepointer.write(data)


3. read():- for read content from a file.
 return str = filepointer.read(length)

 read() use with or without passing parameter.
 here we can pass length of character in numbers.

4. close():- for closing  a open file.
filepointer.close()

=======================================
difference b/w close() and closed property


5. readline():- this function read only single line of specified file 

* return str = filepointer.readline()

6. readlines() :- this function read all content of specified file. this function returns a list containing each line as list data/item.

* return str = filepointer.readlines()

7. writelines():- this function is used to write data in a file
* return int = filepointer.writelines([list])