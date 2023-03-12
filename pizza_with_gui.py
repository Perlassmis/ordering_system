# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
from PIL import ImageTk, Image 
from tkinter import messagebox




pizza = Tk()
pizza.geometry('600x500')
pizza.title("Ruru's Pizza")

name_label = Label(pizza, text= "What is your name?")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza, width=30)
name_entry.grid(row=0, column=1)

address_label = Label(pizza, text= "What is your adress?")
address_label.grid(row=1, column=0)

address_entry = Entry(pizza, width=30)
address_entry.grid(row=1, column=1)

phone_label = Label(pizza, text= "What is your number?")
phone_label.grid(row=2, column=0)

phone_entry = Entry(pizza, width=30)
phone_entry.grid(row=2, column=1)

#pizza list


 
my_pizza_list = ["Classic Pizza" , "Margaritta" , "Turkish Pizza" , "Simple Pizza"]



pizza_list =Listbox(pizza, selectmode=MULTIPLE, bg="white", fg="red")
pizza_list.grid(row=4, column=1)

for item in my_pizza_list:
    pizza_list.insert(0, item)
    
    
    
    
    def add_pizza():
        result=""
        for item in pizza_list.curselection():
            result= result + str(pizza_list.get(item)) + "\n"
            
            add_lbl.config(text="Shopping Cart:" + "\n" +result)
            
add_lbl =Label(pizza, text="")
add_lbl.grid(row=5, column=1)
    
    

add_button = Button(pizza, text="Add Pizza", command= add_pizza)
add_button.grid(row=5, column=0)


def check():
    text1 = name_entry.get()
    new_lbl =Label(pizza, text="Name:" + text1)
    new_lbl.grid(row=5 ,column=2)
    
    text2 = address_entry.get()
    new_lbl2 = Label (pizza, text="Address" + text2)
    new_lbl2.grid(row=6, column=2)
    
    text3 = phone_entry.get()
    new_lbl3 = Label(pizza, text="Phone Number" + text3)
    new_lbl3.grid(row=7, column=2)
    


check_button = Button(pizza, text="Checkout", command= check)
check_button.grid(row=6, column=0)

del_button =Button(pizza, text="Delete Pizza")
del_button.grid(row=7, column=0)


def deleteme():
    pizza_list.delete(0,3)

del_button= Button(pizza, text ="Delete Pizza", command=deleteme)
del_button.grid(row=7,column=0)

sauce = StringVar()
sauce.set("Extra Material")

sauce = OptionMenu(pizza, sauce, "Olive", "Mushroom", "Goat Cheese", "Meat", "Onion", "Corn")
sauce.grid(row=8, column=0)

def exitme():
    answer = messagebox.askyesno("Hey!", "Are you sure to exit?")
    if answer ==1:
        pizza.destroy()
    else:
        return

exit_button =Button(pizza, text="Exit", command=exitme)
exit_button.grid(row=0, column=9)



    
    








pizza.mainloop()