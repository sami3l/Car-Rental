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


def update_car():
    # Get the selected item from the treeview
    selected_item = tree.selection()[0]
    values = tree.item(selected_item)['values']
    if values[1]=='' :
         messagebox.showerror('Error', 'Please select a valid car')
         return
    # Get the new attribute value from the combobox
    selected_attribute = combobox.get()
    new_value = value_entry.get()    
    if selected_attribute == '' :
        messagebox.showerror('Error', 'Please select an attribut')
        return
    if new_value == '' :
        messagebox.showerror('Error', 'Please enter a value')
        return
    # Update the car's attribute in the database
    car_id = int(tree.item(selected_item)['text'])

    if selected_attribute == 'disponible' and new_value == '1':
        sql = "UPDATE voiture SET disponible = True , Renter_id = NULL WHERE id = %s"
        val = (car_id,)
    elif selected_attribute == 'disponible' and new_value == '0':
        messagebox.showerror('Error', 'You can only update this column by booking a car !')
        return
    else:
        sql = f"UPDATE voiture SET {selected_attribute} = %s WHERE id = %s"
        val = (new_value, car_id)

    # Ask user to confirm the update
    confirm = messagebox.askquestion("", "Are you sure you want to update this car?")

    if confirm == 'yes':
        mycursor.execute(sql, val)
        mydb.commit()  # commit the changes to the database
        messagebox.showinfo("", "Car attribute updated successfully.")
    else:
        messagebox.showinfo("", "Update cancelled.")



# create tkinter window
root = tk.Tk()
root.geometry("1000x400")

# Create a Label widget to display the menu title
title_label = tk.Label(root, text="Update a car", font=("Helvetica", 24), bg="#8B008B", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)

# Define custom colors
bg_color = '#9932CC'
fg_color = 'peru'
heading_bg_color = '#9932CC'
heading_fg_color = 'peru'
style = ttk.Style(root)
style.theme_use('default')
style.configure('Custom.Treeview', background='#9932CC', font=('bookman', 10), rowheight=30)
# create table
tree = ttk.Treeview(root, columns=('marque', 'modele', 'carburant', 'places', 'transmission', 'prix', 'disponible','Renter Id'), style='Custom.Treeview')
tree.heading('#0', text='ID', anchor='center')
tree.heading('#1', text='Marque', anchor='center')
tree.heading('#2', text='Modele', anchor='center')
tree.heading('#3', text='Carburant', anchor='center')
tree.heading('#4', text='Places', anchor='center')
tree.heading('#5', text='Transmission', anchor='center')
tree.heading('#6', text='Prix', anchor='center')
tree.heading('#7', text='Disponible', anchor='center')
tree.heading('#8', text='Renter Id', anchor='center')


# Set column width
tree.column('#0', width=50, anchor='center')
tree.column('#1', width=100, anchor='center')
tree.column('#2', width=100, anchor='center')
tree.column('#3', width=100, anchor='center')
tree.column('#4', width=100, anchor='center')
tree.column('#5', width=100, anchor='center')
tree.column('#6', width=100, anchor='center')
tree.column('#7', width=100, anchor='center')
tree.column('#8', width=100, anchor='center')


# Apply custom styles
tree.tag_configure('Custom.Treeview', background=bg_color, foreground=fg_color)
tree.tag_configure('Custom.Treeview.Heading', background=heading_bg_color, foreground=heading_fg_color, font=('bookman', 10, 'bold'))

# Add the treeview to the main window
tree.pack(fill='both', expand=True)

# fetch car details from database
mycursor.execute("SELECT * FROM voiture")
cars = mycursor.fetchall()

# populate the table with car details
for car in cars:
    tree.insert('', 'end', text=car[0], values=(car[1], car[2], car[4], car[5], car[6], car[7], car[8],car[9]))
    tree.insert('', 'end', text='', values=('', '', '', '', '', '', '',''))


tree.pack(side=tk.TOP, pady=10, padx=10)

# create button to add car to database
update_button = tk.Button(root, text='Update Car', command=update_car,fg='floralwhite',  bg='#8B008B',font=('bookman', 20, 'bold'))
update_button.pack(side=tk.BOTTOM, pady=10)

# add combobox to select attribute to update
attributes = ["marque", "modele", "carburant", "places", "transmission", "prix","disponible"]
combobox = ttk.Combobox(root, values=attributes)
value_entry = tk.Entry(root,fg='black',font=('bookman', 15, 'bold'))
value_entry.pack(side=tk.BOTTOM, pady=20,padx=20)

combobox.pack(side=tk.BOTTOM, pady=20)


root.mainloop()
