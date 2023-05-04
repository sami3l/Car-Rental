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
title_label = tk.Label(root, text="Cars List", font=("iceberg", 24), bg="Peru", fg="white")
title_label.pack(side=tk.TOP, fill=tk.X)

# change the background color
root.configure(bg='blue')

# set the window size
root.geometry("900x900")

# create a canvas to display the cars
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# create a frame to hold the cars
frame = tk.Frame(canvas)
frame.pack(fill="both", expand=True)

# add a scrollbar to the canvas
scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# set the canvas width and height
canvas_width = 600
canvas_height = 400
canvas.config(width=canvas_width, height=canvas_height)

# create a list to store the car image objects
car_images = []

# fetch car details from database
mycursor.execute("SELECT * FROM voiture")
cars = mycursor.fetchall()

# display each car with its attributes
for i, car in enumerate(cars):
    # create a frame for the car
    car_frame = tk.Frame(frame, padx=25, pady=30)
    car_frame.grid(row=i, column=0, sticky='w')

    # load the car image and resize it
    image = Image.open(car[3])
    image = image.resize((500, 300), Image.LANCZOS)
    car_image = ImageTk.PhotoImage(image)

    # create a label to display the car image
    image_label = tk.Label(car_frame, image=car_image)
    image_label.image = car_image  # keep a reference to prevent the image from being garbage collected

    # create a label to display the car attributes
    attributes_label = tk.Label(frame, text=f"Marque: {car[1]}\n\nModèle: {car[2]}\n\nCarburant: {car[4]}\n\nPlaces: {car[5]}\n\nTransmission: {car[6]}\n\nPrix: {car[7]}\n\nDisponible: {car[8]}",fg='black',font=("bookman", 13, "bold"))

    # add the car image and attributes labels to the frame
    image_label.grid(row=i, column=0, sticky="w")
    attributes_label.grid(row=i, column=1, sticky="e")

    # add the car image to the list of car image objects
    car_images.append(car_image)

    

# configure the canvas to hold the frame
canvas.create_window((0, 0), window=frame, anchor="nw")

# update the canvas scroll region
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

def Go_back():
    root.destroy()
    import Menu 

back=tk.Button(root, text="Back to menu", command=Go_back, width=10, height=1)
back.place(x=10,y=10)

# start the main tkinter event loop
root.mainloop()
