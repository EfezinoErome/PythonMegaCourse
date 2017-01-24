from tkinter import *

window = Tk()

def call_all():
     #print("I am working!")
     kg_to_grams()
     kg_to_lb()
     kg_to_onces()

def kg_to_grams():
    grams = float(e1_value.get())*1000
    t1.insert(END,grams)
    #do something

def kg_to_lb():
    lbs = float(e1_value.get())*2.20462
    t2.insert(END,lbs)
    #do something

def kg_to_onces():
    ounces = float(e1_value.get())*35.274
    t3.insert(END,ounces)
    #do something

b1 = Button(window,text="convert", command = call_all)
b1.grid(row = 0, column = 2)

l0 = Label(window, text="Kg", height = 1, width = 5)
l0.grid(row = 0, column = 0)

l1 = Label(window, text="Grams", height = 1, width = 15)
l1.grid(row = 2, column = 0)

l2 = Label(window, text="Pounds", height = 1, width = 15)
l2.grid(row = 2, column = 1)

l3 = Label(window, text="Ounces", height = 1, width = 15)
l3.grid(row = 2, column = 2)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value,width=10)
e1.grid(row=0,column = 1)

t1 = Text(window, height = 1, width = 15)
t1.grid(row = 1, column = 0)

t2 = Text(window, height = 1, width = 15)
t2.grid(row = 1, column = 1)

t3 = Text(window, height = 1, width = 15)
t3.grid(row = 1, column = 2)

window.mainloop()
