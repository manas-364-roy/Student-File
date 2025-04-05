# List to store student information in memory
students = []

# Load existing student data from file
try:
    with open("Document.txt", "r") as f:
        for line in f:
            students.append(eval(line.strip()))
except FileNotFoundError:
    pass  # File doesn't exist yet, so we start with an empty list

while True:
    print("1. Add Student Information")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Delete Student by ID")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dept = input("Department Name: ")

        student = {"id": id, "name": name, "dept": dept}
        students.append(student)

        # Write the new student to the file
        with open("Document.txt", "a") as f:
            f.write(f"{student}\n")

        print("Student information added successfully.")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            for student in students:
                print(student)

    elif choice == "3":
        id = input("Enter Student ID to search: ")
        found = False
        for student in students:
            if student["id"] == id:
                print(student)
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        id = input("Enter Student ID to delete: ")
        found = False
        for student in students:
            if student["id"] == id:
                students.remove(student)
                found = True
                print("Student deleted successfully.")
                break
        if not found:
            print("Student not found.")
        else:
            # Rewrite the entire file with updated student list
            with open("Document.txt", "w") as f:
                for student in students:
                    f.write(f"{student}\n")

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")