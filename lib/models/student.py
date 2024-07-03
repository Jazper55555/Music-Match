from models.__init__ import CURSOR, CONN
# from models.part import Part

class Student:

    all = {}

    def __init__(self, name, grade, id=None):
        
        self.id = id
        self.name = name
        self.grade = grade

    def __repr__(self) -> str:
        return (f'<Student: {self.name}, Grade: {self.grade}>')
    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade INTEGER)'''
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE IF EXISTS students'''
        
        CURSOR.execute(sql)
        CONN.commit()