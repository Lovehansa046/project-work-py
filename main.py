from tkinter import *
import csv
import datetime
clicks = 0
count = 0

def datetims():
    a = datetime.datetime.now()
    write_txt4(a)

def datatimes_start():
    a = datetime.datetime.now()
    write_txt6(a)

def write_txt(data):
    person = [
        ['Имя пользователя:',data],
        ['ответы на тест:',''],
    ]

    FILENAME = "users.csv"
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(person)

def write_txt2(data1):
    global count
    count += 1


    counti = [
        ['Номер вопроса',count, data1],
    ]

    FILENAME = "users.csv"
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(counti)

def write_txt3(data):
    person = [
        ['',''],
        ['Итог теста (заключение):',data],
    ]

    FILENAME = "users.csv"
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(person)

def write_txt4(data):
    person = [
        ['время окончания теста:',data],
        ['',''],
    ]

    FILENAME = "users.csv"
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(person)

def write_csv5(data):
    person = [
        ['кол-во ответов с да:',data,'/20'],
    ]

    FILENAME = "users.csv"
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(person)

def write_txt6(data):
    person = [
        ['время начала теста:', data],
    ]

    FILENAME = "users.csv"
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(person)

def click():

    text = entry.get()
    write_txt(text)

def click2():
    global clicks
    clicks += 1
    text = ( "да")
    write_txt2(text)

def click3():

    text = ("нет")
    write_txt2(text)



def window():
    global window1
    window1.destroy()
    window1 = Tk()
    window1.geometry("1920x1080")

    button_d = Button(window1, text='Переход к заключению опросника', background="khaki1", foreground="black", font="10", command=window2)
    button_d.place(x=580, y=720)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow", variable=lang, pady=10, padx=15, font="6",
                                     command=click2)
    config_checkbutton.place(x=30, y=70)

    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, padx=15, pady=10, font="6",
                                   command=click3)
    dont_checkbutton.place(x=90, y=70)

    header = Label(text="Как вы считаете удовлетворяте ли вас ваша жизнь? ", padx=15, font="6", pady=10)
    header.place(x=10, y=40)

    header = Label(text="Живы ли на данный момент ваши родители?", font="6", padx=15, pady=10)
    header.place(x=10, y=150)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow", variable=lang, pady=10, padx=15, font="6", command=click2)
    config_checkbutton.place(x=30, y=130)

    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, padx=15, pady=10, font="6", command=click3)
    dont_checkbutton.place(x=90, y=130)

    header = Label(text="Нравится ли вам ваша работа? ", padx=15, font="6", pady=10)
    header.place(x=10, y=100)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow", variable=lang, font="6", pady=10, padx=15, command=click2)
    config_checkbutton.place(x=30, y=190)

    dont_checkbutton = Radiobutton(text="-", value=2, bg="red",variable=lang, font="6", padx=15, pady=10, command=click3)
    dont_checkbutton.place(x=90, y=190)

    header = Label(text="Как вы считаете ваша работа достойно оплачивается?", padx=15, font="6", pady=10)
    header.place(x=10, y=160)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow", variable=lang, font="6", pady=10, padx=15, command=click2)
    config_checkbutton.place(x=30, y=250)

    dont_checkbutton = Radiobutton(text="-", value=2, bg="red",variable=lang, font="6", padx=15, pady=10, command=click3)
    dont_checkbutton.place(x=90, y=250)

    header = Label(text="Хотели бы вы сменить вашу работу, если была бы возможность?", padx=15, font="6", pady=10)
    header.place(x=10, y=220)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow", variable=lang, pady=10, font="6", padx=15, command=click2)
    config_checkbutton.place(x=30, y=310)

    dont_checkbutton = Radiobutton(text="-", value=2, bg="red",variable=lang, padx=15, font="6", pady=10, command=click3)
    dont_checkbutton.place(x=90, y=310)

    header = Label(text="Занимаетесь ли вы спортом?", padx=15, font="6", pady=10)
    header.place(x=10, y=280)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow", variable=lang, font="6", pady=10, padx=15, command=click2)
    config_checkbutton.place(x=30, y=370)

    dont_checkbutton = Radiobutton(text="-", value=2, bg="red",variable=lang, font="6", padx=15, pady=10, command=click3)
    dont_checkbutton.place(x=90, y=370)

    header = Label(text="Вы женаты/замужем?", padx=15, font="6", pady=10)
    header.place(x=10, y=340)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow", variable=lang, pady=10, font="6", padx=15, command=click2)
    config_checkbutton.place(x=30, y=430)

    dont_checkbutton = Radiobutton(text="-", value=2, bg="red",variable=lang, padx=15, font="6", pady=10, command=click3)
    dont_checkbutton.place(x=90, y=430)

    header = Label(text="У вас есть дети?", padx=15, font="6", pady=10)
    header.place(x=10, y=400)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, pady=10, font="6", padx=15, command=click2)
    config_checkbutton.place(x=30, y=490)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red",variable=lang, padx=15, pady=10, font="6", command=click3)
    dont_checkbutton.place(x=90, y=490)

    header = Label(text="Есть ли у вас цель в жизни к которой вы на данный момент стремитесь?", padx=15, font="6", pady=10)
    header.place(x=10, y=460)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, pady=10, padx=15, font="6", command=click2)
    config_checkbutton.place(x=30, y=550)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red",variable=lang, padx=15, pady=10, font="6", command=click3)
    dont_checkbutton.place(x=90, y=550)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, pady=10, padx=15, font="6", command=click2)
    config_checkbutton.place(x=30, y=610)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, padx=15, pady=10, font="6", command=click3)
    dont_checkbutton.place(x=90, y=610)
    header = Label(text="Можете ли вы себе позволить съездить на отдых хотя бы раз в год?", padx=15, font="6", pady=10)
    header.place(x=10, y=520)

    lang = IntVar()


    header = Label(text="Живы ли на данный момент ваши родители?​", padx=15, font="6", pady=10)
    header.place(x=10, y=580)

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, pady=10, padx=15, font="6", command=click2)
    config_checkbutton.place(x=820, y=70)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, padx=15, pady=10, font="6", command=click3)
    dont_checkbutton.place(x=880, y=70)
    header = Label(
        text="Есть ли люди в вашей жизни, \nкоторые могут вас поддержать при вашей неудаче или новых начинаниях?", font="6",
        padx=15, pady=10)
    header.place(x=800, y=20)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, pady=10, padx=15, font="6", command=click2)
    config_checkbutton.place(x=820, y=130)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, padx=15, pady=10, font="6", command=click3)
    dont_checkbutton.place(x=880, y=130)
    header = Label(text="Вы употребляете алкогольные напитки?", padx=15, font="6", pady=10)
    header.place(x=800, y=100)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow", variable=lang, font="6", pady=10, padx=15, command=click2)
    config_checkbutton.place(x=820, y=190)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, font="6", padx=15, pady=10, command=click3)
    dont_checkbutton.place(x=880, y=190)
    header = Label(text="Употребляли ли вы какие-либо запрещенные вещества?", padx=15, font="6", pady=10)
    header.place(x=800, y=160)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, pady=10, font="6", padx=15, command=click2)
    config_checkbutton.place(x=820, y=250)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, padx=15, font="6", pady=10, command=click3)
    dont_checkbutton.place(x=880, y=250)
    header = Label(text="Есть ли у вас какие-либо заболевания?", padx=15, font="6",pady=10 )
    header.place(x=800, y=220)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, pady=10, font="6",padx=15, command=click2)
    config_checkbutton.place(x=820, y=310)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, padx=15, font="6",pady=10, command=click3)
    dont_checkbutton.place(x=880, y=310)
    header = Label(text="Вы сильно религиозный человек?", padx=15, font="6",pady=10)
    header.place(x=800, y=280)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, font="6",pady=10, padx=15, command=click2)
    config_checkbutton.place(x=820, y=370)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, font="6",padx=15, pady=10, command=click3)
    dont_checkbutton.place(x=880, y=370)
    header = Label(text="Нарушали ли вы закон?", padx=15, font="6",pady=10)
    header.place(x=800, y=340)

    lang = IntVar()
    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, pady=10, font="6",padx=15, command=click2)
    config_checkbutton.place(x=820, y=430)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, padx=15, font="6",pady=10, command=click3)
    dont_checkbutton.place(x=880, y=430)
    header = Label(text="Вы удовлетворены своей сексуальной активностью?", font="6",padx=15, pady=10)
    header.place(x=800, y=400)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, font="6",pady=10, padx=15, command=click2)
    config_checkbutton.place(x=820, y=490)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, font="6",padx=15, pady=10, command=click3)
    dont_checkbutton.place(x=880, y=490)
    header = Label(text="У вас есть домашние животные?", padx=15, font="2",pady=10)
    header.place(x=800, y=460)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, font="2",pady=10, padx=15, command=click2)
    config_checkbutton.place(x=820, y=550)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, font="2",padx=15, pady=10, command=click3)
    dont_checkbutton.place(x=880, y=550)
    header = Label(text="Вы живете в Европе или Америке? (если в Европе '+', если в Америке '-')", padx=15, font="2",pady=10)
    header.place(x=800, y=520)

    lang = IntVar()

    config_checkbutton = Radiobutton(text="+", value=1, bg="greenyellow",variable=lang, font="2",pady=10, padx=15, command=click2)
    config_checkbutton.place(x=820, y=630)
    dont_checkbutton = Radiobutton(text="-", value=2, bg="red", variable=lang, font="2",padx=15, pady=10, command=click3)
    dont_checkbutton.place(x=880, y=630)
    header = Label(
        text="Часто ли вы позволяете себе раслабиться\n(например: сходить в кино,на концерт любимого исполнителя, в бар и тд.)?",
        padx=15, font="2",pady=10)
    header.place(x=800, y=580)

def window2():
    global window1
    global clicks
    window1.destroy()
    window1 = Tk()
    window1.geometry("600x400")
    window1.configure(bg="gray80")
    btn2 = Label(text="Кол-во ответов <<Да>>", background="springgreen", foreground="black", padx="20", pady="8", font="4")
    btn1 = Label(text=clicks, background="springgreen", foreground="black",padx="20", pady="8", font="4")
    if clicks <= 7:
        btn = Label(text="Вы крайне не довольны жизнью, \nстоит задуматься о том чтобы что-то начать менять",
                     background="lightblue1", foreground="black", padx="45", pady="40", font="6")
        btn.place(x=0, y=100)
        text2 = ("Вы крайне не довольны жизнью, стоит задуматься о том чтобы что-то начать менять")
        write_txt3(text2)
        write_csv5(clicks)

    elif clicks >= 8 and clicks <= 14:
        btn = Label(text="В вашей жизни есть как положительные,\nтак и отрицательные моменты \nвы еще можете сделать свою жизнь лучше",
                     background="lightblue1", foreground="black", padx="45", pady="40", font="6")
        btn.place(x=0, y=100)
        text2 = ("В вашей жизни есть как положительные, так и отрицательные моменты вы еще можете сделать свою жизнь лучше")
        write_txt3(text2)
        write_csv5(clicks)

    elif clicks >= 15 and clicks <= 20:
        btn = Label(text="Ваша жизнь очень насыщенная и благополучная,\n советуем вам ценить и беречь то что вы имеете",
                     background="lightblue1", foreground="black", padx="45", pady="40", font="6")
        btn.place(x=0, y=100)
        text2 = ("Ваша жизнь очень насыщенная и благополучная, советуем вам ценить и беречь то что вы имеете")
        write_txt3(text2)
        write_csv5(clicks)


    btn1.place(x=280, y=20)
    btn2.place(x=20, y=20)
    button_d = Button(window1, text='Выход', background="red", foreground="black", font=4, command=window1.destroy)
    button_d.place(x=500, y=250)

window1 = Tk()
entry = Entry(window1, width=20, bd=5)
entry.place(x=275, y=395)

def window54():
    window1.geometry("1000x1000")
    window1.configure(bg='moccasin')

    data = StringVar()
    data.set("Введите имя и фамилию:")

    label = Label(window1, textvariable=data, font = '8')
    label.place(x=20, y=390)

    button = Button(window1, text='Сохранить', background="darkolivegreen1", foreground="black", font='8', command=click)
    button.place(x=20, y=430)

    button_d = Button(window1, text='Перейти к опроснику', background="khaki1", foreground="black", font='12', command=window)
    button_d.place(x=750, y=380)



    label=Label(window1, text="\n\n\nПриветствуем вас в нашем опроснике на тему Удовлетворенность жизнью.\n\nОпросник состоит из 20-то вопросов на которые вам нужно ответить Да или Нет.\n\nОпросник предназначен для лиц старше 21 года.\n\nПосле прохождения опросника вы получите результат, который будет зависить от ваших ответов.\n\n Если вы готовы пройти опросник то введите свои имя и фамилию нажмите сохранить и перейти к опроснику.\n\n\n", font='Times 16', fg='Black',bg='LightSteelBlue1')
    label.place(x=10, y=20)

    window1.mainloop()

datatimes_start()
window54()
datetims()