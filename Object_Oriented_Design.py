"""



"""

import random

class Player:
    max_x = 450
    max_y = 450

    def __init__(self,x,y,character):
        self._x = x
        self._y = y
        self._character = character
        self._num_of_lives = 10


    def move_up(self,step):
        self._y+=step

    def move_down(self,step):
        self._y-=step

    def move_right(self,step):
        self._x+=step

    def move_left(self,step):
        self._x-=step

    def shoot_candy(self):
        pass

    def display_message(self,message='welcome to the game'):
        print(message)

    def  lose_of_life(self):
        self._num_of_lives-=1

class Candy:
    speed = 40

    def __init__(self,x,y,type_of_movement):
        self._x = x
        self._y = y
        self._type_of_movement = type_of_movement

    def movement(self,step,type_of_movement):
        if type_of_movement == 'horizontal':
           self._x += step
        else:
            self._y -= step

    def is_out_of_boundaries(self):
        return (self._x <0 or self._y < 450 ) or (self._x <0 or self._y < 450)

class Enemy:
     max_x = 450
     max_y = 450

     def __init__(self,x,y,type_of_movement,speed,num_of_lives):
         self._x = random.randint(0,self.max_x)
         self._y = random.randint(0,self.max_y)
         self._num_of_lives = num_of_lives
         self._speed = speed
         self.type_of_movement = type_of_movement

     def move(self,step):
        if self.type_of_movement == 'vertical':
            self._y+=step
        else:
            self._x+=step


     def change_direction(self,type_of_movement):
        if self.type_of_movement == 'vertical':
            self.type_of_movement = 'horizontal'
        else:
            self.type_of_movement = 'vertical'

     def loss_of_lives(self):
         if self._num_of_lives > 0:
             self._num_of_lives -= 1


