import tkinter as tk

import random

window = tk.Tk()

canvas1=tk.Canvas(window, width=500, height=500)
canvas1.pack()

label1 = tk.Label(text="welcome to dice roll game",fg="black",bg="green")
canvas1.create_window(250, 50, window=label1)


entry1=tk.Entry()
canvas1.create_window(250, 100, window=entry1)

def playgame():


  def playdice():

    x = int(entry1.get())

    if x==1:

     label1= tk.Label(text=random.randrange(1,7),bg="yellow")
     canvas1.create_window(150, 250, window=label1)

    elif x==2:
     label1 = tk.Label(text=random.randrange(1, 7),bg="green")
     canvas1.create_window(150, 250, window=label1)
     label1 = tk.Label(text=random.randrange(1, 7),bg="blue")
     canvas1.create_window(150, 300, window=label1)

    elif x==3:

      label1 = tk.Label(text=random.randrange(1, 7),bg="green")
      canvas1.create_window(150, 250, window=label1)
      label1 = tk.Label(text=random.randrange(1, 7),bg="blue")
      canvas1.create_window(150, 300, window=label1)
      label1 = tk.Label(text=random.randrange(1, 7),bg="yellow")
      canvas1.create_window(150, 350, window=label1)

    else:
        label1 = tk.Label(text="please choose between 1 to 3",fg="red")
        canvas1.create_window(150, 250, window=label1)

  button2 = tk.Button(text='roll dice',fg="black",bg="green", command=playdice)
  canvas1.create_window(185, 200, window=button2)

  button3 = tk.Button(text='EXIT',fg="black",bg="red", command=window.destroy)
  canvas1.create_window(320, 200, window=button3)

button1 = tk.Button(text='you can roll between 1 to 3 dice',bg="blue", fg="black",command=playgame)
canvas1.create_window(250, 150, window=button1)


window.mainloop()