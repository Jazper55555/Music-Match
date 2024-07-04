#!/usr/bin/env python3
# lib/debug.py

from models.student import Student
from models.piece import Piece

def reset_data():
    Student.drop_table()
    Student.create_table()
    Piece.drop_table()
    Piece.create_table()

reset_data()

luca = Student.create('Luca', 'Saldana', 6)
andrea = Student.create('Andrea', 'Saldana', 12)
jazz = Student.create('Jazz', 'Man', 10)
johnny = Student.create('Johnny', 'Naw', 9)
nick = Student.create('Nick', 'Manyloun', 11)

Piece.create('Sea Shanty', 'Pirates', 'Bass Drum', nick.id)
Piece.create('Sea Shanty', 'Pirates', 'Snare', johnny.id)
Piece.create('Sea Shanty', 'Pirates', 'Flute', andrea.id)
Piece.create('Sea Shanty', 'Pirates', 'Foot Stomps', jazz.id)
Piece.create('Sea Shanty', 'Pirates', 'Yelling', luca.id)
Piece.create('Hallelujah', 'Leonard Cohen', 'Soprano', luca.id)
Piece.create('Hallelujah', 'Leonard Cohen', 'Alto', andrea.id)
Piece.create('Hallelujah', 'Leonard Cohen', 'Tenor', johnny.id)
Piece.create('Hallelujah', 'Leonard Cohen', 'Bass', nick.id)
Piece.create('Blackbird', 'The Beatles', 'Bass Drum', jazz.id)

breakpoint()