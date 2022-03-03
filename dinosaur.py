from robot import Robot


class Dinosaur:

    def __init__(self, name, health, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = health


    def dinosaur_attack(self, robot):
        robot.health -= self.attack_power

        