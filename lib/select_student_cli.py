# lib/select_student_cli.py
from models.student import Student
from models.piece import Piece
from models.part import Part
    

def select_a_student():
    while True:
        print('')
        print('Select from the following:')
        print('')
        students_list = Student.get_all()
        for student in students_list:
                print(f'{student.id}. {student.first_name} {student.last_name}')

        print('')
        print('0. Go back to Students Menu')
        print('')

        choice = input('Option: ')

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            elif 1 <= choice <= len(students_list):
                chosen_student = students_list[choice - 1]
                student_menu(chosen_student)
                break

            else:
                print('')
                print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   

        else:
            print('')
            print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   


def student_menu(chosen_student):
    choice = 0
    while choice != 6:
        menu(chosen_student)

        choice = input('Option: ')

        if choice.isdigit() and 1 <= int(choice) <= 6:
            choice = int(choice)
            if choice == 1:
                update_student(chosen_student)
            elif choice == 2:
                view_parts(chosen_student)
            elif choice == 3:
                update_part(chosen_student)
            elif choice == 4:
                add_part(chosen_student)
            elif choice == 5:
                delete_part(chosen_student)
            elif choice == 6:
                break

            else:
                print('')
                print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m") 


def menu(chosen_student):
    print('')
    print(f"\033[1m***{chosen_student.first_name} {chosen_student.last_name}, {chosen_student.grade}th grade***\033[0m")   
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


def update_student(chosen_student):
    while True:
        print('')
        first_name = input('Enter the students updated first name: ')
        last_name = input('Enter the students updated last name: ')
        grade = input('Enter the students updated grade: ')

        if grade.isdigit() and first_name.strip() != '' and last_name.strip() != '':
            grade = int(grade)

            if 6 <= grade <= 12:
                chosen_student.first_name = first_name
                chosen_student.last_name = last_name
                chosen_student.grade = grade
                chosen_student.update()

                print('')
                print(f"\033[1mSuccessfully updated student: {chosen_student.first_name} {chosen_student.last_name}, {chosen_student.grade}th grade\033[0m") 
                break  

            else:
                print('')
                print(f"\033[1mGrade must be a number between 6 and 12\033[0m")

        else:
            print('')
            print(f"\033[1mError updating student: First name, last name, and grade cannot be empty \033[0m")  


def view_parts(chosen_student):
    print('')
    parts = chosen_student.parts()
    for part in parts:
        piece = part.piece()
        print(f"\033[1mPart: {part.instrument} from {piece.title} by {piece.composer}\033[0m")


def update_part(chosen_student):
    while True:
        print('')
        print('Choose from the following parts to update:')
        print('')
        parts = chosen_student.parts()
        for i, part in enumerate(parts, start=1):
                piece = part.piece()
                print(f"{i}. Part: {part.instrument} from {piece.title} by {piece.composer}")   
            
        print('')
        print(f'0. Go back to Student ({chosen_student.first_name} {chosen_student.last_name})')
        print('')

        choice = input('Enter the part number (or 0 to go back): ')
        print('')

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            if 1 <= choice <= len(parts):
                update_instrument = input('Update the part (instrument): ')
                if update_instrument.strip() == '':
                    print('')
                    print(f"\033[1mInstrument (part) must be text with at least 1 character\033[0m")
                    continue
            
                chosen_part = parts[choice - 1]

                chosen_part.instrument = update_instrument

                chosen_part.update()

                print('')
                print(f"\033[1mSuccessfully updated Part: {chosen_part.instrument}\033[0m")   
                break

            else:
                print('')
                print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m")   

        else:
            print('')
            print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m")   


def add_part(chosen_student):
    while True:
        print('')
        print('Choose from the following pieces to add a part:')
        print('')
        pieces_list = Piece.get_all()
        for i, piece in enumerate(pieces_list, start=1):
            print(f'{i}. {piece}')

        print('')
        print(f'0. Go back to Student ({chosen_student.first_name} {chosen_student.last_name})')
        print('')

        choice = input('Enter the piece number (or 0 to go back): ')

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            if 1 <= choice <= len(pieces_list):
                print('')
                chosen_piece = pieces_list[choice - 1]
                instrument_choice = input("Enter the part (instrument) assignment: ")
                if instrument_choice.strip() == '':
                    print('')
                    print(f"\033[1mInstrument (part) must be text with at least 1 character\033[0m")
                    continue

                print('')
                Part.create(instrument_choice, chosen_student.id, choice)

                print('')
                print(f"\033[1mSuccessfully created new Part: {instrument_choice} from {chosen_piece.title} by {chosen_piece.composer}\033[0m") 
                break
        
            else:
                print('')
                print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m")

        else:
            print('')
            print((f"\033[1mInvalid Option - Try typing a listed number option\033[0m")) 


def delete_part(chosen_student):
    while True:
        print('')
        print('Choose from the following parts to delete:')
        print('')
        parts = chosen_student.parts()
        for i, part in enumerate(parts, start=1):
                piece = part.piece()
                print(f"{i}. Part: {part.instrument} from {piece.title} by {piece.composer}") 

        print('')
        print(f'0. Go back to Student ({chosen_student.first_name} {chosen_student.last_name})')
        print('')

        choice = input('Enter the part number (or 0 to go back): ')

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                break
            if 1 <= choice <= len(parts):
                chosen_part = parts[choice - 1]
                chosen_part.delete()

                print('')
                print(f"\033[1mSuccessfully deleted Part: {chosen_part.instrument} from {piece.title} by {piece.composer}\033[0m") 
                break
        
            else:
                print('')
                print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m")

        else:
            print('')
            print("\033[1mInvalid Option - Try typing a listed number option\033[0m")  