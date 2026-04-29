import math, tkinter as tk

win = tk.Tk()
win.title("Drag and Drop")

pos_x = -1
pos_y = -1

def click(event):
    global pos_x, pos_y
    print("Clicked!")
    objects = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    if object_drag in objects:
        pos_x = event.x
        pos_y = event.y

def move(event):
    print("Moving!")
    global pos_x, pos_y
    if pos_x != -1:
        vector_x = event.x - pos_x
        vector_y = event.y - pos_y
        pos_x = event.x
        pos_y = event.y
        canvas.move(object_drag, vector_x, vector_y)


def release(event):
    print("Released!")
    global pos_x, pos_y
    pos_x = -1
    pos_y = -1

canvas = tk.Canvas(win, width=800, height=800)
canvas.pack()

object_drag = canvas.create_oval(300,300,500,500, fill="peachpuff", outline="peachpuff", width=2)

canvas.bind("<Button-1>", click)
canvas.bind("<B1-Motion>", move)
canvas.bind("<ButtonRelease-1>", release)

win.mainloop()