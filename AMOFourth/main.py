from tkinter import *
from tkinter import messagebox
import math
import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def show_calcs():
    try:
        a, b, t = float(e1.get()), float(e2.get()), float(e3.get())
    except ValueError:
        messagebox.showwarning("Увага!", "Пане, зверніть увагу на вхідні дані\nЗдається, там щось не так :(")
        exit()
    if t > 0.4:
        messagebox.showerror("Помилка", "Завелике значення похибки")
        e3.delete(0, "end")
        exit()
    x = [i for i in numpy.arange(a, b, 0.01)]
    y = lambda x: pow(math.sin(x + math.pi / 2), 2) - pow(x, 2) / 4
    d_y = lambda x: 2 * (math.sin(x + math.pi / 2) * math.cos(x + math.pi / 2) - x / 2)

    fxn_list = []
    Dfxn_list = []
    xn_list = []

    def newton(f, Df, x0, epsilon, max_iter):
        fxn_list.clear()
        Dfxn_list.clear()
        xn_list.clear()
        xn = x0
        for n in range(0, max_iter):
            fxn = f(xn)
            fxn_list.append(round(fxn, 8))
            if abs(fxn) < epsilon:
                return xn
            Dfxn = Df(xn)
            Dfxn_list.append(Dfxn)
            if Dfxn == 0:
                return None
            xn = xn - fxn / Dfxn
            xn_list.append(xn)
        return None

    newton(y, d_y, x_zero, t, 14)
    table = list(zip(xn_list, [round(i * 0.1, 8) for i in fxn_list]))
    top = Toplevel(root)
    top.title("Calculations")
    top.geometry("700x600")

    def show_plot():
        top = Toplevel()
        top.geometry("500x300")
        top.title("Plot")
        fig1 = Figure(figsize=(6, 3))
        a1 = fig1.add_subplot(111)
        a1.plot([i for i in numpy.arange(0, b + 2.01, 0.1)],
                [pow(math.sin(i + math.pi / 2), 2) - pow(i, 2) / 4 for i in numpy.arange(0, b + 2.01, 0.1)],
                color='green')
        a1.scatter(xn_list[-1], y(xn_list[-1]), color='red')
        a1.set_title(f"Корінь рівняння:", fontsize=16)
        canvas = FigureCanvasTkAgg(fig1, master=top)
        canvas.get_tk_widget().pack()
        canvas.draw()

    if a <= sample_res and b >= sample_res:
        Label(top, text=f"\t\t\tx\t\tf(x)", font="Arial 12").pack()
        for i in range(len(table)):
            Label(top, text=f"Ітерація №{i + 1}:\t{str(table[i])[1:-1]}", font="Arial 12").pack()
        Label(top, text=f"\nВідповідь з точністю {t} знайдена за {len(xn_list)} ітерацій\n"
        f"x = {xn_list[-1]}", font="Arial 12", fg="red").pack()
        Button(top, width=20, height=1, text="Показати графік", command=show_plot, font="Arial 14").pack()

    else:
        Label(top, text="На вказаному відрізку кореня не існує", font="Arial 12").pack()


if __name__ == "__main__":
    x_zero = 1.352
    sample_res = 1.0298665293222586

    root = Tk()
    root.title("4th AMO")
    root.geometry("500x500")
    Label(root, text=f"""
    Метод Ньютона(метод дотичних)\n\n
    y(x) = (sin(x+pi/2))^2-(x^2/4)\n
    (корінь існує на відрізку [1, 2])
    Обираємо x0 = {x_zero}\n""", font="Arial 14").pack()
    Label(root, text="Введіть значення a:", font="Arial 14").pack()
    e1 = Entry(root, font="Arial 14")
    e1.pack()
    Label(root, text="b:", font="Arial 14").pack()
    e2 = Entry(root, font="Arial 14")
    e2.pack()
    Label(root, text="Похибка:", font="Arial 14").pack()
    e3 = Entry(root, font="Arial 14")
    e3.pack()
    Label(root, text="", font="Arial 14").pack()
    b1 = Button(root, width=20, height=1, text="Показати обчислення", command=show_calcs, font="Arial 14").pack()
    root.mainloop()
