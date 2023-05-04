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

# create tkinter window
root = tk.Tk()
root.geometry("1000x400")


# Create a Label widget to display the menu title
title_label = tk.Label(root, text="Factures List", font=("black", 24), bg="#F0FFFF", fg="grey")
title_label.pack(side=tk.TOP, fill=tk.X)

# Define custom colors
bg_color = '#DC143C'
fg_color = 'peru'
heading_bg_color = '#34495E'
heading_fg_color = 'peru'
style = ttk.Style(root)
style.theme_use('default')
style.configure('Custom.Treeview', background='#F0FFFF', font=('bookman', 10), rowheight=30)
# create table
tree = ttk.Treeview(root, columns=('Renter id', 'Renter Name', 'Car id', 'Car Name', 'Car Model', 'Price($)','Type payement'), style='Custom.Treeview')
tree.heading('#0', text='ID facture', anchor='center')
tree.heading('#1', text='Renter id', anchor='center')
tree.heading('#2', text='Renter Name', anchor='center')
tree.heading('#3', text='Car id', anchor='center')
tree.heading('#4', text='Car Name', anchor='center')
tree.heading('#5', text='Car Model', anchor='center')
tree.heading('#6', text='Price($)', anchor='center')
tree.heading('#7', text='Type payement', anchor='center')


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
tree.tag_configure('Custom.Treeview.Heading', background=heading_bg_color, foreground=heading_fg_color, font=('bookman', 10, 'bold'))

# Add the treeview to the main window
tree.pack(fill='both', expand=True)

# fetch car details from database
mycursor.execute("SELECT * FROM factures")
factures = mycursor.fetchall()

# populate the table with car details
for facture in factures:
    tree.insert('', 'end', text=facture[0], values=(facture[1], facture[2], facture[3], facture[4], facture[5], facture[6], facture[7]))
    tree.insert('', 'end', text='', values=('', '', '', '', '', '', ''))


tree.pack(side=tk.TOP, pady=10, padx=10)

root.mainloop()
