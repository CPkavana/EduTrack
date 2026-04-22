class Student:
    def __init__(self, name, age, dob, phone, reg_no):
        self.name = name
        self.age = age
        self.dob = dob
        self.phone = phone
        self.reg_no = reg_no

    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("DOB:", self.dob)
        print("Phone:", self.phone)
        print("Registration No:", self.reg_no)
        print("------------------------------")


students = []


def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    dob = input("Enter DOB (dd/mm/yyyy): ")
    phone = input("Enter Phone Number: ")
    reg_no = input("Enter Registration Number: ")
    s = Student(name, age, dob, phone, reg_no)
    students.append(s)
    print("Student added successfully!\n")


def show_students():
    if not students:
        print("No students available\n")
    else:
        for s in students:
            s.display()


def search_student():
    reg_no = input("Enter Registration Number to search: ")
    for s in students:
        if s.reg_no == reg_no:
            print("Student found!")
            s.display()
            return
    print("Student not found\n")


def remove_student():
    reg_no = input("Enter Registration Number to remove: ")
    for s in students:
        if s.reg_no == reg_no:
            students.remove(s)
            print("Student removed successfully!\n")
            return
    print("Student not found\n")


def update_student():
    reg_no = input("Enter Registration Number to update: ")
    for s in students:
        if s.reg_no == reg_no:
            print("Enter new details:")
            s.name = input("New Name: ")
            s.age = int(input("New Age: "))
            s.dob = input("New DOB: ")
            s.phone = input("New Phone: ")
            print("Student updated successfully!\n")
            return
    print("Student not found\n")


# Main Menu Loop
while True:
    print("\n==== Student Management System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        remove_student()
    elif choice == "6":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Please try again.\n")
