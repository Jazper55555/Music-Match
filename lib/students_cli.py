# lib/students_cli.py
from pyfiglet import Figlet
from models.student import Student

def students_menu():
    print("")
    print(Figlet(font='mini').renderText('Students'))
    print("1. View all students")
    print("")
    print("2. Select a student")
    print("")
    print("3. Add a student")
    print("")
    print("4. Delete a student")
    print("")
    print('5. Go back to Main Menu')
    print("")

def view_students():
    print('')
    students_list = Student.get_all()
    for student in students_list:
            print('')
            print(student)

def select_students():
    print('')
    print('Select from the following:')
    print('')
    students_list = Student.get_all()
    for i, student in enumerate(students_list, start=1):
            print(f'{i}. {student.first_name} {student.last_name}')
    
    print('')
    student_id = int(input('Option: '))
    chosen_student = Student.find_by_id(student_id)
    if chosen_student:
        print('')
        print(chosen_student)

    students_menu()

def add_student():
    print('')
    new_first_name = input('Enter the new students first name: ')
    new_last_name = input('Enter the new students last name: ')
    new_grade = input('Enter the new students grade level: ')

    new_student = Student.create(new_first_name, new_last_name, new_grade)
    try:
        print('')
        print(f'Successfully created student: {new_student}')
    except Exception as exc:
        print('Error creating student: ', exc)

    students_menu()

def delete_student():
    print('')
    print('Select from the following:')
    print('')
    students_list = Student.get_all()
    for i, student in enumerate(students_list, start=1):
            print(f'{i}. {student.first_name} {student.last_name}')
    
    print('')
    id_ = input('Enter the student number: ')
    if student := Student.find_by_id(id_):
        student.delete()
        print('')
        print(f'Student successfully deleted')
    else:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   

    students_menu()