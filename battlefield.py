#imports
from fleet import Fleet
from herd import Herd

class Battlefield: # User Stories : As a developer I want to make a class for; Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    
    def run_game(self):
        self.display_welcome()
        self.battle()
        

    def display_welcome(self):
        print(f' ***** Robots vs. Dinosaurs ***** ')


    def battle(self):
      while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
        first_move = input (" Who gets to attack : robots or dinos ? ")
          
        if (first_move == 'robots'):
            Battlefield.robot_turn(self)
        elif (first_move == 'dinos'):
            Battlefield.dino_turn(self)

        if len(self.fleet.robots) == 0:
            self.display_winners("Dinos")
        elif len(self.herd.dinosaurs) == 0:
            self.display_winners("Robots")


    def robot_turn(self):
        self.fleet.robots[0].robot_attack(self.herd.dinosaurs[0])
        print(self.fleet.robots[0].name + " attacked " + self.herd.dinosaurs[0].name + " for " + str(self.fleet.robots[0].weapon.attack_power) + " damage ")
        print(self.herd.dinosaurs[0].name + " has " + str(self.herd.dinosaurs[0].health) + " health left.\n")

        if (self.herd.dinosaurs[0].health <= 0) :
            print(self.herd.dinosaurs[0].name + " has been defeated!\n")
            self.herd.dinosaurs.pop(0)



    def dino_turn(self):
        self.herd.dinosaurs[0].dinosaur_attack(self.fleet.robots[0])
        print(self.herd.dinosaurs[0].name + " attacked " + self.fleet.robots[0].name + " for " + str(self.herd.dinosaurs[0].attack_power) + " damage ")
        print(self.fleet.robots[0].name + " has " + str(self.fleet.robots[0].health) + " health left ")

        if (self.fleet.robots[0].health <= 0) :
            print(self.fleet.robots[0].name + " has been defeated!\n")
            self.fleet.robots.pop(0)


    def show_dino_oppenent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass


    def display_winners(self, winner):
        print("Congrats The " + winner + "  live to fight another day " )
