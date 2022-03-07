from robot import Robot

class Fleet: # User Stories : As a developer I want to make a class for; Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

    def __init__(self):
        self.robots = [] # User Stories : As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur objects to be stored in a Herd.
        self.create_fleet()


    def create_fleet(self): # User Storeis : As a developer, I want to instantiate three Robot objects and three Dinosaur objects and assign the appropriate values. 
        r2d2 = Robot("R2D2", 120)
        c3po = Robot("C3PO", 125)
        bb8 = Robot("BB8", 100)

        self.robots.append(r2d2)
        self.robots.append(c3po)
        self.robots.append(bb8)
