#!/usr/bin/env python3
# lib/debug.py

from models.student import Student
from models.part import Part
import ipdb

def reset_data():
    Student.drop_table()
    Student.create_table()
    Part.drop_table()
    Part.create_table()

    luca = Student.create('Luca', 6)
    andrea = Student.create('Andrea', 12)
    jazz = Student.create('Jazz', 10)
    johnny = Student.create('Johnny', 9)
    nick = Student.create('Nick', 11)

    Part.create('Sea Shanty', 'Pirates', 'Bass Drum', nick.id)
    Part.create('Sea Shanty', 'Pirates', 'Snare', johnny.id)
    Part.create('Sea Shanty', 'Pirates', 'Flute', andrea.id)
    Part.create('Sea Shanty', 'Pirates', 'Foot Stomps', jazz.id)
    Part.create('Sea Shanty', 'Pirates', 'Yelling', luca.id)
    Part.create('Hallelujah', 'Leonard Cohen', 'Soprano', luca.id)
    Part.create('Hallelujah', 'Leonard Cohen', 'Alto', andrea.id)
    Part.create('Hallelujah', 'Leonard Cohen', 'Tenor', johnny.id)
    Part.create('Hallelujah', 'Leonard Cohen', 'Bass', nick.id)
    Part.create('Blackbird', 'The Beatles', 'Bass Drum', jazz.id)

    breakpoint()

reset_data()
ipdb.set_trace()