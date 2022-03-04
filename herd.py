from dinosaur import Dinosaur

class Herd: # User Stories : As a developer I want to make a class for; Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

    def __init__(self):
        self.dinosaurs = [] # User Stories : As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur objects to be stored in a Herd.
        self.create_herd()


    def create_herd(self): # User Storeis : As a developer, I want to instantiate three Robot objects and three Dinosaur objects and assign the appropriate values. 
        rex = Dinosaur("Rex, 120, 50")
        trike = Dinosaur("Trike, 120, 35")
        bronto = Dinosaur("Bronto, 130, 45")

        
        self.dinosaurs.append(rex) 
        self.dinosaurs.append(trike)
        self.dinosaurs.append(bronto)
