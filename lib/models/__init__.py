import sqlite3

CONN = sqlite3.connect('music_assignments.db')
CURSOR = CONN.cursor()
