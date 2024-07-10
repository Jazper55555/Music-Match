# lib/parts_cli.py
from models.piece import Piece
from pyfiglet import Figlet


def pieces_menu():
    print('')
    print(Figlet(font='mini').renderText('Pieces'))
    print("1. View all pieces")
    print("")
    print("2. Update a piece")
    print("")
    print("3. Add a piece")
    print("")
    print("4. Delete a piece")
    print("")
    print('5. Go back to Main Menu')
    print("")


def view_pieces():
    all_pieces = Piece.get_all()
    for piece in all_pieces:
        print('')
        print(f"\033[1m{piece.title} by {piece.composer}\033[0m")
    

def update_piece():
    try:
        print('')
        print('Choose from the following pieces:')
        print('')
        pieces_list = Piece.get_all()
        for i, piece in enumerate(pieces_list, start=1):
            print(f'{i}. {piece}')
        
        print('')
        print('0. Go back to Pieces Menu')
        
        print('')
        choice = int(input("Enter the piece number: "))
        if choice == 0:
            return
        if choice > len(pieces_list):
            raise ValueError
        print('')
        chosen_piece = pieces_list[choice - 1]

        try:
            update_title = input('Enter the pieces updated title: ')
            update_composer = input('Enter the pieces updated composer: ')

            chosen_piece.title = update_title
            chosen_piece.composer = update_composer

            chosen_piece.update()

            print('')
            print(f"\033[1mSuccessfully updated {chosen_piece}\033[0m")   
        except Exception as exc:
            print('')
            print(f"\033[1mError updating piece:\033[0m", exc)   

    except ValueError:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")
        update_piece()    


def add_piece():
    try:
        print('')
        new_title = input("Enter the new piece's title: ")
        new_composer = input("Enter the new piece's composer: ")
        print('')

        new_piece = Piece.create(new_title, new_composer)

        print('')
        print(f"\033[1mSuccessfully created new {new_piece}\033[0m")   
    except Exception as exc:
        print('')
        print(f"\033[1mError creating piece:\033[0m", exc)


def delete_piece():
    try:
        print('')
        print('Select from the following pieces to delete:')
        print('')
        pieces_list = Piece.get_all()
        for i, piece in enumerate(pieces_list, start=1):
                print(f'{i}. {piece}')

        print('')
        print('0. Go back to Pieces Menu')

        print('')
        choice = input('Enter the piece number: ')
        
        if int(choice) == 0:
            return
        if int(choice) > len(pieces_list):
            raise ValueError
        
        chosen_piece = pieces_list[int(choice) - 1]
        chosen_piece.delete()

        print('')
        print(f"\033[1mSuccessfully deleted {chosen_piece}\033[0m")   
    
    except ValueError:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")
        delete_piece()

    # print('')
    # print('0. Go back to Pieces Menu')
    
    # print('')
    # choice = input('Enter the piece number: ')
    # if int(choice) == '0' or choice == '':
    #     delete_piece()
    # if int(choice) > len(pieces_list):
    #     raise ValueError
    # try:
    #     # piece_id = int(id_)
    #     # chosen_piece = Piece.find_by_id(piece_id)
    #     chosen_piece = pieces_list[int(choice) - 1]
    #     chosen_piece.delete()
    #     print('')
    #     print(f"\033[1mPiece: {chosen_piece.title} by {chosen_piece.composer} successfully deleted\033[0m")
    # except ValueError:
    #     print('')
    #     print("\033[1mInvalid Option - Try typing a listed number option\033[0m")
    #     delete_piece() 