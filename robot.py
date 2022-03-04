from weapon import Weapon
from dinosaur import Dinosaur


class Robot: # User Stories : As a developer I want to make a class for; Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

    def __init__(self, name, health): # User Stories : As a developer, I want a Robot to have a Name, Health, and a Weapon.
        self.name = name
        self.health = health
        self.weapon = Weapon("Photon Blaster, 45")
        

    def robot_attack(self, dinosaur): #User Stories : As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield.
        dinosaur.health -= self.weapon.attack_power #User Stories : As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power)


