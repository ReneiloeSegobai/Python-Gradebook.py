Gradebook Management System

Overview
The Gradebook Management System is a Python program designed to aid the user with efficiently uploading, storing and managing student grades. It allows users to perform operations such as adding students, updating grades, viewing grades, and calculating averages. This system is implemented using object-oriented principles to ensure modularity and ease of maintenance.

Features of the Management System:
•	Add Students: 
Users are able to easily add new students together with their grades to the gradebook.
•	Remove Students:
User are able to remove existing students from the gradebook without complication.
•	Update Grades: 
users are able to add, update or delete grades from specific subjects belonging to a student.
•	View Subject Grades: 
Users are able to view every grade for a specific subject if they so choose .
•	Search Students: 
Users are able to search for specific students by name in order to view their grades and averages.
•	Display All Students: 
The Gradebook can be used to display all students and their respective grades.
•	Class Average: 
Users are able to efficiently calculate and display the class averages for all students and the subjects the averages belong to.

Code Structure

Main Classes:
•	Student.
•	Gradebook

Student

•	Attributes:  Name - The names of the student.
                     Grades - A dictionary mapping subjects to a list of grades.

•	Methods (functions that are associated with the object or a class in Python programming):

a) The Add_grade(subject, grade) method is used to add a grade for a specific subject.
      b) The calculate_average() method is used to calculate the average grade across all subjects.
             c) The print_details() method is used to print the student's details including grades and average.

Gradebook

•	Attributes: 
students: A dictionary mapping student names to Student objects.

Methods:
a) The add_student(name) is a method used to add a new student to the system
b) remove_student(name) is a method used to remove a student by name.
c) update_grades(name, subject, grade) is a method used to update a student's grades for a subject.
d) view_subject_grades(subject) is a method used  to view all the grades for a specific subject.
e) search_student_by_name(name) is a method used to search for a specific student by name and display their details.
f) display_all_students() is used to display the details of every student.
g) calculate_class_average()is used to calculate the average grade across all students and subjects.

Helper Functions
•	search_student_by_name(students) used to search and display details of a specific student.

•	update_grades(students, subjects) used when the user needs to update grades for existing students.

•	collect_student_data(number_students, subjects) help collect initial student data.


How to Run
First ensure that you have Python 3 or higher installed on your system. Proceed to save the code in a file named gradebook.py.
Open a terminal or command prompt and navigate to the directory containing the gradebook.py file.
Run the program with the command: python gradebook.py
Follow the on-screen prompts to perform various gradebook operations.

Usage Instructions
•	The program provides a menu with options for managing the gradebook so you will have to respond by entering the number corresponding to the action you as the user want to perform.

•	If the user wants to add, update or delete a name of a student, you will need to enter their name and grades for specific subjects.

•	Ensure the value grades entered are between 0 and 100 in order to yield a valid output.

•	You can view grades for specific subjects or search for students by entering their names to retrieve their details.

•	You can select the exit option to terminate the program.
Notes

I decided to implement input validation to ensure user inputs are valid for example., grades are within the 0-100 range.
Please ensure to follow the prompts provided carefully to avoid errors during input.

Future Enhancements

Future versions of the Gradebook Management system will have Save and Load Functionality, allowing gradebook data to be saved to a file and reloading it.

A Graphical User Interface (GUI) should be developed for easier interaction with the Gradebook management system

Author: Motheo Reneiloe Segobai

