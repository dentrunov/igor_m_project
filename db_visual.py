from tkinter import *
import sqlite3
from bd_script import *


db_init()
current_day = -1
current_grade = -1

def class_selected():
    global current_grade

    current_grade = grades_list.curselection()[0]
    label_main['text'] = current_grade
    # Забираем данные из БД
    d = 0
    for dl in day_lists:
        dl.delete(0, END)
        les = get_lessons(current_grade, d)

        for l in les:
            #print(all_subjects[int(l[1])])
            dl.insert(END, all_subjects[int(l[1])-1])
        d += 1
        #выводим их в day_list


def day_selected():
    global current_day
    current_day = days_list.curselection()[0]
    label_main['text'] = current_day


def subject_selected():
    sel = subjects_list.curselection()
    if current_day >= 0 and sel:
        day_lists[current_day].insert(END, all_subjects[sel[0]])
    else:
        label_main['text'] = 'Не выбран класс или день недели'

def save_day(day):
    #сохранение дня недели
    #print(day_lists[day].get(0, END))
    db_save_day(current_day, current_grade, day_lists[day].get(0, END))


root = Tk()
root.geometry("1150x700")

label_grade = Label(root, width=20, bg='white', fg='black', text='Выберите класс')
grades_list = Listbox(root, width=20, height=8)
for g in all_grades():
    grades_list.insert(*g)

days = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}.items()
label_day = Label(root, width=20, bg='white', fg='black', text='Выберите день недели')
days_list = Listbox(root, width=20, height=8)
for d in days:
    days_list.insert(*d)

label_subjects = Label(root, width=20, bg='white', fg='black', text='Список предметов')
subjects_list = Listbox(root, width=20, height=20)

all_subjects = all_subj()
print(all_subjects)
for g in all_subjects:
    subjects_list.insert(*g)
subjects_button = Button(root, text='Выбрать', command=subject_selected).grid(row=5, column=0)


label_day1 = Label(root, width=20, bg='white', fg='black', text='Понедельник')
label_day2 = Label(root, width=20, bg='white', fg='black', text='Вторник')
label_day3 = Label(root, width=20, bg='white', fg='black', text='Среда')
label_day4 = Label(root, width=20, bg='white', fg='black', text='Четверг')
label_day5 = Label(root, width=20, bg='white', fg='black', text='Пятница')

day_lists = [Listbox(root, width=20, height=8) for i in range(5)]



day_list_buttons = [Button(root, text='Сохранить', command=lambda x=i: save_day(x)) for i in range(5)]

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
i = j = 3
for x in day_lists:
    x.grid(row=1, column=i)
    i += 1
for x in day_list_buttons:
    x.grid(row=2, column=j)
    j += 1


root.mainloop()

