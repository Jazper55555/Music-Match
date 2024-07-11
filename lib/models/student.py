from models.__init__ import CURSOR, CONN

class Student:

    all = {}

    def __init__(self, first_name, last_name, grade, id=None):
        
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def __repr__(self) -> str:
        return (f'<Student: {self.first_name} {self.last_name}, Grade: {self.grade}>')

    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        first_name = first_name.strip()
        if isinstance(first_name, str) and len(first_name) > 0:
            self._first_name = first_name
        else:
            raise Exception(f"\033[1mFirst name must be text with at least 1 character\033[0m")
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        last_name = last_name.strip()
        if isinstance(last_name, str) and len(last_name) > 0:
            self._last_name = last_name
        else:
            raise Exception(f"\033[1mLast name must be text with at least 1 character\033[0m")
        
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        if isinstance(grade, int) and 6<= grade <= 12:
            self._grade = grade
        else:
            raise Exception(f"\033[1mGrade must be a number between 6 and 12\033[0m")
    

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
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
    def create(cls, first_name, last_name, grade):
        student = cls(first_name, last_name, grade)
        student.save()
        return student
    
    def save(self):
        sql = '''
            INSERT INTO students (first_name, last_name, grade)
            VALUES (?, ?, ?)'''
        
        CURSOR.execute(sql, (self.first_name, self.last_name, self.grade))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = '''
            UPDATE students
            SET first_name = ?, last_name = ?, grade = ?
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.first_name, self.last_name, self.grade, self.id))
        CONN.commit()

    def delete(self):
        sql = '''
            DELETE FROM students
            WHERE id = ?'''
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        sql_update = '''
        UPDATE parts
        SET student_id = NULL
        WHERE student_id = ?'''

        CURSOR.execute(sql_update, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        student = cls.all.get(row[0])
        if student:
            student.first_name = row[1]
            student.last_name = row [2]
            student.grade = row[3]
        else:
            student = cls(row[1], row[2], row[3])
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
    
    @classmethod
    def find_by_id(cls, id):
        sql = '''
            SELECT *
            FROM students
            WHERE id = ?'''
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def parts(self):
        from models.part import Part
        sql = '''
            SELECT *
            FROM parts
            WHERE student_id = ?'''
        
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Part.instance_from_db(row) for row in rows]
    