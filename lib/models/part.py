from models.__init__ import CURSOR, CONN

class Part:

    all = {}
    
    def __init__(self, instrument, student_id, piece_id, id=None):
        
        self.id = id
        self.instrument = instrument
        self.student_id = student_id
        self.piece_id = piece_id
        if self.id is not None:
            self.all[self.id] = self

    def __repr__(self) -> str:
        return (f'<Instrument: {self.instrument}; student_id: {self.student_id}; piece_id: {self.piece_id}>')
    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS parts (
            id INTEGER PRIMARY KEY,
            instrument TEXT,
            student_id INTEGER,
            piece_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (piece_id) REFERENCES pieces(id))'''
        
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS parts'''
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, instrument, student_id, piece_id):
        part = cls(instrument, student_id, piece_id)
        part.save()
        return part
    
    def save(self):
        sql = '''
            INSERT INTO parts (instrument, student_id, piece_id)
            VALUES (?, ?, ?)'''
        
        CURSOR.execute(sql, (self.instrument, self.student_id, self.piece_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = '''
            UPDATE parts
            SET instrument = ?, student_id = ?, piece_id = ?
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.instrument, self.student_id, self.piece_id, self.id))
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
            part.instrument = row[1]
            part.student_id = row[2]
            part.piece_id = row[3]
        else:
            part = cls(row[1], row[2], row[3])
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
        return cls.instance_from_db(row) if row else None

    @classmethod
    def student_parts(cls, student_id):
        sql = '''
            SELECT *
            FROM parts
            WHERE student_id = ?'''
        
        rows = CURSOR.execute(sql, (student_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_student_and_piece_id(cls, student_id, piece_id):
        sql = '''
            SELECT *
            FROM parts
            WHERE student_id = ? and piece_id = ?'''
        
        row = CURSOR.execute(sql, (student_id, piece_id)).fetchone()
        return cls.instance_from_db(row) if row else None