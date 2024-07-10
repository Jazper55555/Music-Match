# lib/students_cli.py
from pyfiglet import Figlet
from models.student import Student


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
            print(f"\033[1m{student.first_name} {student.last_name}, {student.grade}th grade\033[0m")   

    print('')


def add_student():
    try:
        print('')
        new_first_name = input('Enter the new students first name: ')
        new_last_name = input('Enter the new students last name: ')
        new_grade = input('Enter the new students grade level: ')

        if new_grade.strip() == '':
            raise Exception(f"\033[1mGrade must be a number between 6 and 12\033[0m")

        new_student = Student.create(new_first_name, new_last_name, int(new_grade))
        print('')
        print(f"\033[1mSuccessfully created new student: {new_student.first_name} {new_student.last_name}, {new_student.grade}th grade\033[0m")  
    
    except Exception as exc:
        print('')
        print(f"\033[1mError creating student: \033[0m", exc)   


def delete_student():
    while True:
        print('')
        print('Choose from the following students to delete:')
        print('')
        students_list = Student.get_all()
        for i, student in enumerate(students_list, start=1):
                print(f'{i}. {student.first_name} {student.last_name}')
        
        print('')
        print('0. Go back to Students Menu')
        
        print('')
        choice = input('Enter the student number: ')
        
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            elif 1 <= choice <= len(students_list):            
                chosen_student = students_list[int(choice) - 1]
                chosen_student.delete()

                print('')
                print(f"\033[1mStudent {student.first_name} {student.last_name} successfully deleted\033[0m")   
                break

            else:
                print('')
                print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   
    
        else:
            print('')
            print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   