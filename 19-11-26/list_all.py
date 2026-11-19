import sys 
student = []

while True:
    print("1 for add")
    print("2 for display")
    print("3 for clear records")
    print("4 for search student")
    print("0 for exit ")
    ch = int(input("Enter your choice: "))
    if(ch == 1):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))
        x = [name,age,marks]
        student.append(x)
        print("student added successfully")
    elif(ch == 2):
        if(len(student) == 0):
            print("No student found")
        else:
            for x in student:
                print("name: ",x[0])
                print("age: ",x[1])
                print("marks: ",x[2])   
                print("-------------------")

    elif(ch == 3):
        student.clear()
        print("Records cleared successfully")

    elif(ch == 4):
        name = input("enter name to search: ")
        found = False
        for x in student:
            if(x[0] == name):
                print("name: ",x[0])
                print("age: ",x[1])
                print("marks: ",x[2])   
                print("-------------------")
                found = True
        if(found == False):
            print("No student found with name:",name)

    elif(ch == 0):
       sys.exit()
    else:
        print("Invalid choice")
