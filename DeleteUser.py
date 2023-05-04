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


def delete_user():
    # Get the selected user's ID
    selected_item = tree.selection()[0]
    values = tree.item(selected_item)['values']
    if values[1]=='' :
         messagebox.showerror('Error', 'Please select a valid user')
         return

    user_id = tree.item(selected_item)['text']
    
    # Check if the user is renting a car
    mycursor.execute("SELECT Renter_id FROM voiture WHERE Renter_id = %s", (user_id,))
    result = mycursor.fetchone()
    if result:
        messagebox.showerror("Error", "You cannot delete this user because they are renting a car right now.")
    else:
        # Delete the user from the database
        mycursor.execute("DELETE FROM user WHERE Id = %s", (user_id,))
        mydb.commit()
        
        # Remove the user from the treeview
        tree.delete(selected_item)





# create tkinter window
root = tk.Tk()
root.geometry("1000x400")


# Create a Label widget to display the menu title
title_label = tk.Label(root, text="Delete User", font=("black", 24), bg="#9ACD32", fg="black")
title_label.pack(side=tk.TOP, fill=tk.X)

# Define custom colors
bg_color = '#DC143C'
fg_color = 'peru'
heading_bg_color = '#9ACD32'
heading_fg_color = 'peru'
style = ttk.Style(root)
style.theme_use('default')
style.configure('Custom.Treeview', background='#9ACD32', font=('bookman', 10), rowheight=30)
# create table
tree = ttk.Treeview(root, columns=( 'Name', 'Gender','Email', 'Phone'), style='Custom.Treeview')
tree.heading('#0', text='User id', anchor='center')
tree.heading('#1', text='Name', anchor='center')
tree.heading('#2', text='Gender', anchor='center')
tree.heading('#3', text='Email', anchor='center')
tree.heading('#4', text='Phone', anchor='center')


# Set column width
tree.column('#0', width=50, anchor='center')
tree.column('#1', width=100, anchor='center')
tree.column('#2', width=100, anchor='center')
tree.column('#3', width=100, anchor='center')
tree.column('#4', width=100, anchor='center')



# Apply custom styles
tree.tag_configure('Custom.Treeview', background=bg_color, foreground=fg_color)
tree.tag_configure('Custom.Treeview.Heading', background=heading_bg_color, foreground=heading_fg_color, font=('bookman', 10, 'bold'))

# Add the treeview to the main window
tree.pack(fill='both', expand=True)

# fetch car details from database
mycursor.execute("SELECT * FROM user")
users = mycursor.fetchall()

# populate the table with car details
for user in users:
    tree.insert('', 'end', text=user[0], values=(user[1], user[2], user[3], user[4], user[5]))
    tree.insert('', 'end', text='', values=('', '', '', '', '', '', ''))


tree.pack(side=tk.TOP, pady=10, padx=10)

# create button to delete user from database
delete_button = tk.Button(root, text='Delete User', command=delete_user,fg='floralwhite',  bg='#9ACD32',font=('bookman', 20, 'bold'))
delete_button.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
