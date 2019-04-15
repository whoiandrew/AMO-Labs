from tkinter import *
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from interp import lagr
import numpy as np
from tkinter import messagebox


def sin_window(n):
    try:
        n = int(n) - 1
    except ValueError:
        messagebox.showwarning("Увага!", "Введіть ціле число!")
    x = [round((2/n) * i, 4) for i in range(n+1)]
    x1 = [x / 10 for x in range(0, 21)]
    print(x1)
    print(len(x1))
    y1 = [math.sin(i) for i in x]
    y_x1 = [math.sin(i) for i in x1]

    top = Toplevel(root)
    top.geometry("500x600")

    fig1 = Figure(figsize=(6, 3))
    a1 = fig1.add_subplot(111)
    a1.plot([i for i in np.arange(0, 2.1, 0.1)], [math.sin(i) for i in np.arange(0, 2.1, 0.1)], color='green')
    a1.set_title("Sin(x) plot", fontsize=16)
    canvas = FigureCanvasTkAgg(fig1, master=top)
    canvas.get_tk_widget().pack()
    canvas.draw()

    fig2 = Figure(figsize=(6, 3))
    a2 = fig2.add_subplot(111)
    a2.scatter(x, y1, color='red')
    a2.plot(x1, [lagr(x, y1, i) for i in x1], color='blue')
    a2.set_title("Sin(x) interpolated function", fontsize=16)
    canvas = FigureCanvasTkAgg(fig2, master=top)
    canvas.get_tk_widget().pack()
    canvas.draw()


def var_window(n):
    try:
        n = int(n) - 1
    except ValueError:
        messagebox.showwarning("Увага!", "Введіть ціле число!")
        exit()
    x = [round((2/n) * i, 4) for i in range(n+1)]
    x2 = [x / 10 for x in range(0, 21)]
    y2 = [math.cos(i + pow(math.cos(i), 3)) for i in x]
    y_x2 = [math.cos(i + pow(math.cos(i), 3)) for i in x2]
    top = Toplevel(root)
    top.geometry("500x600")

    fig1 = Figure(figsize=(6, 3))
    a1 = fig1.add_subplot(111)
    a1.plot([i for i in np.arange(0, 2.1, 0.1)], [math.cos(i + math.cos(i)**3) for i in np.arange(0, 2.1, 0.1)], color='green')
    a1.set_title("cos(x + cos(x)^3) plot", fontsize=16)
    canvas = FigureCanvasTkAgg(fig1, master=top)
    canvas.get_tk_widget().pack()
    canvas.draw()

    fig2 = Figure(figsize=(6, 3))
    a2 = fig2.add_subplot(111)
    a2.scatter(x, y2, color='red')
    a2.plot(x2, [lagr(x, y2, i) for i in x2], color='blue')
    a2.set_title("cos(x + cos(x)^3) interpolated", fontsize=16)
    canvas = FigureCanvasTkAgg(fig2, master=top)
    canvas.get_tk_widget().pack()
    canvas.draw()


def fault_window(n):
    try:
        n = int(n) - 1
    except ValueError:
        messagebox.showwarning("Увага!", "Введіть ціле число!")
        exit()
    x = [round((2/n) * i, 4) for i in range(n+1)]
    x2 = [round((2 / n) * i, 4) for i in np.arange(0, 2.1, 0.1)]
    y2 = [math.cos(i + pow(math.cos(i), 3)) for i in x]
    y_x2 = [math.cos(i + pow(math.cos(i), 3)) for i in x2]
    x1 = [x / 10 for x in range(0, 21)]
    y_x1 = [math.sin(i) for i in x1]
    y1 = [math.sin(i) for i in x]
    top = Toplevel(root)
    top.geometry("500x600")

    fig3 = Figure(figsize=(6, 3))
    a3 = fig3.add_subplot(111)
    a3.plot(x1, [y_x1[i] - lagr(x1, y_x1, x1[i]) for i in range(len(x1))], color='blue')
    a3.set_title("Похибка sin(x)", fontsize=16)
    canvas = FigureCanvasTkAgg(fig3, master=top)
    canvas.get_tk_widget().pack()
    canvas.draw()

    fig4 = Figure(figsize=(6, 3))
    a4 = fig4.add_subplot(111)
    a4.plot(x2, [y_x2[i] - lagr(x2, y_x2, x2[i]) for i in range(len(x2))], color='blue')
    a4.set_title("Похибка cos(x + cos(x)^3)", fontsize=16)
    canvas = FigureCanvasTkAgg(fig4, master=top)
    canvas.get_tk_widget().pack()
    canvas.draw()



if __name__ == "__main__":
    MY_FONT = "Arial 20"
    root = Tk()
    root.geometry("500x500")
    root.title("Labwork №3 by Andrii Doroshenko")
    l1 = Label(root, text="Лабораторна робота №3\n"
                          "\"Інтерполяція функцій\"\n(метод Лагранжа)\n\n"
                          "Виконав студент групи ІО-73\n"
                          "Дорошенко Андрій (Варіант 8)\n\n"
                          "Введіть кількість вузлів:", font=MY_FONT)
    l1.pack()
    e1 = Entry(root, width = 20, font = MY_FONT)
    e1.pack()
    b1 = Button(root, text="show sin", command=lambda: sin_window(e1.get()), width=20, height=2,
                font="Arial 16").pack()
    b2 = Button(root, text="show var", command=lambda: var_window(e1.get()), width=20, height=2,
                font="Arial 16").pack()
    b3 = Button(root, text="show fault", command=lambda: fault_window(e1.get()), width=20, height=2,
                font="Arial 16").pack()


    root.mainloop()
