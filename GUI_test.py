from tkinter import *
import calendar

Root = Tk()
Root.title("备忘录")
Root.geometry('500x300')
l = Label(Root, text=calendar.month(2020,1))
l.pack()
def hit_me():
    print("hello me")
b = Button(Root, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
c = Button(Root, text='hit', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()
c.pack()
Root.mainloop()