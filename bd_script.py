import sqlite3

conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()
create_table_1 = '''CREATE TABLE IF NOT EXISTS raspisanie 
                    (id INTEGER PRIMARY KEY,
                    subject TEXT NOT NULL,
                    weekday TEXT NOT NULL,
                    time DATETIME NOT NULL,
                    grade TEXT NOT NULL);'''
cursor.execute(create_table_1)
conn.commit()
create_table_2 = '''CREATE TABLE IF NOT EXISTS subjects 
                    (subject_id INTEGER PRIMARY KEY,
                    subject_name TEXT NOT NULL);'''
cursor.execute(create_table_2)
conn.commit()
create_table_3 = '''CREATE TABLE IF NOT EXISTS grades
                    (grade_id INTEGER PRIMARY KEY,
                    grade_name TEXT NOT NULL);'''
cursor.execute(create_table_3)
conn.commit()

days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}

'''grades_1 = [str(i)+j for i in (10,11) for j in 'АБВГ']
data = ((i, grades_1[i]) for i in range(len(grades_1)))

cursor.executemany('INSERT INTO grades (grade_id, grade_name) VALUES (?, ?);', data)
conn.commit()'''
subj = {1: "Математика", 2: "Физика", 3: "Русский язык",
        4: "Литература", 5: "История", 6: "География",
        7: "Физкультура", 8: "ОБЖ", 9: "Обществознание",
        10: "Химия", 11: "Музыка", 12: 'Информатика',
        13: 'Биология', 14: 'Экономика', 15: 'Право'}
lesson = (subj.items())

cursor.executemany('INSERT INTO subjects (subject_id, subject_name) VALUES (?, ?);', lesson)
conn.commit()

query_1 = '''SELECT * FROM subjects'''
cursor.execute(query_1)
for g in cursor.fetchall():
    print(g)


#создать список предметов
#создать список кортежей (id, предмет)
#заполнить БД предметов методом cursor.executemany

cursor.close()
conn.close()