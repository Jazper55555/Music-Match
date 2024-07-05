# lib/parts_cli.py
from models.piece import Piece
from models.student import Student
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
    print('')
    all_pieces = Piece.get_all()
    for piece in all_pieces:
        print('')
        print(f"\033[1m{piece}\033[0m")
    
    pieces_menu()


def update_piece():
    print('')
    print('Choose from the following pieces:')
    print('')
    pieces_list = Piece.get_all()
    for i, piece in enumerate(pieces_list, start=1):
        print(f'{i}. {piece}')
    
    print('')
    piece_id = int(input("Enter the piece id: "))
    print('')
    chosen_piece = Piece.find_by_id(piece_id)
    print(f"\033[1m{chosen_piece}\033[0m")   
    print('')
    update_title = input('Enter the pieces updated title: ')
    update_composer = input('Enter the pieces updated composer: ')

    print('')
    chosen_piece.title = update_title
    chosen_piece.composer = update_composer
    chosen_piece.update()

    try:
        print('')
        print(f"\033[1mSuccessfully updated {chosen_piece}\033[0m")   
    except Exception as exc:
        print('Error updating piece: ', exc)

    pieces_menu()


def add_piece():
    print('')
    new_title = input("Enter the new piece's title: ")
    new_composer = input("Enter the new piece's composer: ")
    print('')
    new_piece = Piece.create(new_title, new_composer)
    try:
        print('')
        print(f"\033[1mSuccessfully created new {new_piece}\033[0m")   
    except Exception as exc:
        print('Error creating piece: ', exc)

    pieces_menu()


def delete_piece():
    print('')
    print('Select from the following:')
    print('')
    pieces_list = Piece.get_all()
    for i, piece in enumerate(pieces_list, start=1):
            print(f'{i}. {piece}')
    
    print('')
    id_ = input('Enter the piece id: ')
    if piece := Piece.find_by_id(id_):
        piece.delete()
        print('')
        print(f"\033[1mPiece {piece.title} successfully deleted\033[0m")   
    else:
        print('')
        print("\033[1mInvalid Option - Try typing a listed number option\033[0m")   

    pieces_menu()