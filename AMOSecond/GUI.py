from tkinter import *
from HeapSort import *
from tkinter import messagebox
import time
from tools import *


def from_file_window():
    def dynamic_writer(entry):
        try:
            my_arr = set_rand_arr(int(entry.get()))
            writer("generated_array.txt", my_arr)
            l_set.config(text=f"\nn = {len(my_arr)}\n")
            l_set1.config(text="Дані згенеровано та записано\n")
        except ValueError:
            messagebox.showerror("УВАГА!", "Можуть бути введені тільки цілі числа.")
        entry.delete(0, "end")

    def sort_from_file():
        start = time.time()
        my_sorted = heap_sort(reader("generated_array.txt"))
        end = time.time()
        writer("generated_array.txt", my_sorted)
        l2.config(text="\nВідсортовано!")
        l3.config(text="Перевірте, будь ласка, вищевказаний файл")
        l4.config(text=f"Час виконання: {end - start}")

    top = Toplevel(root)
    top.geometry = ("500x500")
    top.title("HeapSort")
    l1 = Label(top, text=f"Операції виконуються з файлом \"generated_array.txt\"\n"
    f"\nВведіть кількість вхідних даних:", font="Arial 18")
    l1.pack()
    e1 = Entry(top, width=20, bd=3, font="Arial 20")
    e1.pack()
    b_set = Button(top, text="ЗАПИСАТИ", command=lambda: dynamic_writer(e1), font="Arial 18").pack()
    l_set = Label(top, text=f"\nn - (Кількість вхідних даних)\n", font="Arial 20", fg="blue")
    l_set.pack()
    l_set1 = Label(top, fg="green", font="Arial 20")
    l_set1.pack()
    b1 = Button(top, text="ВІДСОРТУВАТИ", command=sort_from_file, font="Arial 18").pack()
    l2 = Label(top, fg="green", font="Arial 24")
    l2.pack()
    l3 = Label(top, font="Arial 24")
    l3.pack()
    l4 = Label(top, font="Arial 24")
    l4.pack()


def from_input_window():
    def cleaner(arr):
        arr.clear()
        l1.config(text=f"\n{arr_from_input}")
        l2.config(text=f"\nВідсортований масив: {arr_from_input}\n")

    def adder():
        try:
            arr_from_input.append(int(e1.get()))
            l1.config(text=f"\n{arr_from_input}")
        except ValueError:
            messagebox.showerror("УВАГА!", "Можуть бути введені тільки цілі числа.")
        e1.delete(0, "end")

    def show_sorted():
        start = time.time()
        heap_sort(arr_from_input)
        end = time.time()
        l2.config(text=f"\nВідсортований масив: {arr_from_input}\n\n(Час виконання: {end - start})")

    top = Toplevel(root)
    top.geometry = ("500x500")
    top.title("HeapSort")
    e1 = Entry(top, width=20, bd=3, font="Arial 20")
    e1.pack()
    b1 = Button(top, text="ДОДАТИ", font="Arial 18", height=1, width=15, command=adder)
    b1.pack()
    b2 = Button(top, text="СКИНУТИ", font="Arial 18", height=1, width=15, command=lambda: cleaner(arr_from_input))
    b2.pack()
    b3 = Button(top, text="ВІДСОРТУВАТИ", font="Arial 18", height=1, width=15, command=show_sorted)
    b3.pack()
    l1 = Label(top, font="Arial 18")
    l1.pack()
    l2 = Label(top, font="Arial 18", fg="blue")
    l2.pack()


if __name__ == "__main__":
    my_n = 0
    arr_from_input = []
    my_arr = set_rand_arr(my_n)
    writer("generated_array.txt", my_arr)
    show_plot()

    root = Tk()
    root.title("АМО-2")
    root.geometry("500x500")
    l1 = Label(root, text="Алгоритми та методи обчислень\nЛабораторна робота №2\nВиконав:\nстудент групи ІО-73\n"
                          "Дорошенко Андрій", font="Arial 18")
    l1.pack()
    l2 = Label(root, text="\nАлгоритм сортування \"Heap Sort\"\n(\"Пірамідальне сортування\")"
                          "\n\nОбчислювальна складність - O(n*log(n))\n", font="Arial 18")
    l2.pack()
    but1 = Button(root, text="Зчитати з файлу", command=from_file_window, width=20, height=2, font=("Arial", 20))
    but1.pack()
    but2 = Button(root, text="Ввести з клавіатури", command=from_input_window, width=20, height=2, font=("Arial", 20))
    but2.pack()
    root.mainloop()

# by @whoiandrew
