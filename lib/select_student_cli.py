# lib/select_student_cli.py
from models.student import Student
from models.piece import Piece
from models.part import Part
    

def select_a_student():
    try:
        print('')
        print('Select from the following:')
        print('')
        students_list = Student.get_all()
        for student in students_list:
                print(f'{student.id}. {student.first_name} {student.last_name}')

        print('')
        print('0. Go back to Students Menu')
        print('')

        choice = int(input('Option: '))
        if choice == 0:
            return
        if choice > len(students_list):
            raise ValueError

        chosen_student = students_list[choice - 1]
        student_menu(chosen_student)
    
    except ValueError:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   
        select_a_student()
        return


def student_menu(chosen_student):
    while True:
        # try:
            print('top of the loop')
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
            print('6. Go back to Students')
            print('')

            choice = int(input('Option: '))

            # if choice < 1 or choice > 6:
            #     raise ValueError
            if choice == 1:
                update_student(chosen_student)
                # return
            elif choice == 2:
                view_parts(chosen_student)
                print('done with viewing')
                # return
            elif choice == 3:
                update_part(chosen_student)
                # return
            elif choice == 4:
                add_part(chosen_student)
                # return
            elif choice == 5:
                delete_part(chosen_student)
                # return
            elif choice == 6:
                select_a_student()
                # return

            else:
                print('')
                print(f"\033[1mSTUDENT MENU Invalid Option - Try typing a listed number option\033[0m") 
        
            print('Done with if')
            # student_menu(chosen_student)
            # return


def update_student(chosen_student):
    try:
        print('')
        first_name = input('Enter the students updated first name: ')
        last_name = input('Enter the students updated last name: ')
        grade = input('Enter the students updated grade: ')

        if grade.strip() == '':
            raise Exception(f"\033[1mGrade must be a number between 6 and 12\033[0m")

        else:
            chosen_student.first_name = first_name
            chosen_student.last_name = last_name
            chosen_student.grade = int(grade)
            chosen_student.update()

            print('')
            print(f"\033[1mSuccessfully updated student: {chosen_student.first_name} {chosen_student.last_name}, {chosen_student.grade}th grade\033[0m")   
    
    except Exception as exc:
        print('')
        print(f"\033[1mError updating student:\033[0m", exc)  
        student_menu(chosen_student) 
        return

    student_menu(chosen_student)


def view_parts(chosen_student):
    print('')
    parts = chosen_student.find_parts()
    print('parts')
    for part in parts:
        print('piece')
        piece = part.find_piece()
        # change find_piece() to piece()
        print(f"\033[1mPart: {part.instrument} from {piece.title} by {piece.composer}\033[0m")

    print('done with printing')

    # student_menu(chosen_student)


def update_part(chosen_student):
    try:
        print('')
        print('Choose from the following parts to update:')
        print('')
        parts = chosen_student.find_parts()
        for i, part in enumerate(parts, start=1):
                piece = part.find_piece()
                print(f"{i}. Part: {part.instrument} from {piece.title} by {piece.composer}")   
            
        print('')
        print(f'0. Go back to Student ({chosen_student.first_name} {chosen_student.last_name})')
        print('')
        choice = int(input('Enter the part number (or 0 to go back): '))
        print('')

        if choice == 0:
            student_menu(chosen_student)
            return
        if choice > len(parts):
            raise ValueError
        
        try:
            update_instrument = input('Update the part (instrument): ')
            chosen_part = parts[choice - 1]

            chosen_part.instrument = update_instrument

            chosen_part.update()

            print('')
            print(f"\033[1mSuccessfully updated Part: {chosen_part.instrument} from {piece.title} by {piece.composer}\033[0m")   

        except Exception as exc:
            print('')
            print(f"\033[1mError updating part:\033[0m", exc) 

    except ValueError:
        print('')
        print(f"\033[1mInvalid Option - Try typing a listed number option\033[0m")   
        update_part(chosen_student)
        return       

    student_menu(chosen_student)


def add_part(chosen_student):
    try:
        print('')
        print('Choose from the following pieces to add a part:')
        print('')
        pieces_list = Piece.get_all()
        for i, piece in enumerate(pieces_list, start=1):
            print(f'{i}. {piece}')

        print('')
        print(f'0. Go back to Student ({chosen_student.first_name} {chosen_student.last_name})')
        print('')

        choice = int(input('Enter the piece number (or 0 to go back): '))
        if choice == 0:
            student_menu(chosen_student)
            return
        if choice == '' or int(choice) > len(pieces_list):
            raise ValueError
        
        try:
            print('')
            chosen_piece = pieces_list[choice - 1]
            instrument_choice = input("Enter the part (instrument) assignment: ")

            print('')
            Part.create(instrument_choice, chosen_student.id, int(choice))

            print('')
            print(f"\033[1mSuccessfully created new Part: {instrument_choice} from {chosen_piece.title} by {chosen_piece.composer}\033[0m") 
    
        except Exception as exc:
            print('')
            print(f"\033[1mError updating part:\033[0m", exc)
            add_part(chosen_student)
            return

    except ValueError:
        print('')
        print((f"\033[1mInvalid Option - Try typing a listed number option\033[0m")) 
        add_part(chosen_student)
        return
    
    student_menu(chosen_student)


def delete_part(chosen_student):
    try:
        print('')
        print('Choose from the following parts to delete:')
        print('')
        parts = chosen_student.find_parts()
        for i, part in enumerate(parts, start=1):
                piece = part.find_piece()
                print(f"{i}. Part: {part.instrument} from {piece.title} by {piece.composer}") 

        print('')
        print(f'0. Go back to Student ({chosen_student.first_name} {chosen_student.last_name})')
        print('')
        choice = int(input('Enter the part number (or 0 to go back): '))

        if choice == 0:
            student_menu(chosen_student)
            return
        if choice > len(parts):
            raise ValueError
       
        try:
            chosen_part = parts[choice - 1]
            chosen_part.delete()

            print('')
            print(f"\033[1mSuccessfully deleted Part: {chosen_part.instrument} from {piece.title} by {piece.composer}\033[0m") 
    
        except Exception as exc:
            print('')
            print(f"\033[1mError deleting part:\033[0m", exc)

    except ValueError:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")  
        delete_part(chosen_student)
        return
    
    student_menu(chosen_student)