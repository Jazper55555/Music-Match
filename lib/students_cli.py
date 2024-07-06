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


def select_students(chosen_student=None):
    print('')
    print('Select from the following:')
    print('')
    students_list = Student.get_all()
    for student in students_list:
            print(f'{student.id}. {student.first_name} {student.last_name}')
    
    print('')
    print('0. Go back to Students Menu')
    print('')
    try:
        if chosen_student is None:
            student_id = int(input('Option: '))
            if student_id == 0:
                return
            if not any(student.id == student_id for student in students_list):
                raise ValueError
            chosen_student = Student.find_by_id(student_id)

        student_choices = 0
        while student_choices != 6:
            if chosen_student:
                try:
                    print('')
                    print(f"\033[1m{chosen_student}\033[0m")   
                    print('')
                    print('1. Update student')
                    print('')
                    print('2. View pieces/parts')
                    print('')
                    print('3. Update parts')
                    print('')
                    print('4. Add a part')
                    print('')
                    print('5. Delete a part')
                    print('')
                    print('6. Go back to Students Menu')
                    print('')

                    student_choices = int(input('Option: '))
                    if student_choices < 1 or student_choices > 6:
                        raise ValueError
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
                        add_part(chosen_student.id)
                        return
                    elif student_choices == 5:
                        delete_part(chosen_student.id)
                        return
                    elif student_choices == 6:
                        return
                    else:
                        print('')
                        print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m") 
                        print('')

                except ValueError:
                    print('')
                    print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m") 
                    select_students(chosen_student)

    except ValueError:
        print('')
        print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m") 
        select_students()  


def update_student(student_id):
    print('')
    chosen_student = Student.find_by_id(student_id)
    if chosen_student:
        try:
            first_name = input('Enter the students updated first name: ')
            last_name = input('Enter the students updated last name: ')
            grade = input('Enter the students updated grade: ')

            chosen_student.first_name = first_name
            chosen_student.last_name = last_name
            chosen_student.grade = grade

            chosen_student.update()

            print('')
            print(f"\033[1mSuccessfully updated student: {chosen_student}\033[0m")   
        except Exception as exc:
            print('')
            print(f"\033[1mError updating student:\033[0m", exc)   


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
    print('Choose from the following pieces to update:')
    print('')
    pieces_list = Part.student_parts(student_id)
    for piece in pieces_list:
        piece_title = Piece.find_by_id(piece.piece_id)
        print(f"\033[1m{piece_title.id}. Piece: {piece_title.title} by {piece_title.composer}; Part: {piece.instrument}\033[0m")   
    
    print('')
    piece_id = int(input('Enter the piece id: '))
    update_instrument = input('Update the part: ')
    chosen_part = Part.find_by_student_and_piece_id(student_id, piece_id)

    try:
        if chosen_part:
            chosen_part.instrument = update_instrument

            chosen_part.update()
            print('')
            print(f"\033[1mSuccessfully updated Part: {chosen_part.instrument}\033[0m")   
    except Exception as exc:
            print('Error updating part: ', exc) 


def add_part(student_id):
    try:
        print('')
        print('Choose from the following pieces to add a part:')
        print('')
        pieces_list = Piece.get_all()
        for piece in pieces_list:
            print(f'{piece.id}. {piece}')
        print('')
        piece_id = int(input('Enter the piece id: '))
        
        print('')
        instrument_choice = input("Enter the instrument (part) assignment: ")

        print('')
        new_part = Part.create(instrument_choice, student_id, piece_id)
        piece_display = Piece.find_by_id(piece_id)

        print('')
        print(f"\033[1mSuccessfully created new part: Instrument: {instrument_choice}; Piece: {piece_display.title} by {piece_display.composer}\033[0m") 
    except Exception as exc:
        print('')
        print(f"\033[1mError creating part: \033[0m", exc)

    students_menu()   


def delete_part(student_id):
    try:
        print('')
        print('Choose from the following parts to delete:')
        print('')
        parts = Part.student_parts(student_id)
        for part in parts:
            piece_title = Piece.find_by_id(part.piece_id)
            print(f"{part.id}. Piece: {piece_title.title} by {piece_title.composer}; Part: {part.instrument}") 

        print('')
        part_id = int(input('Enter the part id: '))
        part = Part.find_by_id(part_id)
        part.delete()

        print('')
        print(f"\033[1mSuccessfully deleted Part: {part.instrument}; Piece: {piece_title.title} by {piece_title.composer}\033[0m") 
    except Exception:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")


def add_student():
    print('')
    try:
        new_first_name = input('Enter the new students first name: ')
        new_last_name = input('Enter the new students last name: ')
        new_grade = input('Enter the new students grade level: ')

        new_student = Student.create(new_first_name, new_last_name, new_grade)
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