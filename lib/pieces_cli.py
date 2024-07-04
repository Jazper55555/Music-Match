# lib/parts_cli.py
from models.piece import Piece
from pyfiglet import Figlet

def pieces():
    print("")
    print(Figlet(font='mini').renderText('Pieces'))
    print("1. View all pieces")
    print("")
    print("2. Add a piece")
    print("")
    print("3. Update a piece")
    print("")
    print("4. Delete a piece")
    print("")
    print('5. Go back to Main Menu')
    print("")

