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

    @classmethod
    def create(cls, name, grade):
        student = cls(name, grade)
        student.save()
        return student
    
    def save(self):
        sql = '''
            INSERT INTO students (name, grade)
            VALUES (?, ?)'''
        
        CURSOR.execute(sql, (self.name, self.grade))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = '''
            UPDATE students
            SET name = ?, grade = ?
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.name, self.grade, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM students
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        student = cls.all.get(row[0])
        if student:
            student.name = row[1]
            student.grade = row[2]
        else:
            student = cls(row[1], row[2])
            student.id = row[0]
            cls.all[student.id] = student

        return student
    
    @classmethod
    def get_all(cls):
        sql = '''
            SELECT *
            FROM students'''
        
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]