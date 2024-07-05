from models.__init__ import CURSOR, CONN
# from models.student import Student
# from models.part import Part

class Piece:

    all = {}
    
    def __init__(self, title, composer, id=None):
        
        self.id = id
        self.title = title
        self.composer = composer

    def __repr__(self) -> str:
        return (f'Piece: {self.title} by {self.composer}')    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS pieces (
            id INTEGER PRIMARY KEY,
            title TEXT,
            composer TEXT)'''
                
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS pieces'''
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, title, composer):
        piece = cls(title, composer)
        piece.save()
        return piece
    
    def save(self):
        sql = '''
            INSERT INTO pieces (title, composer)
            VALUES (?, ?)'''
        
        CURSOR.execute(sql, (self.title, self.composer))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = '''
            UPDATE pieces
            SET title = ?, composer = ?
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.title, self.composer, self.id))
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
            piece.title = row[1]
            piece.composer = row[2]
        else:
            piece = cls(row[1], row[2])
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
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_piece(cls, title):
        sql = '''
            SELECT *
            FROM pieces
            WHERE title is ?'''
        
        rows = CURSOR.execute(sql, (title,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_composer(cls, composer):
        sql = '''
            SELECT *
            FROM pieces
            WHERE composer is ?'''
        
        rows = CURSOR.execute(sql, (composer,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
