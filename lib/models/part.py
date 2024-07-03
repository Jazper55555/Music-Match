from models.__init__ import CURSOR, CONN
from models.student import Student

class Part:

    all = {}
    
    def __init__(self, song, composer, instrument, student_id, id=None):
        
        self.id = id
        self.song = song
        self.composer = composer
        self.instrument = instrument
        self.student_id = student_id

    def __repr__(self) -> str:
        return (f'<Song: {self.song} by {self.composer} ' +
                f'Part: {self.instrument}>')
    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY,
            song TEXT,
            composer TEXT,
            instrument TEXT,
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id))'''
        
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS parts'''
        
        CURSOR.execute(sql)
        CONN.commit()