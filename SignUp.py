import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from PIL import ImageTk, Image
from tkinter import messagebox


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
    email = email_entry1.get()
    tel = tel_entry1.get()
    gender = gender_var.get()

    if username=="" or password=="" or email=="" or tel=="" or gender=="":
        messagebox.showerror('Error' , 'Tous les champs sont obligatoires')
    else:     
        mycursor = mydb.cursor()
 
        # insert data into table
        sql = "INSERT INTO user (username, password ,Email , Telephone ,Gender) VALUES (%s,%s,%s,%s,%s)"
        val = (username, password,email,tel,gender)
        mycursor.execute(sql, val)
        mydb.commit()
        signup_window.destroy()
        import Login
        # show success message
        succes=tk.Label(signup_window, text="Signup successful!",fg='grey',font=('Iceberg', 15, 'bold'))
        succes.place(x=144, y=495)

    


signup_window = tk.Tk()
signup_window.title("Signup Form")

# load the image file
img1 = Image.open("SignupCover.jpg")
img1 = img1.resize((600, 999))      

# create a label to display the image
img1_tk = ImageTk.PhotoImage(img1)
img1_label = tk.Label(signup_window, image=img1_tk)
img1_label.image = img1_tk # store the image in the label to prevent garbage collection

# position the label in the window
img1_label.pack()

signup_window.geometry("600x800")
signup_window.resizable(False, False)

# create labels

SignupForm=tk.Label(signup_window,text="Sign up page",font=('bookman', 25, 'bold'),fg='grey')
SignupForm.place(x=277, y=33)

Suser=tk.Label(signup_window, text="Username: ",fg='grey',font=('Iceberg', 15, 'bold'))
Suser.place(x=129, y=138)

Spass=tk.Label(signup_window, text="Password: ",fg='grey',font=('Iceberg', 15, 'bold'))
Spass.place(x=129, y=199)

Semail=tk.Label(signup_window, text="Email: ",fg='grey',font=('Iceberg', 15, 'bold'))
Semail.place(x=129, y=260)

Stel=tk.Label(signup_window, text="Telephone: ",fg='grey',font=('Iceberg', 15, 'bold'))
Stel.place(x=129, y=321)

Sgender=tk.Label(signup_window, text="Gender: ",fg='grey',font=('Iceberg', 15, 'bold'))
Sgender.place(x=129, y=382)


# create entries
username_entry1 = tk.Entry(signup_window,fg='black',font=('Iceberg', 15, 'bold'))
password_entry1 = tk.Entry(signup_window, show="*",fg='black',font=('Iceberg', 15, 'bold'))
email_entry1 = tk.Entry(signup_window, fg='black',font=('Iceberg', 15, 'bold'))
tel_entry1 = tk.Entry(signup_window, fg='black',font=('Iceberg', 15, 'bold'))
# create a StringVar to store the selected gender
gender_var = tk.StringVar()

# create the Checkbutton widgets for male and female
male_checkbox = tk.Checkbutton(signup_window, text="Male", variable=gender_var, onvalue="Male", offvalue=0,fg='grey',font=('Iceberg', 15, 'bold'))
female_checkbox = tk.Checkbutton(signup_window, text="Female", variable=gender_var, onvalue="Female", offvalue=0,fg='grey',font=('Iceberg', 15, 'bold'))



username_entry1.place(x=250, y=138)
password_entry1.place(x=250, y=199)
email_entry1.place(x=250, y=260)
tel_entry1.place(x=250, y=321)
male_checkbox.place(x=250, y=382)
female_checkbox.place(x=320, y=382)

# create submit button
SignupButt=tk.Button(signup_window, text="Submit", command=submit_form,fg='grey',font=('Iceberg', 15, 'bold'))
SignupButt.place(x=280, y=460)

def Go_back():
    signup_window.destroy()
    import Login

back=tk.Button(signup_window, text="Back to Login", command=Go_back, width=10, height=1)
back.place(x=0,y=10)

signup_window.mainloop()
