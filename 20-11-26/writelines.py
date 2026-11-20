x = open("students.txt", "w")
a = ["roll_no - 1, name- ram",
     "roll_no - 2, name- shyam",
     "roll_no - 3, name- ajay"
     ]
x.writelines(a)
print("list created")
x.close()