import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from PIL import ImageTk, Image

# create database and table
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="20011103S-",
  database="Voitures"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
 

def submit_form():
        username = username_entry1.get()
        password = password_entry1.get()
         
        mycursor = mydb.cursor()
 
        # insert data into table
        sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
        val = (username, password)
        mycursor.execute(sql, val)
        mydb.commit()

        # show success message
        succes=tk.Label(signup_window, text="Signup successful!",fg='peru',font=('Iceberg', 15, 'bold'))
        succes.place(x=144, y=475)


signup_window = tk.Tk()
signup_window.title("Signup Form")

# load the image file
img1 = Image.open("SignupCover.jpg")
img1 = img1.resize((600, 1066))      


# create a label to display the image
img1_tk = ImageTk.PhotoImage(img1)
img1_label = tk.Label(signup_window, image=img1_tk)
img1_label.image = img1_tk # store the image in the label to prevent garbage collection

# position the label in the window
img1_label.pack()

signup_window.geometry("600x1066")
signup_window.resizable(False, False)

# create labels
Suser=tk.Label(signup_window, text="Username: ",fg='peru',font=('Iceberg', 15, 'bold'))
Suser.place(x=129, y=149)

Spass=tk.Label(signup_window, text="Password: ",fg='peru',font=('Arial', 15, 'bold'))
Spass.place(x=129, y=188)

# create entries
username_entry1 = tk.Entry(signup_window,fg='peru',font=('Arial', 15, 'bold'))
password_entry1 = tk.Entry(signup_window, show="*",fg='peru',font=('Arial', 15, 'bold'))

username_entry1.place(x=250, y=149)
password_entry1.place(x=250, y=188)

# create submit button
SignupButt=tk.Button(signup_window, text="Submit", command=submit_form,fg='peru',font=('Arial', 15, 'bold'))
SignupButt.place(x=280, y=237)


signup_window.mainloop()
