#!/usr/bin/env python3
# lib/debug.py
from models.student import Student
from models.piece import Piece
from models.part import Part


def reset_data():
    Student.drop_table()
    Student.create_table()
    Piece.drop_table()
    Piece.create_table()
    Part.drop_table()
    Part.create_table()

reset_data()

# seed data for database
luca = Student.create('Luca', 'Saldana', 6)
andrea = Student.create('Andrea', 'Saldana', 12)
jazz = Student.create('Jazz', 'Man', 10)
johnny = Student.create('Johnny', 'Naw', 9)
nick = Student.create('Nick', 'Manyloun', 11)

sea_shanty = Piece.create('Sea Shanty', 'Pirates')
hallelujah = Piece.create('Hallelujah', 'Leonard Cohen')
blackbird = Piece.create('Blackbird', 'The Beatles')

ss_bd = Part.create('Bass Drum', jazz.id, sea_shanty.id)
ss_fs = Part.create('Foot Stomps', nick.id, sea_shanty.id)
ss_vocals = Part.create('Vocals', luca.id, sea_shanty.id)
hl_sop = Part.create('Soprano', johnny.id, hallelujah.id)
hl_alto = Part.create('Alto', andrea.id, hallelujah.id)
hl_tenor = Part.create('Tenor', jazz.id, hallelujah.id)
hl_bass = Part.create('Bass', nick.id, hallelujah.id)
bb_gt = Part.create('Guitar', jazz.id, blackbird.id)
bb_gt2 = Part.create('Backup Guitar', andrea.id, blackbird.id)
bb_bass = Part.create('Bass Guitar', johnny.id, blackbird.id)
bb_drums = Part.create('Drums', luca.id, blackbird.id)

breakpoint()