import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from PIL import ImageTk, Image
from tkinter import messagebox

def GoTo_Search_Car() :
    root.destroy()
    import SearchCar

def GoTo_Cars_List() :
    root.destroy()
    import CarsList

def GoTo_book() :
    import Booking

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
title_label = tk.Label(root, text="WELCOME TO CAR RENTAL SYSTEM", font=("bookman", 24), bg="#0078D7", fg="white")
title_label.place(x=0, y=0, relwidth=1, height=50)

# Create three buttons
button1 = tk.Button(root, text="SHOW ALL CARS INFORMATIONS" , command=GoTo_Cars_List,fg="#0078D7",font=("bookman", 13, "bold"))
button1.place(x=240, y=60, width=350, height=50)

button2 = tk.Button(root, text="SEARCH FOR A CAR", command=GoTo_Search_Car,fg="#0078D7",font=("bookman", 13, "bold"))
button2.place(x=240, y=120, width=350, height=50)

button3 = tk.Button(root, text="BOOK A CAR",command=GoTo_book,fg="#0078D7",font=("bookman", 13, "bold"))
button3.place(x=240, y=180, width=350, height=50)

button4 = tk.Button(root, text="LOG OUT",command=Log_out,fg="#0078D7",font=("bookman", 13, "bold"))
button4.place(x=240, y=240, width=350, height=50)

# Start the main event loop
root.mainloop()
