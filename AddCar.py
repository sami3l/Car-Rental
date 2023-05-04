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


def Add_Car():
    marque=marque_entry1.get()
    modele=modele_entry1.get()
    image=image_entry1.get()
    carburant=Carb_combobox.get()
    place=place_entry1.get()
    transmission=trans_combobox.get()
    prix=prix_entry1.get()

    if marque=="" or modele=="" or image=="" or carburant=="" or place=="" or transmission=="" or prix=="":
        messagebox.showerror('Error' , 'Tous les champs sont obligatoires')

    else:     
        mycursor = mydb.cursor()
 
        # insert data into table
        sql = "INSERT INTO voiture (marque,modele, image, carburant, places, transmission, prix,disponible) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"
        val = (marque ,modele, image ,carburant ,place, transmission, prix, True)
        mycursor.execute(sql, val)
        mydb.commit()

        # show success message
        messagebox.showinfo("", "Car Added successfully.")


    


root = tk.Tk()
root.title("Add Car")

# load the image file
img1 = Image.open("AddCover.jpg")
img1 = img1.resize((600, 999))      

# create a label to display the image
img1_tk = ImageTk.PhotoImage(img1)
img1_label = tk.Label(root, image=img1_tk)
img1_label.image = img1_tk # store the image in the label to prevent garbage collection

# position the label in the window
img1_label.pack()

root.geometry("600x800")
root.resizable(False, False)

# create labels

AddCar=tk.Label(root,text="ADDING A CAR",font=('bookman', 25, 'bold'),fg='grey')
AddCar.place(x=277, y=33)

label_marque=tk.Label(root, text="Marque: ",fg='grey',font=('Iceberg', 15, 'bold'))
label_marque.place(x=129, y=138)

label_modele=tk.Label(root, text="Modele: ",fg='grey',font=('Iceberg', 15, 'bold'))
label_modele.place(x=129, y=199)

label_image=tk.Label(root, text="Image (path): ",fg='grey',font=('Iceberg', 15, 'bold'))
label_image.place(x=129, y=260)

label_carburant=tk.Label(root, text="Carburant: ",fg='grey',font=('Iceberg', 15, 'bold'))
label_carburant.place(x=129, y=321)

label_places=tk.Label(root, text="Places: ",fg='grey',font=('Iceberg', 15, 'bold'))
label_places.place(x=129, y=382)

label_transmission=tk.Label(root, text="Transmission: ",fg='grey',font=('Iceberg', 15, 'bold'))
label_transmission.place(x=129, y=433)

label_prix=tk.Label(root, text="Prix: ",fg='grey',font=('Iceberg', 15, 'bold'))
label_prix.place(x=129, y=504)


# create entries
marque_entry1 = tk.Entry(root,fg='black',font=('Iceberg', 15, 'bold'))
modele_entry1 = tk.Entry(root,fg='black',font=('Iceberg', 15, 'bold'))
image_entry1 = tk.Entry(root, fg='black',font=('Iceberg', 15, 'bold'))
Carb_combobox = ttk.Combobox(root, values=['Gasoline', 'Hybrid', 'électrique'], font=('Iceberg', 15, 'bold'), foreground='white', style='TCombobox')
place_entry1 = tk.Entry(root, fg='black',font=('Iceberg', 15, 'bold'))
trans_combobox = ttk.Combobox(root, values=['Automatic', 'Manual'], font=('Iceberg', 15, 'bold'), foreground='white', style='TCombobox')
prix_entry1 = tk.Entry(root, fg='black',font=('Iceberg', 15, 'bold'))



marque_entry1.place(x=270, y=138)
modele_entry1.place(x=270, y=199)
image_entry1.place(x=270, y=260)
Carb_combobox.place(x=270, y=321)
place_entry1.place(x=270, y=382)
trans_combobox.place(x=270, y=433)
prix_entry1.place(x=270, y=504)



# create submit button
AddBtn=tk.Button(root, text="    Add   ", command=Add_Car,fg='grey',font=('Iceberg', 15, 'bold'))
AddBtn.place(x=280, y=600)

def Go_back():
    root.destroy()
    import AdminMenu

back=tk.Button(root, text="Back to Admin Menu", command=Go_back, width=17, height=1)
back.place(x=0,y=10)

root.mainloop()


