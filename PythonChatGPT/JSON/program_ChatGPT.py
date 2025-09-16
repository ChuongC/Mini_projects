import json

# Helper function to load JSON file
def load_students(file_name="students.json"):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data.get("Students", []), data.get("max_id", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return [], 0  # If file doesn't exist or JSON is invalid, return empty list and max_id = 0

# Helper function to save JSON file
def save_students(students, max_id, file_name="students.json"):
    with open(file_name, "w") as file:
        json.dump({"Students": students, "max_id": max_id}, file, indent=4)

# Function to generate a new unique ID
def generate_student_id(students):
    if not students:
        return 1
    return max(student["id"] for student in students) + 1

# Function to add a student
def add_student(students):
    name = input("Enter student's name: ").strip()
    age = input("Enter student's age: ").strip()
    
    if not name or not age.isdigit():
        print("Invalid input. Please provide a valid name and age.")
        return None  # Return None if input is invalid
    
    student_id = generate_student_id(students)  # Generate a unique ID
    students.append({"id": student_id, "name": name, "age": int(age)})
    
    save_students(students, student_id)  # Save with the updated student ID
    print(f"Student {name} (ID: {student_id}) added successfully.")
    return student_id  # Return the new max_id

# Function to display all students
def display_students(students):
    if students:
        print("List of students:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    else:
        print("No students found.")

# Function to delete a student by ID
def delete_student(students):
    student_id = input("Enter student ID to delete: ")
    
    if not student_id.isdigit():
        print("Invalid ID. Please enter a numeric ID.")
        return
    
    student_id = int(student_id)
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            save_students(students, max([s["id"] for s in students], default=0))
            print(f"Student with ID {student_id} deleted successfully.")
            return

    print(f"No student found with ID {student_id}.")

# Main menu
def main():
    students, max_id = load_students()  # Load students and current max ID
    options = {
        "1": lambda: add_student(students),
        "2": lambda: display_students(students),
        "3": lambda: delete_student(students),
        "4": exit
    }
    
    while True:
        print("\n1. Add student\n2. Display students\n3. Delete student by ID\n4. Exit")
        choice = input("Choose an option: ")

        if choice in options:
            if choice == "4":
                print("Exiting the program.")
                break
            elif choice == "1":
                new_id = options[choice]()  # Capture the new max_id after adding
                if new_id is not None:  # Only update if a new student was added
                    max_id = new_id
            else:
                options[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
