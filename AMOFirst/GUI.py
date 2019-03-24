from Algs import *
from tkinter import *
from tkinter import messagebox


def reader(filename, type):
    with open(filename, "r+") as f:
        a = f.read()
        return list(map(type, a.split()))


def selector1():
    select = Toplevel(root)
    select.title("Лінійний")
    Button(select, text="Ввести з клавіатури", command=top_kb1, font="Arial 16").pack()
    Button(select, text="Зчитати з файлу", command=top_file1, font="Arial 16").pack()


def selector2():
    select = Toplevel(root)
    select.title("Що розгалужується")
    Button(select, text="Ввести з клавіатури", command=top_kb2, font="Arial 16").pack()
    Button(select, text="Зчитати з файлу", command=top_file2, font="Arial 16").pack()


def selector3():
    select = Toplevel(root)
    select.title("Циклічний")
    Button(select, text="Ввести з клавіатури", command=top_kb3, font="Arial 16").pack()
    Button(select, text="Зчитати з файлу", command=top_file3, font="Arial 16").pack()


# first window func
def top_kb1():
    def show_input():
        try:
            lab = Label(top, font="Arial 16")
            lab.config(text="\n\n Результат роботи алгоритму (b={}, c={}):\n\n{} \n\n\n".format(en1.get(),
                                                                                                en2.get(),
                                                                                                alg1(float(en1.get()),
                                                                                                     float(en2.get()))))
            lab.pack()
        except ValueError:
            messagebox.showwarning("Увага!", "Помилка вхідних даних.")
        except OverflowError:
            messagebox.showwarning("Увага!", "Відбулося переповнення!\nБудь ласка, введіть менші значення констант.")

    top = Toplevel(root)
    top.geometry("500x500")
    top.title("Лінійний")

    lab1 = Label(top, text="Введіть константи для виконання {}ого алгоритму\n".format(top.title()[:-2].lower()),
                 font="Arial 12")
    lab1.pack()

    lab2 = Label(top, text="Значення b\n(b >= 0):", font="Arial 12")
    lab2.pack()

    en1 = Entry(top, width=20, bd=3, font="Arial 20")
    en1.pack()

    lab3 = Label(top, text="Значення c\n(c >= 0):", font="Arial 12")
    lab3.pack()

    en2 = Entry(top, width=20, bd=3, font="Arial 20")
    en2.pack()

    b1 = Button(top, text="Отримати результат", font="Arial 16",
                command=show_input)
    b1.pack()


def top_file1():
    def show_from_file():
        lab = Label(top, font="Arial 16")
        massive = reader(r"values\\alg1.txt", float)
        lab.config(text="Дані з файлу: b={}, c={}\nРезультат: {}".format(massive[0], massive[1],
                                                                         alg1(massive[0], massive[1])))
        lab.pack()

    top = Toplevel(root)
    top.geometry("500x500")
    top.title("Лінійний")

    lab = Label(top, text="\nЗчитати вхідні дані з файлу\n", font="Arial 18")
    lab.pack()

    b2 = Button(top, text="Зчитати", command=show_from_file, width=20, height=2, font=("Arial", 20))
    b2.pack()


# second window func
def top_kb2():
    def show_input():
        try:
            lab = Label(top, font="Arial 16")
            lab.config(
                text="\n\n Результат роботи алгоритму (a={}, b={}, x={}):\n\n{} \n\n\n".format(en1.get(), en2.get(),
                                                                                               en3.get(),
                                                                                               alg2(float(en1.get()),
                                                                                                    float(en2.get()),
                                                                                                    float(en3.get()))))
            lab.pack()
        except ValueError:
            messagebox.showwarning("Увага!", "Помилка вхідних даних.")
        except OverflowError:
            messagebox.showwarning("Увага!", "Відбулося переповнення!\nБудь ласка, введіть менші значення констант.")

    top = Toplevel(root)
    top.geometry("500x500")
    top.title("Що розгалужується")

    lab1 = Label(top, text="Введіть константи для виконання алгоритму, {}\n".format(top.title().lower()),
                 font="Arial 12")
    lab1.pack()

    lab2 = Label(top, text="Значення a:", font="Arial 12")
    lab2.pack()

    en1 = Entry(top, width=20, bd=3, font="Arial 20")
    en1.pack()

    lab3 = Label(top, text="Значення b:", font="Arial 12")
    lab3.pack()

    en2 = Entry(top, width=20, bd=3, font="Arial 20")
    en2.pack()

    lab3 = Label(top, text="Значення x:", font="Arial 12")
    lab3.pack()

    en3 = Entry(top, width=20, bd=3, font="Arial 20")
    en3.pack()

    b1 = Button(top, text="Отримати результат", font="Arial 16",
                command=show_input)
    b1.pack()


def top_file2():
    def show_from_file():
        lab = Label(top, font="Arial 16")
        massive = reader(r"values\\alg2.txt", float)
        lab.config(text="Дані з файлу: a={}, b={}, x={}\nРезультат: {}".format(massive[0], massive[1], massive[2],
                                                                               alg2(massive[0], massive[1],
                                                                                    massive[2])))
        lab.pack()

    top = Toplevel(root)
    top.geometry("500x500")
    top.title("Що розгалужується")

    lab = Label(top, text="\nЗчитати вхідні дані з файлу\n", font="Arial 18")
    lab.pack()

    b2 = Button(top, text="Зчитати", command=show_from_file, width=20, height=2, font=("Arial", 20))
    b2.pack()


# third window func
def top_kb3():
    def show_input():
        try:
            lab4 = Label(top, font="Arial 10")
            lab4.config(text="\n\n Результат роботи алгоритму (n1={}, n2={}):\n\n{} \n\n\n".format(abs(int(en1.get())),
                                                                                                   abs(int(en2.get())),
                                                                                                   alg3(abs(
                                                                                                       int(en1.get())),
                                                                                                       abs(int(
                                                                                                           en2.get())))))
            lab4.pack()
        except ValueError:
            messagebox.showwarning("Увага!", "Помилка вхідних даних.")
        except OverflowError:
            messagebox.showwarning("Увага!", "Відбулося переповнення!\nБудь ласка, введіть менші значення констант.")

    top = Toplevel(root)
    top.geometry("500x500")
    top.title("Циклічний")

    lab1 = Label(top, text="Введіть константи для виконання {}ого алгоритму".format(top.title()[:-2].lower()),
                 font="Arial 12")
    lab1.pack()

    lab2 = Label(top, text="Значення n1:\n(ціле число >= 0)", font="Arial 12")
    lab2.pack()

    en1 = Entry(top, width=20, bd=3, font="Arial 20")
    en1.pack()

    lab3 = Label(top, text="Значення n2:\n(ціле число >= 0)", font="Arial 12")
    lab3.pack()

    en2 = Entry(top, width=20, bd=3, font="Arial 20")
    en2.pack()

    b1 = Button(top, text="Отримати результат", font="Arial 16",
                command=show_input)
    b1.pack()


def top_file3():
    def show_from_file():
        lab = Label(top, font="Arial 16")
        massive = reader(r"values\\alg3.txt", int)
        lab.config(text="Дані з файaлу: n1={}, n2={}\nРезультат: {}".format(abs(massive[0]), abs(massive[1]),
                                                                            alg3(abs(massive[0]), abs(massive[1]))))
        lab.pack()

    top = Toplevel(root)
    top.geometry("500x500")
    top.title("Циклічний")

    lab = Label(top, text="\nЗчитати вхідні дані з файлу\n", font="Arial 18")
    lab.pack()

    b2 = Button(top, text="Зчитати", command=show_from_file, width=20, height=2, font=("Arial", 20))
    b2.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("АМО-1")
    root.geometry("{}x{}".format(500, 500))

    l1 = Label(root, text="Алгоритми та методи обчислень\nЛабораторна робота №1\nВиконав:\nстудент групи ІО-73\n"
                          "Дорошенко Андрій", font="Arial 18")
    l1.pack()

    l2 = Label(root, text="\nОберіть, будь ласка, алгоритм:\n", font="Arial 18")
    l2.pack()

    but1 = Button(root, text="Лінійний", command=selector1, width=20, height=2, font=("Arial", 20))
    but1.pack()

    but2 = Button(root, text="Що розгалужується", command=selector2, width=20, height=2, font=("Arial", 20))
    but2.pack()

    but3 = Button(root, text="Циклічний", command=selector3, width=20, height=2, font=("Arial", 20))
    but3.pack()

    root.mainloop()

# by @whoiandrew
