# #####################################################################
# PROJECT 7: STUDENT GRADE MANAGEMENT SYSTEM (FUNCTION-BASED)
# #####################################################################

students = [ {"name": "sanju", "marks": 95, "grade": "A+" }, {"name": "sravya", "marks": 88, "grade": "A"}, { "name": "surya", "marks": 79, "grade": "A" } ]

def add_student():
    name = input(" Enter Student Name: ")
    for student in students:
        if name == student["name"]:
            print(" Student Already there! ")
            return
        
    marks = int(input(" Enter Student Marks: "))
    if marks >= 90:
        grade = "A+"
    elif 79 <= marks <= 89:
        grade = "A"
    elif 60 <= marks < 79:
        grade = "B"
    else:
        grade = "F"
    new_student = {"name": name, "marks": marks, "grade": grade }
    students.append(new_student)
    print(students)
    return

    
def view_students():
    for number, student in enumerate(students, start=1):
        print(f" {number}. ")
        print("name:", student["name"]),
        print("marks:", student["marks"]),
        print("grade:", student["grade"])
        print()
        
def search_student():
        name = input(" Enter Student Name: ")
        for student in students:
            if name == student["name"]:
                print(" Student found! ")
                print(student)
                break
        else:
                print(" Student Not Found! ")
                return
            
def delete_student():
        name = input(" Enter Student Name: ")
        for student in students:
            if name == student["name"]:
                print(" Student found! ")
                students.remove(student)
                break
        else:
                print(" Student Doesn't Exist! ")
        return

                                
def show_topper():
        highest = 0
        for student in students:
            if student["marks"] > highest:
                highest = student["marks"]
                topper = student["name"]
                
        print("Highest marks", highest )
        print(" Topper is: ", topper )
                
        
def avg_marks():
    total_marks = 0
    total_students = len(students)
    for student in students:
        total_marks += student["marks"]
        average = total_marks / total_students
    print(" Total marks: ", total_marks)
    print(" Total Students: ", total_students)
    print(average)
    return
        
def save_data():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(student["name"] + "," + str(student["marks"]) + "," + student["grade"] + "," + "\n")
        print(" Data Saved Successfully")
        
def load_data():
    students.clear()
    with open("students.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            new_students = {"name": data[0], "marks": int(data[1]), "grade": data[2]}
            students.append(new_students)
        print(" Data loaded successfully")
        
while True:
    choice = input(" Enter 1. add student or 2. view student or 3. search student or 4. delete student or 5. show topper or 6. average marks or 7. save data or 8. load data or 9. Exit: ").lower()
    
    if choice == "1":
        add_student()
        
    elif choice == "2":
        view_students()
        
    elif choice == "3":
        search_student()
        
    elif choice == "4":
        delete_student()
        
    elif choice == "5":
        show_topper()
        
    elif choice == "6":
        avg_marks()
        
    elif choice == "7":
        save_data()
        
    elif choice == "8":
        load_data()
        
    elif choice == "9":
        print(" Exit Successful! ")
        break
        
    else:
        print(" Invalid Choice! ")

    
    
        
