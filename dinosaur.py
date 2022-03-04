from robot import Robot


class Dinosaur: # User Stories : As a developer I want to make a class for; Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

    def __init__(self, name, health, attack_power): # User Stories : As a developer, I want a Dinosaur to have a Name, Health, and attack power.
        self.name = name
        self.attack_power = attack_power
        self.health = health


    def dinosaur_attack(self, robot): #User Stories : As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield.
        robot.health -= self.attack_power #User Stories : As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power)

        