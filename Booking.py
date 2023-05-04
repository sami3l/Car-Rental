import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import mysql.connector



# create database and table
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="20011103S-",
  database="Voitures"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS voiture (id INT AUTO_INCREMENT PRIMARY KEY, marque VARCHAR(255), modele VARCHAR(255), image VARCHAR(255), carburant VARCHAR(255), places INT, transmission VARCHAR(255), prix FLOAT, disponible BOOLEAN)")

# fetch car details from database
mycursor.execute("SELECT * FROM voiture")
cars = mycursor.fetchall()

import datetime

def Book_car():
    # Get the selected item from the treeview
    selected_item = tree.selection()[0]
    values = tree.item(selected_item)['values']
    if values[1]=='' :
         messagebox.showerror('Error', 'Please select a valid car')
         return
    # If the car is not available, show an error message
    if not values[6]:
        messagebox.showerror('Error', 'This car is unavailable')
        return
    price=values[5]
    # Prompt the user for their username and password
    username = simpledialog.askstring('Login', 'Confirm your username:', parent=root)
    password = simpledialog.askstring('Login', 'Confirm your password:', parent=root, show='*')

    # Check if the username and password match a user in the database
    sql = "SELECT id FROM user WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result is None:
        messagebox.showerror('Error', 'Invalid username or password')
        return

    # Get the id of the matching user
    user_id = result[0]

    # Prompt the user for the payment type
    payment=''
    payment_type = simpledialog.askinteger('Payment', 'Enter payment type (1: Cash, 2: credit card, 3: paypal):', parent=root)
    if payment_type == 1 :
        payment = 'Cash'
    elif payment_type == 2 :
        payment = 'Credit Card'
    elif payment_type == 3 :
        payment = 'Paypal'
    
    # Prompt the user for the end date of the booking
    end_date = simpledialog.askstring('Booking End Date', 'Enter the end date of the booking (YYYY-MM-DD):', parent=root)

     # Validate the input
    try:
        end_datetime = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        if end_datetime < datetime.datetime.now():
             messagebox.showerror('Error', 'End date must be in the future')
             return
    except ValueError:
        messagebox.showerror('Error', 'Invalid date format')
        return

    # Convert the end date to a string in the correct format
    date_fin = end_datetime.strftime('%Y-%m-%d')


    # Update the car's availability and renter_id in the database
    car_id = int(tree.item(selected_item)['text'])
    sql = "UPDATE voiture SET disponible = false, Renter_id = %s WHERE id = %s"
    val = (user_id, car_id)
    mycursor.execute(sql, val)

    # Insert the booking into the factures table
    sql = "INSERT INTO factures (renter_id, Renter_Name, Type_payement, Car_id,Montant,Car_Name,Car_Model) VALUES (%s,%s, %s, %s,%s,%s,%s)"
    val = (user_id, username, payment, car_id,price,values[0],values[1])
    mycursor.execute(sql, val)

    # Insert the booking into the contrats table
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    # Convert the end date to a Date object
    date_fin = end_datetime.date()


    sql = "INSERT INTO contrats (Car_id, Renter_id, Date_contrat, Num_facture,Car_name,Car_model,Date_fin) VALUES ( %s, %s, %s, %s,%s,%s,%s)"
    val = (car_id, user_id, date, mycursor.lastrowid,values[0],values[1],date_fin)
    mycursor.execute(sql, val)

    mydb.commit()  # commit the changes to the database

    # Update the treeview
    selected_item = tree.selection()[0]
    values = tree.item(selected_item)['values']
    tree.item(selected_item, values=(values[0], values[1], values[2], values[3], values[4], values[5], False, user_id, date_fin))

    messagebox.showinfo("", "Car booked successfully.")



# create tkinter window
root = tk.Tk()
root.geometry("1000x400")



# Create a Label widget to display the menu title
title_label = tk.Label(root, text="Book a car", font=("Helvetica", 24), bg="#0078D7", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)

# Define custom colors
bg_color = '#2C3E50'
fg_color = 'peru'
heading_bg_color = '#34495E'
heading_fg_color = 'peru'
style = ttk.Style(root)
style.theme_use('default')
style.configure('Custom.Treeview', background='light blue', font=('bookman', 10), rowheight=30)
# create table
tree = ttk.Treeview(root, columns=('marque', 'modele', 'carburant', 'places', 'transmission', 'prix', 'disponible'), style='Custom.Treeview')
tree.heading('#0', text='ID', anchor='center')
tree.heading('#1', text='Marque', anchor='center')
tree.heading('#2', text='Modele', anchor='center')
tree.heading('#3', text='Carburant', anchor='center')
tree.heading('#4', text='Places', anchor='center')
tree.heading('#5', text='Transmission', anchor='center')
tree.heading('#6', text='Prix ($)', anchor='center')
tree.heading('#7', text='Disponible', anchor='center')

# Set column width
tree.column('#0', width=50, anchor='center')
tree.column('#1', width=100, anchor='center')
tree.column('#2', width=100, anchor='center')
tree.column('#3', width=100, anchor='center')
tree.column('#4', width=100, anchor='center')
tree.column('#5', width=100, anchor='center')
tree.column('#6', width=100, anchor='center')
tree.column('#7', width=100, anchor='center')

# Apply custom styles
tree.tag_configure('Custom.Treeview', background=bg_color, foreground=fg_color)
tree.tag_configure('Custom.Treeview.Heading', background=heading_bg_color, foreground=heading_fg_color, font=('bookman', 14, 'bold'))

# Add the treeview to the main window
tree.pack(fill='both', expand=True)


# populate the table with car details
for car in cars:
    tree.insert('', 'end', text=car[0], values=(car[1], car[2], car[4], car[5], car[6], car[7], car[8]))
    tree.insert('', 'end', text='', values=('', '', '', '', '', '', ''))

tree.pack(side=tk.TOP, pady=10, padx=10)

# create button to add car to database
add_button = tk.Button(root, text='Book Car', command=Book_car,fg='floralwhite',  bg='#0078D7',font=('bookman', 20, 'bold'))
add_button.pack(side=tk.BOTTOM, pady=10)

def Go_back():
    root.destroy()
    import Menu 

back=tk.Button(root, text="Back to menu", command=Go_back, width=10, height=1)
back.place(x=0,y=10)
root.mainloop()




