"""
You just signed up for a game development competition and now you need to represent sprites using Inheritance. But... wait a minute! Your team has made mistakes in the code and the inheritance is not working correctly. The due date is tomorrow. You need to save your team from being disqualified!

Your job is to fix the errors in the existing code.

These are the requirements for the program:

      - Enemy must be a subclass of Sprite.

      - Player must be a subclass of Sprite.

      - Enemy must be a superclass of DifficultEnemy and HardEnemy.

Submit the working code to complete this mini project.

Tip: remember that subclasses inherit attributes from their superclasses.


"""

class Sprite:

    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter


class Enemy(Sprite):

    def __init__(self, x, y, img_file, speed):
        Sprite.__init__(self, x, y, img_file, speed, 4)
        self.message = "I'm here to protect my master"


class Player(Enemy):

    def __init__(self, x, y, img_file, speed):
        Sprite.__init__(self, x, y, img_file, speed, 5)
        self.speed = 55


class DifficultEnemy(Enemy):

    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 79)
        self.life_counter = 0


class EasyEnemy(Enemy):

    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 39)
        self.life_counter = 0