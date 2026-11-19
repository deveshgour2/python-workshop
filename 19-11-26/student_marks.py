students = []

while True:
    print("1 for add student record")
    print("2 for display student record")
    print("3 for search student record")
    print("0 for exit")

    ch = int(input("enter your choice: "))

    if(ch == 1):
        name = input("enter student name: ")
        marks = []
        for i in range(3):
            m = float(input("enter marks: "))
            marks.append(m)
        total = sum(marks)
        percentage = total / 3
        if(percentage >= 60):
           div = "First Division"
        elif(percentage >= 50):
           div = "Second Division"
        elif(percentage >= 40):
           div = "Third Division"
        else:
           div = "Fail"

        student = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "division": div
        }

        #append dictionary data into list 
        students.append(student)
        print("Student record Added")

    elif(ch == 2):
        if(len(students) == 0):
            print("Record not found")

        else:
            for x in students:
                print(x["name"])
                print(x["marks"])
                print(x["percentage"])

    elif(ch == 3):
        search = input("enter record to be search: ")
        found = False 
        for s in students:
            print(s["name"])
            found = True
            break
        if(found == False):
            print("Record not found")

    elif(ch == 0):
        break
    else:
        print("Invalid choice")
    