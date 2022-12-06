from tkinter import *
import sqlite3

conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()


def class_selected():
    global current_grade
    current_grade = grades_list.curselection()
    label_main['text'] = current_grade


def day_selected():
    global current_day
    current_day = days_list.curselection()[0]
    label_main['text'] = current_day


def subject_selected():
    sel = subjects_list.curselection()
    day_lists[current_day].insert(END, all_subjects[sel[0]])


root = Tk()
root.geometry("1100x600")

label_grade = Label(root, width=20, bg='white', fg='black', text='Выберите класс')
grades_list = Listbox(root, width=20, height=8)
cursor.execute('SELECT * FROM grades')
for g in cursor.fetchall():
    grades_list.insert(*g)

days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}.items()
label_day = Label(root, width=20, bg='white', fg='black', text='Выберите день недели')
days_list = Listbox(root, width=20, height=8)
for d in days:
    days_list.insert(*d)

label_subjects = Label(root, width=20, bg='white', fg='black', text='Список предметов')
subjects_list = Listbox(root, width=20, height=20)
cursor.execute('SELECT * FROM subjects')
all_subjects = cursor.fetchall()
for g in all_subjects:
    subjects_list.insert(*g)
subjects_button = Button(root, text='Выбрать', command=subject_selected).grid(row=5, column=0)


label_day1 = Label(root, width=20, bg='white', fg='black', text='Понедельник')
label_day2 = Label(root, width=20, bg='white', fg='black', text='Вторник')
label_day3 = Label(root, width=20, bg='white', fg='black', text='Среда')
label_day4 = Label(root, width=20, bg='white', fg='black', text='Четверг')
label_day5 = Label(root, width=20, bg='white', fg='black', text='Пятница')
day_lists = [Listbox(root, width=20, height=8) for i in range(5)]


but_grade = Button(root, text='Выбрать класс', command=class_selected)
but_day = Button(root, text='Выбрать день', command=day_selected)
label_main = Label(root, width=20, bg='white', fg='black', text='Привет')


label_grade.grid(row=0, column=0)
grades_list.grid(row=1, column=0)
but_grade.grid(row=2, column=0)
label_day.grid(row=0, column=1)
days_list.grid(row=1, column=1)
but_day.grid(row=2, column=1)
label_subjects.grid(row=3, column=0)
subjects_list.grid(row=4, column=0)
label_day1.grid(row=0, column=3)
label_day2.grid(row=0, column=4)
label_day3.grid(row=0, column=5)
label_day4.grid(row=0, column=6)
label_day5.grid(row=0, column=7)
label_main.grid(row=3, column=1)
i = 3
for x in day_lists:
    x.grid(row=1, column=i)
    i += 1


root.mainloop()

