# Function to prompt the user to enter the number of students in a class
def enter_number_of_students():
    while True:
        try:
            # Prompt the user for input
            number_students = int(input("Please enter the number of students in the class: "))

            # Check if the number is positive
            if number_students <= 0:
                print("Invalid input. The number of students must be greater than 0. Please try again.")
            else:
                return number_students
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to collect student names and grades for multiple subjects
def collect_student_data(number_students, subjects):
    students = {}
    for i in range(number_students):
        print(f"\nEntering data for student {i + 1}:")
        name = input("Enter the student's name: ").strip()
        while not name:
            print("Invalid input. Name cannot be empty.")
            name = input("Enter the student's name: ").strip()

        grades = {subject: [] for subject in subjects}  # Initialize an empty list for each subject
        
        for subject in subjects:
            while True:
                try:
                    grade = float(input(f"Enter the grade for {name} in {subject}: "))
                    if 0 <= grade <= 100:  # Grade validation
                        grades[subject].append(grade)  # Append the grade to the subject's list
                        break
                    else:
                        print("Invalid grade. Please enter a grade between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number for the grade.")
        
        # Add the student's name as the key and their grades dictionary as the value
        students[name] = grades
    return students

# Function to calculate the average grade for a student
def calculate_average(grades):
    if not grades:
        return 0  # No grades, average is 0
    total_grades = [grade for subject_grades in grades.values() for grade in subject_grades]  # Flatten all grades
    return sum(total_grades) / len(total_grades)

# Function to calculate highest and lowest grades for each subject
def calculate_subject_extremes(students, subjects):
    subject_extremes = {subject: {'highest': None, 'lowest': None} for subject in subjects}
    
    for name, grades in students.items():
        for subject in subjects:
            subject_grades = grades.get(subject, [])
            for grade in subject_grades:
                if subject_extremes[subject]['highest'] is None or grade > subject_extremes[subject]['highest']:
                    subject_extremes[subject]['highest'] = grade
                if subject_extremes[subject]['lowest'] is None or grade < subject_extremes[subject]['lowest']:
                    subject_extremes[subject]['lowest'] = grade

    return subject_extremes

# Function to add a new student
def add_student(students, subjects):
    name = input("Enter the student's name: ").strip()
    while not name:
        print("Invalid input. Name cannot be empty.")
        name = input("Enter the student's name: ").strip()

    grades = {subject: [] for subject in subjects}  # Initialize an empty list for each subject
    
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter the grade for {name} in {subject}: "))
                if 0 <= grade <= 100:
                    grades[subject].append(grade)  # Append the grade to the subject's list
                    break
                else:
                    print("Invalid grade. Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number for the grade.")
    
    students[name] = grades
    print(f"Student {name} has been added.")

# Function to view grades for a specific subject
def view_subject_grades(students, subjects):
    subject = input("Enter the subject to view grades: ").strip()
    if subject in subjects:
        print(f"\nGrades for {subject}:")
        for name, grades in students.items():
            if subject in grades:
                print(f"{name}: {grades[subject]}")
    else:
        print("Subject not found. Please check the list of subjects.")\

# Function to search for a student by name and retrieve their grades and average
def search_student_by_name(students, subjects):
    name = input("Enter the student's name to search: ").strip()
    
    if name in students:
        grades = students[name]
        print(f"\nGrades for {name}:")
        for subject, subject_grades in grades.items():
            print(f"  {subject}: {subject_grades}")
        
        # Calculate and display the average grade
        average_grade = calculate_average(grades)
        print(f"  Average Grade Across All Subjects: {average_grade:.2f}")
    else:
        print(f"Student {name} not found.")

# Function to update the grades of an existing student
def update_grades(students, subjects):
    name = input("Enter the name of the student whose grades you want to update: ").strip()
    if name in students:
        print(f"Updating grades for {name}:")
        for subject in subjects:
            while True:
                try:
                    grade = float(input(f"Enter the new grade for {name} in {subject}: "))
                    if 0 <= grade <= 100:
                        students[name][subject].append(grade)  # Append the new grade to the subject's list
                        break
                    else:
                        print("Invalid grade. Please enter a grade between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number for the grade.")
        print(f"Grades for {name} have been updated.")
    else:
        print(f"Student {name} not found.")

# Function to remove a student
def remove_student(students):
    name = input("Enter the name of the student you want to remove: ").strip()
    if name in students:
        del students[name]
        print(f"Student {name} has been removed.")
    else:
        print(f"Student {name} not found.")

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """Add a grade for a specific subject."""
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def calculate_average(self):
        """Calculate the average grade across all subjects."""
        total_grades = [grade for subject_grades in self.grades.values() for grade in subject_grades]
        if not total_grades:
            return 0  # No grades, average is 0
        return sum(total_grades) / len(total_grades)

    def print_details(self):
        """Print the student's details (grades and average)."""
        print(f"\nStudent: {self.name}")
        for subject, grades in self.grades.items():
            print(f"  {subject}: {grades}")
        print(f"  Average Grade Across All Subjects: {self.calculate_average():.2f}")

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        """Add a new student."""
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Student {name} has been added.")
        else:
            print(f"Student {name} already exists.")

    def remove_student(self, name):
        """Remove a student from the gradebook."""
        if name in self.students:
            del self.students[name]
            print(f"Student {name} has been removed.")
        else:
            print(f"Student {name} not found.")

    def update_grades(self, name, subject, grade):
        """Update grades for a student."""
        if name in self.students:
            student = self.students[name]
            student.add_grade(subject, grade)
            print(f"Grade for {subject} has been updated for {name}.")
        else:
            print(f"Student {name} not found.")

    def view_subject_grades(self, subject):
        """View grades for a specific subject."""
        print(f"\nGrades for {subject}:")
        for student in self.students.values():
            if subject in student.grades:
                print(f"{student.name}: {student.grades[subject]}")

    def search_student_by_name(self, name):
        """Search for a student by name and retrieve their grades and average."""
        if name in self.students:
            self.students[name].print_details()  # Print the student's details
        else:
            print(f"Student {name} not found.")

    def display_all_students(self):
        """Display the details of all students in the gradebook."""
        for student in self.students.values():
            student.print_details()

    def calculate_class_average(self):
        """Calculate and display the average grade for the whole class."""
        total_grades = []
        for student in self.students.values():
            total_grades.extend([grade for grades in student.grades.values() for grade in grades])
        if not total_grades:
            return 0
        return sum(total_grades) / len(total_grades)

# Function to collect student names and grades for multiple subjects
def collect_student_data(number_students, subjects):
    students = {}
    for i in range(number_students):
        print(f"\nEntering data for student {i + 1}:")
        name = input("Enter the student's name: ").strip()
        while not name:
            print("Invalid input. Name cannot be empty.")
            name = input("Enter the student's name: ").strip()

        student = Student(name)  # Create a Student object for the student
        
        for subject in subjects:
            while True:
                try:
                    grade = float(input(f"Enter the grade for {name} in {subject}: "))
                    if 0 <= grade <= 100:  # Grade validation
                        student.add_grade(subject, grade)  # Add grade for the subject
                        break
                    else:
                        print("Invalid grade. Please enter a grade between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number for the grade.")
        
        # Add the student object to the students dictionary
        students[name] = student
    return students

# Function to update the grades of an existing student
def update_grades(students, subjects):
    name = input("Enter the name of the student whose grades you want to update: ").strip()
    if name in students:
        student = students[name]
        print(f"Updating grades for {name}:")
        for subject in subjects:
            while True:
                try:
                    grade = float(input(f"Enter the new grade for {name} in {subject}: "))
                    if 0 <= grade <= 100:
                        student.add_grade(subject, grade)  # Add the new grade
                        break
                    else:
                        print("Invalid grade. Please enter a grade between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number for the grade.")
        print(f"Grades for {name} have been updated.")
    else:
        print(f"Student {name} not found.")

# Function to search for a student by name and retrieve their grades and average
def search_student_by_name(students):
    name = input("Enter the student's name to search: ").strip()
    
    if name in students:
        student = students[name]
        student.print_details()  # Print the student's details
    else:
        print(f"Student {name} not found.")

# Main function
if __name__ == "__main__":
    gradebook = Gradebook()

    # Example usage of the Gradebook class
    while True:
        print("\nChoose an action:")
        print("1. Add a new student")
        print("2. Remove a student")
        print("3. Update grades for an existing student")
        print("4. View grades for a specific subject")
        print("5. Search for a student by name")
        print("6. Display all students")
        print("7. Calculate class average")
        print("8. Exit")

        action = input("\nEnter the number of your choice: ").strip()

        if action == '1':
            name = input("Enter the student's name: ").strip()
            gradebook.add_student(name)
        elif action == '2':
            name = input("Enter the student's name to remove: ").strip()
            gradebook.remove_student(name)
        elif action == '3':
            name = input("Enter the student's name to update grades: ").strip()
            subject = input("Enter the subject: ").strip()
            grade = float(input("Enter the grade: "))
            gradebook.update_grades(name, subject, grade)
        elif action == '4':
            subject = input("Enter the subject to view grades: ").strip()
            gradebook.view_subject_grades(subject)
        elif action == '5':
            name = input("Enter the student's name to search: ").strip()
            gradebook.search_student_by_name(name)
        elif action == '6':
            gradebook.display_all_students()
        elif action == '7':
            print(f"Class average: {gradebook.calculate_class_average():.2f}")
        elif action == '8':
            print("\nThank you for using the gradebook. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")