from tkinter import *

root = Tk()
root.title('buttons')
root.geometry('300x300')
i = 0


def clickbuttonfunction():
    global i
    i += 1
    button.config(text=i)
    print('button bosildi', i)


button = Button(root, bg='red', width=10, height=2, text=0, command=clickbuttonfunction)
button.pack()
root.mainloop()
