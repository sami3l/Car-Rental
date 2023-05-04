import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from PIL import ImageTk, Image
from tkinter import messagebox

def GoTo_AddCar() : 
    root.destroy() 
    import AddCar

def GoTo_Update() :
    import UpdateCar

def GoTo_Delete() :
    import Delete

def GoTo_Factures() :
    import FacturesList

def GoTo_Contracts() :
    import ContractsList

def Log_out() :
    root.destroy()
    import Login

# Create a Tkinter window
root = tk.Tk()

# Set the window title
root.title("Menu")

# Set the window size
root.geometry("800x600")
# disable window resizing
root.resizable(False, False)

# Load the background image
bg_image = ImageTk.PhotoImage(Image.open("menu.jpg"))

# Create a Label widget to display the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a Label widget to display the menu title
title_label = tk.Label(root, text="Cars Management", font=("bookman", 24), bg="#2F4F4F", fg="white")
title_label.place(x=0, y=0, relwidth=1, height=50)

# Create three buttons
button1 = tk.Button(root, text="ADD CAR" ,command=GoTo_AddCar, fg="#2F4F4F",font=("bookman", 13, "bold"))
button1.place(x=240, y=60, width=350, height=40)

button2 = tk.Button(root, text="UPDATE CAR", command=GoTo_Update,fg="#2F4F4F",font=("bookman", 13, "bold"))
button2.place(x=240, y=100, width=350, height=40)

button3 = tk.Button(root, text="DELETE CAR",command=GoTo_Delete,fg="#2F4F4F",font=("bookman", 13, "bold"))
button3.place(x=240, y=140, width=350, height=40)

button4 = tk.Button(root, text="SHOW FACTURES LIST",command=GoTo_Factures,fg="#2F4F4F",font=("bookman", 13, "bold"))
button4.place(x=240, y=180, width=350, height=40)

button4 = tk.Button(root, text="SHOW CONTRACTS LIST",command=GoTo_Contracts,fg="#2F4F4F",font=("bookman", 13, "bold"))
button4.place(x=240, y=220, width=350, height=40)

button5 = tk.Button(root, text="LOG OUT",command=Log_out,fg="#2F4F4F",font=("bookman", 13, "bold"))
button5.place(x=240, y=260, width=350, height=40)


# Start the main event loop
root.mainloop()
