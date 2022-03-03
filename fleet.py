from robot import Robot

class Fleet:

    def __init__(self):
        self.robots = []
        self.create_fleet()


    def create_fleet(self):
        r2d2 = Robot("R2D2, 120")
        c3po = Robot("C3PO, 125")
        bb8 = Robot("BB8, 100")

