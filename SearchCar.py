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

# create a tkinter window
root = tk.Tk()
root.title("Cars List")


title_label = tk.Label(root, text="SEARCH", font=("iceberg", 24), bg="Peru", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)


# create a label for the ComboBox
attributes_label = tk.Label(root, text="Attribute:", font=("bookman", 13, "bold"), bg="peru", fg="white")
attributes_label.place(x=900, y=16)

# create a ComboBox for selecting the attribute
attributes = ttk.Combobox(root, font=("bookman", 13), width=10)
attributes['values'] = ("marque", "modele", "carburant", "places", "transmission", "prix", "disponible")
attributes.place(x=1000, y=16)
attributes.current(0)

# create a label for the input box
input_label = tk.Label(root, text="Value:", font=("bookman", 13, "bold"), bg="peru", fg="white")
input_label.place(x=1150, y=16)

# create an input box for entering the value
input_box = tk.Entry(root, font=("bookman", 13), width=15)
input_box.place(x=1230, y=16)


# change the background color
root.configure(bg='blue')

# set the window size
root.geometry("900x900")

# create a canvas to display the cars
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# set the canvas width and height
canvas_width = 600
canvas_height = 400
canvas.config(width=canvas_width, height=canvas_height)





# create a list to store the car image objects
car_images = []

# function to filter cars based on attribute and value
def filter_cars():
    # get the selected attribute and value from the input box
    attribute = attributes.get()
    value = input_box.get()

    # fetch car details from database
    mycursor.execute(f"SELECT * FROM voiture WHERE {attribute} = %s", (value,))
    cars = mycursor.fetchall()

    # delete all the previous car frames from the canvas
    canvas.delete("all")

    # create a frame to hold the car frames
    cars_frame = tk.Frame(canvas)

    # add a scrollbar to the canvas
    scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # display each car with its attributes that match the filter
    for i, car in enumerate(cars):
        # create a frame for the car
        car_frame = tk.Frame(cars_frame, padx=25, pady=30)
        car_frame.pack(side="top", fill="x", pady=10, padx=10)

        # load the car image and resize it
        image = Image.open(car[3])
        image = image.resize((500, 300), Image.LANCZOS)
        car_image = ImageTk.PhotoImage(image)

        # create a label to display the car image
        image_label = tk.Label(car_frame, image=car_image)
        image_label.image = car_image  # keep a reference to prevent the image from being garbage collected

        # create a label to display the car attributes
        attributes_label = tk.Label(car_frame, text=f"Marque: {car[1]}\n\nModèle: {car[2]}\n\nCarburant: {car[4]}\n\nPlaces: {car[5]}\n\nTransmission: {car[6]}\n\nPrix: {car[7]}\n\nDisponible: {car[8]}", fg='black', font=("bookman", 13, "bold"))

        # add the car image and attributes labels to the frame
        image_label.grid(row=0, column=0, sticky="w")
        attributes_label.grid(row=0, column=1, sticky="e")

        # add the car image to the list of car image objects
        car_images.append(car_image)

    # add the cars frame to the canvas
    canvas.create_window((0, 0), window=cars_frame)

    # update the canvas scroll region
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


Fiter_button= tk.Button(root, text="Search" ,command=filter_cars, fg="peru",font=("bookman", 13, "bold"))
Fiter_button.place(x=1420, y=10)

def Go_back():
    root.destroy()
    import Menu 

back_butt=tk.Button(root, text="Back to menu", command=Go_back, width=10, height=1)
back_butt.place(x=10,y=10)
root.mainloop()

