from tkinter import *
from tkinter import messagebox
import random

Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
Low = 'qwertyuiopasdfghjklzxcvbnm'
Num = '1234567890'
Sig = '!@#$%^&*()_+=-'

Bi = True #юзать или нет
Lo = True
Nu = True
Si = True



#Показывает сгенерированный пароль

#окно
prog = Tk()
prog.title('Генератор пароля V.1.0')
prog.geometry('500x400')
#кнопка
#btn = Button(text = 'Сгенерировать пароль', font = ('Impact', 15), command = show)
#btn.place(x = '160', y = '250')

#количество символов
nums = StringVar()#nums - это строка, которая может меняться
num_l = Label(prog, text = 'Введите количество символов в пароле: ', font = ('Impact', 15))
num_l.place(x = '10', y = '10')
num_entry = Entry(textvariable = nums)
num_entry.place(x = '370', y = '18')



#количество паролей
ams = StringVar()#ams - это строка, которая модет меняться
ams_l = Label(prog, text  = 'Введите количество паролей: ', font = ('Impact', 15))
ams_l.place(x = '104', y = '60')
ams = Entry(textvariable = ams)
ams.place(x = '370', y = '67')

PassLen = 0

def analis():
    global PassLen
    if not ams:
        print('Error')
    else:
        val = ams.get()#_______________________ ИДИИОТСКАЯ ПОЧЕМУ ТЫ НЕ ВИДИШЬ ЕЕ ДЕБИЛ
        PassLen = int(val)

PassSymb = []

if Bi == True:
    PassSymb.extend(list(Big))
if Lo == True:
    PassSymb.extend(list(Low))
if Nu == True:
    PassSymb.extend(list(Num))
if Si == True:
    PassSymb.extend(list(Sig))

Password = []


Password.append(''. join([random.choice(PassSymb) for x in range(int(PassLen))]))

a = str(Password)

def show():
    messagebox.showinfo('Генератор пароля V.1.0', a)


btn = Button(text = 'Сгенерировать пароль', font = ('Impact', 15), command = show)
btn.place(x = '160', y = '250')
#
prog.mainloop()