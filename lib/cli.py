# lib/cli.py
from pyfiglet import Figlet 
from pieces_cli import (
    pieces_menu,
    add_piece,
    view_pieces,
    delete_piece,
    update_piece)
from students_cli import (
    students_menu, 
    view_students, 
    add_student, 
    delete_student)
from select_student_cli import (
    select_a_student)


def greeting():
    print('')
    print(Figlet(font='big').renderText('Music Match'))
    print('Welcome!')
    print('')
    print('With this program, you can easily keep track of your students, pieces, and part assignments.')
    print('')
    print('Please select an option below (using the # pad) to get started:')
    print('')

    
def menu():
    print(Figlet(font='mini').renderText('Main Menu'))
    print("1. Students")
    print("")
    print("2. Pieces")
    print("")
    print("3. Exit the program")
    print('')


def main():
    option = 0
    while option != 3:
        menu()

        option = input("Option: ")
        students_choice = 0
        pieces_choice = 0

        if option == "1":
            while students_choice != 5:
                students_menu()
                students_choice = input('Option: ')
                if students_choice.isdigit() and 1 <= int(students_choice) <= 5:
                    students_choice = int(students_choice)
                    if students_choice == 1:
                        view_students()
                    elif students_choice == 2:
                        select_a_student()
                    elif students_choice == 3:
                        add_student()
                    elif students_choice == 4:
                        delete_student()
                    elif students_choice == 5:
                        main()
                else:
                    print('')
                    print("\033[1mInvalid Option - Try typing a listed number option\033[0m") 
                    print('') 

        elif option == "2":
            while pieces_choice != 5:
                pieces_menu()
                pieces_choice = input('Option: ')
                if pieces_choice.isdigit() and 1 <= int(pieces_choice) <= 5:
                    pieces_choice = int(pieces_choice)
                    if pieces_choice == 1:
                        view_pieces()
                    elif pieces_choice == 2:
                        update_piece()
                    elif pieces_choice == 3:
                        add_piece()
                    elif pieces_choice == 4:
                        delete_piece()
                    elif pieces_choice == 5:
                        main()
                else:
                    print('')
                    print("\033[1mInvalid Option - Try typing a listed number option\033[0m") 
                    print('') 

        elif option == "3":
            exit_program()

        else:
            print('')
            print("\033[1mInvalid Option - Try typing a listed number option\033[0m")
            print('')


def exit_program():
    print('')
    print(Figlet(font='big').renderText('Goodbye'))
    print('')
    exit()


if __name__ == "__main__":
    greeting()
    main()