# #####################################################################
# PROJECT 4: STUDENT MANAGEMENT SYSTEM (FUNCTION-BASED)
# #####################################################################

students = ["Surya", "Sanjith", "ChatGPT",
            "Nani", "Prabhas", "Priya", "Sita"]

def add_student():
    while True:
        student = input(" Enter New Student name: ")
        if student not in students:
            print(student, "Added Successfully! ")
            print(" Welcome ", student)
            students.append(student)
            print(students)
            break
        else:
            print(" Student already exists! ")

def view_students():
    count = 1
    for student in students:
        print(count, student)
        count += 1

def search_student():
    student = input(" Enter student name: ")
    if student in students:
        print(" Student found! ", student)
    else:
        print(" Student Not Found")

def remove_student():
    while True:
        out = input(" Enter Student you want to remove: ")
        if out in students:
            print(" Student found! Removed", out, "Successfully! ")
            students.remove(out)
            print(students)
            break
        else:
            print(" Student not found! ")

def count_students():
    count = len(students)
    print(count, "Students are there!")


print(" Student Management System")
while True:

    print(" Choice is Case Sensitive! Enter Your Choice in Small letters. ")

    choice = input(" Add Student or View Students or Search Student or Remove Students or Count Students or Exit: ")

    if choice == "add student":
        add_student()

    elif choice == "view students":
        view_students()

    elif choice == "search student":
        search_student()

    elif choice == "remove student":
        remove_student()

    elif choice == "count students":
        count_students()

    elif choice == "exit":
        print(" Exit Successful! ")
        break

    else:
        print(" Invalid Choice! Check properly! Choice is Case Sensitive.")

