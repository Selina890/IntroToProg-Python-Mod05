# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Lim, 07/30/2024,Created Script
#   
# ------------------------------------------------------------------------------------------ #
import json
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str,str] = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = '' # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except Exception as e:
    print("File not found. Check that the file is in json format")
    print("-- Technical Error Message -- ")

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")
            student_data = {'FirstName':student_first_name, 'LastName':student_last_name, 'CourseName':course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except Exception as e:
            print("Invalid input. Please try again.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)    # Print the documentation string of the exception type
            print(e.__str__())  # Print the string representation of the exception
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student_data in students:
            print(f"Student {student_data['FirstName']} {student_data['LastName']} is enrolled in {student_data['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            print("The following data was saved to file!")
            for student_data in students:
                print(f"Student {student_data['FirstName']} {student_data['LastName']} is enrolled in {student_data['CourseName']}")
            file.close()
            continue

        except Exception as e:
            if file.closed == False:
                file.close()
            print("Error: Cannot write to the file.")
            print("Check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)    # Print the documentation string of the exception type
            print(e.__str__())  # Print the string representation of the exception

        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
