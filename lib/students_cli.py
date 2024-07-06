# lib/students_cli.py
from pyfiglet import Figlet
from models.student import Student
from models.part import Part
from models.piece import Piece


def students_menu():
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
    students_list = Student.get_all()
    for student in students_list:
            print('')
            print(f"\033[1m{student}\033[0m")   

    print('')


def add_student():
    print('')
    try:
        new_first_name = input('Enter the new students first name: ')
        new_last_name = input('Enter the new students last name: ')
        new_grade = input('Enter the new students grade level: ')

        new_student = Student.create(new_first_name, new_last_name, int(new_grade))
        print('')
        print(f"\033[1mSuccessfully created new student: {new_student}\033[0m")  
    except Exception as exc:
        print('')
        print(f"\033[1mError creating student: \033[0m", exc)   


def delete_student():
    print('')
    print('Choose from the following students to delete:')
    print('')
    students_list = Student.get_all()
    for student in students_list:
            print(f'{student.id}. {student.first_name} {student.last_name}')
    
    print('')
    print('0. Go back to Students Menu')
    
    print('')
    id_ = input('Enter the student id: ')
    if int(id_) == 0:
        students_menu()
        return
    if student := Student.find_by_id(id_):
        student.delete()
        print('')
        print(f"\033[1mStudent {student.first_name} {student.last_name} successfully deleted\033[0m")   
    else:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   
        delete_student()