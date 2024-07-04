from models.__init__ import CURSOR, CONN
# from models.student import Student

class Piece:

    all = {}
    
    def __init__(self, piece, composer, instrument, student_id, id=None):
        
        self.id = id
        self.piece = piece
        self.composer = composer
        self.instrument = instrument
        self.student_id = student_id

    def __repr__(self) -> str:
        return (f'<Piece: {self.piece} by {self.composer}; ' +
                f'Part: {self.instrument}>')
    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pieces (
            id INTEGER PRIMARY KEY,
            piece TEXT,
            composer TEXT,
            instrument TEXT,
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id))'''
        
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS pieces'''
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, piece, composer, instrument, student_id):
        piece = cls(piece, composer, instrument, student_id)
        piece.save()
        return piece
    
    def save(self):
        sql = '''
            INSERT INTO pieces (piece, composer, instrument, student_id)
            VALUES (?, ?, ?, ?)'''
        
        CURSOR.execute(sql, (self.piece, self.composer, self.instrument, self.student_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = '''
            UPDATE pieces
            SET piece = ?, composer = ?, instrument = ?, student_id = ?
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.piece, self.composer, self.instrument, self.student_id, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM pieces
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        piece = cls.all.get(row[0])
        if piece:
            piece.piece = row[1]
            piece.composer = row[2]
            piece.instrument = row[3]
            piece.student_id = row[4]
        else:
            piece = cls(row[1], row[2], row[3], row[4])
            piece.id = row[0]
            cls.all[piece.id] = piece

        return piece
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT *
            FROM pieces'''
        
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT *
            FROM pieces
            WHERE id = ?'''
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_instrument(cls, instrument):
        sql = '''
            SELECT *
            FROM pieces
            WHERE instrument is ?'''
        
        rows = CURSOR.execute(sql, (instrument,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_piece(cls, piece):
        sql = '''
            SELECT *
            FROM pieces
            WHERE piece is ?'''
        
        rows = CURSOR.execute(sql, (piece,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_composer(cls, composer):
        sql = '''
            SELECT *
            FROM pieces
            WHERE composer is ?'''
        
        rows = CURSOR.execute(sql, (composer,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
