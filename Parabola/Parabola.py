from tkinter import * 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

def square():
    #Чтобы текста не накладывались друг на друга
    label1.configure(text='')
    D.configure(text='')
    A = int(a.get())
    B = int(b.get())
    C = int(c.get())
    Disc = B**2-4*A*C
    D.configure(text=f'Дискриминант: {Disc}')
    if Disc > 0:
        label1.configure(text=f'Корни уравнения:\nx1 = {-B+round(math.sqrt(Disc),2)/2*A}\nx2 = {-B-round(math.sqrt(Disc),2)/2*A}')
    elif Disc == 0:
        label1.configure(text=f'Дискриминант равен 0, по этому корни уравнения равны.\nx = {-B/2*A}')
    else:
        label1.configure(text='Дискриминант меньше 0, корней нет.')
    if chkvar.get() == 1:
        parabola(A,B,C)

def parabola(a,b,c):
    x = np.arange(-100,100)
    y=a*x**2 + b*x + c
    plt.plot(x,y)
    plt.show()

main = Tk()
mM = Menu(main)
main.config(menu=mM)
main.title('Решатель квадратного уравнения')
#mM.add_command(label='Файл')
#mM.add_command(label='Справка')

CanvasWidth = 250
CanvasHeight = 400

w = Canvas(main, width = CanvasWidth, height = CanvasHeight)
w.pack()

a = Entry(main)
w.create_window(CanvasWidth/2,150,window=a)
aLabel = Label(main,text='Впиши а')
w.create_window(CanvasWidth/2,130,window=aLabel)

b = Entry(main)
w.create_window(CanvasWidth/2,200,window=b)
bLabel = Label(main,text='Впиши b')
w.create_window(CanvasWidth/2,180,window=bLabel)

c = Entry(main)
w.create_window(CanvasWidth/2,250,window=c)
cLabel = Label(main,text='Впиши c')
w.create_window(CanvasWidth/2,230,window=cLabel)

button1 = Button(text='Решить',command=square)
w.create_window(CanvasWidth/2, 300, window=button1)

D = Label(main)
w.create_window(CanvasWidth/2,50,window=D)

label1 = Label(main)
w.create_window(CanvasWidth/2,80,window=label1)

chkvar = IntVar()
#радио кнопку сложно выключать, по этому легче использовать чек
#yes = Radiobutton(main,variable=var,value=True,text='Рисовать диаграмму',
#command=radio).pack(side=LEFT,expand=YES)
yes = Checkbutton(main, text='Рисовать диаграмму', 
var=chkvar, onvalue=True, offvalue=False).pack(side=LEFT,expand=YES)
#запаковывать можно на той же строчке, строчка ниже фигня
#yes.pack(side=LEFT,expand=YES)

main.mainloop()