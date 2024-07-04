# lib/cli.py
from pyfiglet import Figlet 
from pieces_cli import pieces
from students_cli import (
    students_menu, 
    view_students, 
    select_students, 
    add_student, 
    delete_student)


def greeting():
    print('')
    print(Figlet(font='big').renderText('Music Assignments'))
    print('Welcome!')
    print('')
    print('With this program, you can easily keep track of your students and their part assignments.')
    print('')
    print('Please select an option below (using the # pad) to get started:')
    print('')

def main():
    option = 0
    while option != 3:
        menu()

        option = input("Option: ")
        students_choice = 0
        pieces_choice = 0

        if option == "1":
            students_menu()
            while students_choice != 5:
                students_choice = int(input('Option: '))
                if students_choice == 1:
                    view_students()
                    students_menu()
                elif students_choice == 2:
                    select_students()
                elif students_choice == 3:
                    add_student()
                elif students_choice == 4:
                    delete_student()
                elif students_choice == 5:
                    menu()
                else:
                    print("")
                    print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   

        elif option == "2":
            while pieces_choice != 5:
                pieces()
                pieces_choice = int(input('Option: '))
                if pieces_choice == 1:
                    pass
                elif pieces_choice == 2:
                    pass
                elif pieces_choice == 3:
                    pass
                elif pieces_choice == 4:
                    pass
                elif pieces_choice == 5:
                    menu()
                else:
                    print("")
                    print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   

        elif option == "3":
            exit_program()

        else:
            print("")
            print("\033[1mInvalid Option - Try typing a listed number option\033[0m")


def menu():
    print(Figlet(font='mini').renderText('Main Menu'))
    print("1. Students")
    print("")
    print("2. Pieces")
    print("")
    print("3. Exit the program")
    print('')


def exit_program():
    print('')
    print(Figlet(font='big').renderText('Goodbye'))
    print('')
    exit()


if __name__ == "__main__":
    greeting()
    main()