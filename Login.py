import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import simpledialog



# create database and table
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="20011103S-",
  database="Voitures"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
   
def signup():
	root.destroy()
	import SignUp

# create login function
def login():
   username = username_entry.get()
   password = password_entry.get()
   if username=="" or password=="" :
    	messagebox.showerror('Error', 'All fields are mandatory')
   else : 
    # check if user exists in database
    sql = "SELECT * FROM user WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    user = mycursor.fetchone()

   if user:
          root.destroy()
          import Menu
   else:
        # show error message
        error_message = messagebox.showerror("Error", "Invalid username or password!")



def Log_As_Admin():
    username = username_entry.get()
    password = password_entry.get()
    if username == "" or password == "":
        messagebox.showerror('Error', 'All fields are mandatory')
    else:
        if username == "hamza" and password == "hamza":
            result = simpledialog.askstring("Choose Window", "Do you want to go to Users Management (Type 1) or Cars Management (Type 2)?")
            if result == "1":
                root.destroy()
                import UserMangement
            elif result == "2":
                root.destroy()
                import CarsManagement
        else:
            messagebox.showerror('Error', 'Access denied')

# create main window
root = tk.Tk()
root.title("Login Form")
# load the image file
img = Image.open("LoginCover.jpg")

# resize the image
img = img.resize((600, 1066))

# convert the image to a format that Tkinter can use
img_tk = ImageTk.PhotoImage(img)

# create a label to display the image
img_label = tk.Label(root, image=img_tk)

# position the label in the window
img_label.pack()
root.geometry("600x1066")

# disable window resizing
root.resizable(False, False)

Car_rental=tk.Label(root, text="CAR RENTAL",fg='peru',font=('bookman', 20, 'bold'))
Car_rental.place(x=277, y=33)

# create labels
User_label=tk.Label(root, text="Username: ",fg='peru',font=('bookman', 15, 'bold'))
User_label.place(x=125, y=149)
Pass_Label=tk.Label(root, text="Password: ",fg='peru',font=('bookman', 15, 'bold'))
Pass_Label.place(x=125, y=188)

# create entries
username_entry = tk.Entry(root,fg='black',font=('bookman', 15, 'bold'))
password_entry = tk.Entry(root, show="*",fg='black',font=('bookman', 15, 'bold'))

username_entry.place(x=260, y=149)
password_entry.place(x=260, y=188)


# create login button and signup button
Login_Button=tk.Button(root, text="Login", command=login,fg='peru',font=('bookman', 15, 'bold'))
Login_Button.place(x=300, y=245)

Signup_Button=tk.Button(root, text="Signup", command=signup,fg='peru',font=('bookman', 15, 'bold'))
Signup_Button.place(x=400, y=245)

Log_As_Admin_Button=tk.Button(root, text="Login As Admin", command=Log_As_Admin,fg='peru',font=('bookman', 15, 'bold'))
Log_As_Admin_Button.place(x=100, y=245)

root.mainloop()
