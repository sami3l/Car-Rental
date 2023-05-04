import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from PIL import ImageTk, Image
from tkinter import messagebox

def GoTo_AddUser() : 
    root.destroy() 
    import SignUp

def GoTo_UpdateUser() :
    import UpdateUser

def GoTo_DeleteUser() :
    import DeleteUser

def GoTo_UsersList() :
    import UsersList

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
bg_image = ImageTk.PhotoImage(Image.open("Users.jpg"))

# Create a Label widget to display the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a Label widget to display the menu title
title_label = tk.Label(root, text="Users Management", font=("bookman", 24), bg="#2F4F4F", fg="white")
title_label.place(x=0, y=0, relwidth=1, height=50)

# Create three buttons
button1 = tk.Button(root, text="ADD USER" ,command=GoTo_AddUser, fg="#2F4F4F",font=("bookman", 13, "bold"))
button1.place(x=240, y=135, width=350, height=40)

button2 = tk.Button(root, text="UPDATE USER", command=GoTo_UpdateUser,fg="#2F4F4F",font=("bookman", 13, "bold"))
button2.place(x=240, y=200, width=350, height=40)

button3 = tk.Button(root, text="DELETE USER",command=GoTo_DeleteUser,fg="#2F4F4F",font=("bookman", 13, "bold"))
button3.place(x=240, y=265, width=350, height=40)

button4 = tk.Button(root, text="SHOW USERS LIST",command=GoTo_UsersList,fg="#2F4F4F",font=("bookman", 13, "bold"))
button4.place(x=240, y=330, width=350, height=40)

button4 = tk.Button(root, text="LOG OUT",command=Log_out,fg="#2F4F4F",font=("bookman", 13, "bold"))
button4.place(x=240, y=395, width=350, height=40)


# Start the main event loop
root.mainloop()
