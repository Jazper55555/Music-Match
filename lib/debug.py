#!/usr/bin/env python3
# lib/debug.py

from models.student import Student
from models.part import Part
import ipdb

luca = Student('Luca', 5)
snare = Part('Booty', 'Ludwig', 'Snare', 1)

ipdb.set_trace()
