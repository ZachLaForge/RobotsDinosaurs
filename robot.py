from weapon import Weapon
from dinosaur import Dinosaur


class Robot:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon("Photon Rifle, 45")
        

    def robot_attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power

        
