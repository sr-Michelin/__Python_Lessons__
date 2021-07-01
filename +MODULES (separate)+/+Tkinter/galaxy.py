import datetime
from tkinter import *
from PIL import Image, ImageTk, ImageGrab

tk = Tk()

n = 0
coords = []
print('програма для графічного зображення введених апертурних координат.'.upper())

S = input('Вкажіть розмір фотографії: ')

try:
    size_ = int(S) / 2.  # Половина розміру зображення
except ValueError:
    print('Розмір фотографії хибний...')
    size_ = 0

canvas = Canvas(tk, width=size_ * 2, height=size_ * 2, bd=0)
image = Image.open("galaxy.jpg")
photo = ImageTk.PhotoImage(image)

image_ = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.pack()

try:
    N = int(input('Вкажіть кількість апертур: '))
    while n <= N - 1:
        cd = input(f'Введіть координати апертури {n}: ')
        cd = cd.split(',')

        if len(cd) == 2:
            x, y = float(cd[0]), float(cd[1])
        else:
            print('Ви забули повністю ввести координати апертури.\nЗакриття програми...')
            break
        coords.append((x, y, n))
        n += 1
except IndexError and ValueError:
    N = 0
    coords.clear()
    print('Дані були введені хибно!\nЗакриття програми...')

print(f'\nТестовий список координат апертур: {coords} із {len(coords)} елементів')


def exit_(event):
    tk.destroy()


for c, n in zip(coords, range(len(coords))):
    l = Label(tk, text=f'Z{c[2]}', font=("Arial 32",
                                         8, "bold"))
    l.place(x=(c[0] * size_ + size_), y=(-c[1] * size_ + size_))

canvas.pack()

with open('galaxy.dat', 'a') as f:
    f.write(f'\n:: date :: {str(datetime.datetime.today())} :: coordinates (x, y, n[app]) :: {str(coords)}')

tk.bind('<Button-2>', exit_)
tk.mainloop()
