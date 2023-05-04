
class Voiture:
    def __init__(self, marque, modele, image, carburant, places, transmission, prix, disponible):
        self.marque = marque
        self.modele = modele
        self.image = image
        self.carburant = carburant
        self.places = places
        self.transmission = transmission
        self.prix = prix
        self.disponible = disponible

voitures = [
    Voiture('Toyota', 'Corolla', 'Toyota.jpg', 'Gasoline', 5, 'Automatic', 50, True),
    Voiture('Ford', 'Mustang', 'Mustang.jpg', 'Gasoline', 4, 'Automatic', 100, True),
    Voiture('Nissan', 'Altima', 'Nissan.jpg', 'Gasoline', 5, 'Automatic', 45, False),
    Voiture('Chevrolet', 'Camaro', 'Camaro.jpg', 'Gasoline', 4, 'Manual', 90, True),
    Voiture('BMW', '3 Series', 'Bmw.jpg', 'Gasoline', 5, 'Automatic', 65, True),
    Voiture('Audi', 'A4', 'Audi.jpg', 'Gasoline', 5, 'Automatic', 60, False),
    Voiture('Benz', 'C-Class', 'benz.jpg', 'Gasoline', 5, 'Automatic', 70, True),
    Voiture('Tesla', 'Model S', 'Tesla.jpg', 'électrique', 5, 'Automatic', 350, True),
    Voiture('Volvo', 'S60', 'Volvo.jpg', 'Hybrid', 5, 'Automatic', 45, False),
    Voiture('Mazda', 'Mazda3', 'Mazda.jpg', 'Gasoline', 5, 'Manual', 35, False),
    Voiture('Subaru', 'WRX', 'Subaru.jpg', 'Gasoline', 5, 'Manual', 30, True),
    Voiture('Hyundai', 'Elantra', 'Elantra.jpg', 'Hybrid', 5, 'Automatic', 40, True)
    ] 

    