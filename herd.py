from dinosaur import Dinosaur

class Herd:

    def __init__(self):
        self.dinosaur.list = []
        self.create_herd()


    def create_herd(self):
        rex = Dinosaur("Rex, 120, 50")
        trike = Dinosaur("Trike, 120, 35")
        bronto = Dinosaur("Bronto, 130, 45")

        
        self.dinosaur.list.append(rex) 
        self.dinosaur.list.append(trike)
        self.dinosaur.list.append(bronto)
