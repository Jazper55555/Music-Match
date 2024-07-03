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

    @classmethod
    def create(cls, song, composer, instrument, student_id):
        part = cls(song, composer, instrument, student_id)
        part.save()
        return part
    
    def save(self):
        sql = '''
            INSERT INTO parts (song, composer, instrument, student_id)
            VALUES (?, ?, ?, ?)'''
        
        CURSOR.execute(sql, (self.song, self.composer, self.instrument, self.student_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = '''
            UPDATE parts
            SET song = ?, composer = ?, instrument = ?, student_id = ?
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.song, self.composer, self.instrument, self.student_id, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM parts
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        part = cls.all.get(row[0])
        if part:
            part.song = row[1]
            part.composer = row[2]
            part.instrument = row[3]
            part.student_id = row[4]
        else:
            part = cls(row[1], row[2], row[3], row[4])
            part.id = row[0]
            cls.all[part.id] = part

        return part
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT *
            FROM parts'''
        
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT *
            FROM parts
            WHERE id = ?'''
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_instrument(cls, instrument):
        sql = '''
            SELECT *
            FROM parts
            WHERE instrument is ?'''
        
        row = CURSOR.execute(sql, (instrument,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    