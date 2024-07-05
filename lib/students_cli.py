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

    students_menu()


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
    student_choices = 0
    if chosen_student:
        print('')
        print(f"\033[1m{chosen_student}\033[0m")   
        print('')
        print('1. Update student')
        print('')
        print('2. View pieces/parts')
        print('')
        print('3. Update parts')
        print('')
        print('4. Go back to Students Menu')
        print('')

        while student_choices != 4:
            student_choices = int(input('Option: '))
            if student_choices == 1:
                update_student(chosen_student.id)
                return
            elif student_choices == 2:
                display_student_parts(chosen_student.id)
                return
            elif student_choices == 3:
                update_parts(chosen_student.id)
                return
            elif student_choices == 4:
                students_menu()


def update_student(student_id):
    print('')
    chosen_student = Student.find_by_id(student_id)
    if chosen_student:
        first_name = input('Enter the students updated first name: ')
        last_name = input('Enter the students updated last name: ')
        grade = input('Enter the students updated grade: ')

        chosen_student.first_name = first_name
        chosen_student.last_name = last_name
        chosen_student.grade = grade

        chosen_student.update()

        try:
            print('')
            print(f"\033[1mSuccessfully updated student: {chosen_student}\033[0m")   
        except Exception as exc:
            print('Error updating student: ', exc)

    students_menu()


def display_student_parts(student_id):
    chosen_student = Student.find_by_id(student_id)
    if chosen_student:
        parts = Part.student_parts(student_id)
        for part in parts:
            piece_title = Piece.find_by_id(part.piece_id)
            print('')
            print(f"\033[1mPiece: {piece_title.title} by {piece_title.composer}; Part: {part.instrument}\033[0m")   

    students_menu()


def update_parts(student_id):
    print('')
    print('Choose from the following pieces:')
    print('')
    pieces_list = Part.student_parts(student_id)
    for piece in pieces_list:
        piece_title = Piece.find_by_id(piece.piece_id)
        print(f"\033[1m{piece_title.id}. Piece: {piece_title.title} by {piece_title.composer}; Part: {piece.instrument}\033[0m")   
    
    print('')
    piece_id = int(input('Enter the piece id: '))
    update_instrument = input('Update the part: ')
    chosen_part = Part.find_by_student_and_piece_id(student_id, piece_id)

    if chosen_part:
        chosen_part.instrument = update_instrument

        print('')
        try:
            chosen_part.update()
            print('')
            print(f"\033[1mSuccessfully updated Part: {chosen_part.instrument}\033[0m")   
        except Exception as exc:
            print('Error updating part: ', exc) 

    students_menu()
    

def add_student():
    print('')
    new_first_name = input('Enter the new students first name: ')
    new_last_name = input('Enter the new students last name: ')
    new_grade = input('Enter the new students grade level: ')

    new_student = Student.create(new_first_name, new_last_name, new_grade)
    try:
        print('')
        print(f"\033[1mSuccessfully created new student: {new_student}\033[0m")   
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
    id_ = input('Enter the student id: ')
    if student := Student.find_by_id(id_):
        student.delete()
        print('')
        print(f"\033[1mStudent {student.first_name} {student.last_name} successfully deleted\033[0m")   
    else:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   

    students_menu()