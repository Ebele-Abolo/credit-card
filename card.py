# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 00:37:54 2021

@author: 13m0nD3m0n
"""

from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Credit card")
root.geometry("600x400")
input_box = Entry(root)
input_box.pack()
def addition():
    card = 2468
    get_input = input_box.get()
    
    try:
    
      print(card + input_box)
    except(TypeError):
        messagebox.showinfo("Password", "correct password " )
def innocret():
        card = [1,3,5,7,9,0]
        get_input = input_box.get()
        try:
            print(card + input_box)
        except(TypeError):
            messagebox.showinfo("Error", "incorrect password")
            
button = Button(root, text = "Enter", command = addition)
button.pack()
root.mainloop()