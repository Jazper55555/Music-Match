from __init__ import CURSOR, CONN
# from student import Student

class Part:

    all = {}
    
    def __init__(self, song, composer, instrument, student_id, id=None):
        
        self.id = id
        self.song = song
        self.composer = composer
        self.instrument = instrument
        self.student_id = student_id

    def __repr__(self) -> str:
        return (f'<Song: {self.song} by {self.composer}' +
                f'Part: {self.instrument}>')
    