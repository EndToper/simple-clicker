from tkinter import *
import time
number = 0

window = Tk()

window.geometry('500x500')
point = 1
cost = 10
cost1=cost
point2 = 0
cost2 = 500
cost3 = cost2
cost4 = 10000
cost5 = cost4
time = 2500
m= 0
def hello():
    global number
    number += point
    label_count['text'] = +int(number)

    #label_count.config(text = str(number))

def up():
    global number,cost,point
    if int(number) >= cost:
        point = point + 1
        number = number - cost
        for i in range(point):
            cost = cost + cost1*i
        label_2['text']=f'Цена улучшения: {cost}'
        label_3['text']=f'множитель улучшения: {point}'
        label_count['text'] = +int(number)


def up2():
    global number,cost2,point2
    if int(number) >= cost2:
        point2 = point2 + 5
        number = number - cost2
        print(round(point2/5))
        for i in range(round(point2/5)):
            cost2 = cost2 + cost3*i
        label_4['text']=f'Цена улучшения: {cost2}'
        label_5['text']=f'множитель улучшения: {point2}'
        label_count['text'] = +int(number)
        if m == 0:
            afk_click()

def afk_click():
    global number,point2,time,m
    m = 1
    number += point2
    label_count['text'] = +int(number)
    window.after(time, afk_click)
    


def up3():
    global number,cost4,time
    if int(number) >= cost4:
        if time > 100:
            time = time - 100
            number = number - cost4
            cost4 = round(cost4*cost4/cost5)
            if cost4 == cost5:
                cost4 = cost4*1.25
            label_6['text']=f'Цена улучшения: {cost4}'
            label_7['text']=f'время одного клика афк кликера: {time/1000} секунд'
            label_count['text'] = +int(number)
        if time == 100:
            label_6['text']=f'Куплено максимальное улучшение'


button = Button(window,
                text = 'Клик',
                command = hello)

button_lvl = Button(window,
                text = f"Купить улучшение",
                command = up)

button_lvl_2 = Button(window,
                text = f"Купить улучшение афк кликера",
                command = up2)

button_lvl_3 = Button(window,
                text = f"ускорить афк кликер",
                command = up3)

label = Label(text='Ваш счет')
label_2 = Label(text=f'Цена улучшения: {cost}')
label_3 = Label(text=f'множитель улучшения: {point}')

label_4 = Label(text=f'Цена улучшения афк кликера: {cost2}')
label_5 = Label(text=f'множитель улучшения: {point2}')

label_6=Label(text=f'Цена улучшения: {cost4}')
label_7=Label(text=f'время одного клика афк кликера: {time/1000} секунд')

label_count = Label(text=+int(number))

#размещение объектов на экране
label.pack()
label_count.pack()
button.pack()
label_2.pack()
label_3.pack()
button_lvl.pack()
label_4.pack()
label_5.pack()
button_lvl_2.pack()
#добавление коорщдинат объектам
button.place(x = 225, y = 100)
button_lvl.place(x = 50, y = 250)
button_lvl_2.place(x = 250, y = 250)
button_lvl_3.place(x = 150, y = 350)

label.place(x = 200, y = 140)
label_count.place(x = 275, y = 140)

label_2.place(x = 35, y = 280)
label_3.place(x = 25, y = 310)

label_4.place(x = 250, y = 280)
label_5.place(x = 255, y = 310)

label_6.place(x = 150, y = 380)
label_7.place(x = 115, y = 410)
#основной
afk_click()

window.mainloop()