class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = {
                "name": name,
                "age": age,
                "grade": grade
            }
            print(f"Student {name} added successfully!")

    def remove_student(self, student_id):
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Student {removed_student['name']} removed successfully!")
        else:
            print(f"Student with ID {student_id} not found.")

    def search_student(self, student_id=None, name=None):
        if student_id:
            if student_id in self.students:
                return self.students[student_id]
            else:
                print(f"No student found with ID {student_id}.")
                return None
        elif name:
            for student_id, details in self.students.items():
                if details["name"].lower() == name.lower():
                    return {student_id: details}
            print(f"No student found with the name {name}.")
            return None
        else:
            print("Please provide a student ID or name to search.")
            return None

    def display_all_students(self):
        if not self.students:
            print("No students to display.")
        else:
            for student_id, details in self.students.items():
                print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Grade: {details['grade']}")

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id in self.students:
            if name:
                self.students[student_id]["name"] = name
            if age:
                self.students[student_id]["age"] = age
            if grade:
                self.students[student_id]["grade"] = grade
            print(f"Student ID {student_id} updated successfully!")
        else:
            print(f"Student with ID {student_id} not found.")

sms = StudentManagementSystem()

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Update Student")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        grade = input("Enter Student Grade: ")
        sms.add_student(student_id, name, age, grade)
        
    elif choice == "2":
        student_id = input("Enter Student ID to remove: ")
        sms.remove_student(student_id)
        
    elif choice == "3":
        search_choice = input("Search by (1) ID or (2) Name: ")
        if search_choice == "1":
            student_id = input("Enter Student ID: ")
            result = sms.search_student(student_id=student_id)
            if result:
                print(f"Student found: {result}")
        elif search_choice == "2":
            name = input("Enter Student Name: ")
            result = sms.search_student(name=name)
            if result:
                print(f"Student found: {result}")
        else:
            print("Invalid search option.")
            
    elif choice == "4":
        sms.display_all_students()
        
    elif choice == "5":
        student_id = input("Enter Student ID to update: ")
        name = input("Enter new name (leave blank to skip): ")
        age = input("Enter new age (leave blank to skip): ")
        grade = input("Enter new grade (leave blank to skip): ")
        
        sms.update_student(student_id, name if name else None, age if age else None, grade if grade else None)
        
    elif choice == "6":
        print("Exiting the system.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
