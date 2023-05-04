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


def update_user():
    # Get the selected item from the treeview
    selected_item = tree.selection()[0]
    values = tree.item(selected_item)['values']
    if values[1]=='' :
         messagebox.showerror('Error', 'Please select a valid user')
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
    user_id = int(tree.item(selected_item)['text'])


    sql = f"UPDATE user SET {selected_attribute} = %s WHERE id = %s"
    val = (new_value, user_id)

    # Ask user to confirm the update
    confirm = messagebox.askquestion("", "Are you sure you want to update this user?")

    if confirm == 'yes':
        mycursor.execute(sql, val)
        mydb.commit()  # commit the changes to the database
        messagebox.showinfo("", "User attribute updated successfully.")
    else:
        messagebox.showinfo("", "Update cancelled.")



# create tkinter window
root = tk.Tk()
root.geometry("1000x400")

# Create a Label widget to display the menu title
title_label = tk.Label(root, text="Update User", font=("Helvetica", 24), bg="#6A5ACD", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)


# Define custom colors
bg_color = '#6A5ACD'
fg_color = 'peru'
heading_bg_color = '#6A5ACD'
heading_fg_color = 'peru'
style = ttk.Style(root)
style.theme_use('default')
style.configure('Custom.Treeview', background='#6A5ACD', font=('bookman', 10), rowheight=30)
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

# create button to add car to database
update_button = tk.Button(root, text='Update User', command=update_user,fg='floralwhite',  bg='#6A5ACD',font=('bookman', 20, 'bold'))
update_button.pack(side=tk.BOTTOM, pady=10)

# add combobox to select attribute to update
attributes = ["username", "Gender", "Email", "Telephone"]
combobox = ttk.Combobox(root, values=attributes)
value_entry = tk.Entry(root,fg='black',font=('bookman', 15, 'bold'))
value_entry.pack(side=tk.BOTTOM, pady=20,padx=20)

combobox.pack(side=tk.BOTTOM, pady=20)

root.mainloop()
