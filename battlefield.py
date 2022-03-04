#imports
from fleet import Fleet
from herd import Herd

class Battlefield: # User Stories : As a developer I want to make a class for; Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    
    def start_game(self):
        self.starting_message()
        self.battle()
        


    def starting_message(self):
        print(f"""
Insert witty stuff Here       
       
        
        
        
        
        
        
        
        
        
And Here        
        """)


    def battle(self):
