from robot import Robot

class Fleet:

    def __init__(self):
        self.robots = []
        self.create_fleet()


    def create_fleet(self):
        r2d2 = Robot()
        c3po = Robot()
        bd1 = Robot()

