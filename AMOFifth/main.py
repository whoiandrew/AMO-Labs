from tkinter import *
from tkinter import messagebox


def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i

        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            try:
                c = -A[k][i] / A[i][i]
            except ZeroDivisionError:
                messagebox.showerror("Помилка", "Введені дані не можуть бути використані")
                exit()
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        try:
            x[i] = A[i][n] / A[i][i]
        except ZeroDivisionError:
            messagebox.showerror("Помилка", "Введені дані не можуть бути використані")
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

def show_result():

    A = [[e11.get(), e12.get(), e13.get(), e14.get()],
         [e21.get(), e22.get(), e23.get(), e24.get()],
         [e31.get(), e32.get(), e33.get(), e34.get()]]
    try:
        res = [list(map(lambda x: float(x), i)) for i in A]
    except ValueError:
        messagebox.showwarning("Увага!", "Пане, вхідні дані є помилковими")
        exit()
    top = Toplevel(root)
    top.geometry("300x300")
    x_list = list(map(lambda x: round(x, 6), gauss(res)))
    for i in range(len(x_list)):
        Label(top, text = f"x{i+1} = {x_list[i]}", font = "Arial 16").pack()
    #Label(top, text = f"{x_list}").pack()
2
if __name__ == "__main__":
    # A = [[1.84, 2.25, 2.58, -6.09],
    #      [2.32, 2, 2.82, -6.96],
    #      [2.83, 2.06, 2.24, -5.52]]
    # A = [list(map(lambda x: float(x), i)) for i in A]
    root = Tk()
    root.geometry("500x300")
    root.title("AMO 5th Labwork")
    Label(root, text="Розв'язування СЛАР\n"
                     "Метод Гауса з одиничними коефіціэнтами\n\n", font="Arial 16").grid(row=0, column=0, columnspan=8)
    for i in range(3):
        Label(root, text="x1 + ", font="Arial 16").grid(row=i + 1, column=1)
        Label(root, text="x2 + ", font="Arial 16").grid(row=i + 1, column=3)
        Label(root, text="x3", font="Arial 16").grid(row=i + 1, column=5)
        Label(root, text="=", font="Arial 16").grid(row=i + 1, column=6)
    (e11, e12, e13, e14, e21, e22, e23, e24, e31, e32, e33, e34) = (StringVar() for i in range(12))
    Entry(root, width=4, font="Arial 16", textvariable = e11).grid(row=1, column=0)
    Entry(root, width=4, font="Arial 16", textvariable=e12).grid(row=1, column=2)
    Entry(root, width=4, font="Arial 16", textvariable=e13).grid(row=1, column=4)
    Entry(root, width=4, font="Arial 16", textvariable=e14).grid(row=1, column=8)

    Entry(root, width=4, font="Arial 16", textvariable = e21).grid(row=2, column=0)
    Entry(root, width=4, font="Arial 16", textvariable=e22).grid(row=2, column=2)
    Entry(root, width=4, font="Arial 16", textvariable=e23).grid(row=2, column=4)
    Entry(root, width=4, font="Arial 16", textvariable=e24).grid(row=2, column=8)

    Entry(root, width=4, font="Arial 16", textvariable = e31).grid(row=3, column=0)
    Entry(root, width=4, font="Arial 16", textvariable=e32).grid(row=3, column=2)
    Entry(root, width=4, font="Arial 16", textvariable=e33).grid(row=3, column=4)
    Entry(root, width=4, font="Arial 16", textvariable=e34).grid(row=3, column=8)

    Label(root, text="\n\n", font="Arial 12").grid(row=4, column=0, columnspan=8)
    Button(root, text = "Порахувати", command = show_result, font = "Arial 16").grid(row=5, column = 0, columnspan = 8)



    root.mainloop()
