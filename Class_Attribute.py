class Enemy:
    int_num_of_lives = 5
    def __init__(self,x_coord,y_coord):
        self.x_coord=x_coord
        self.y_coord=y_coord

print(Enemy.int_num_of_lives)
Enemy.int_num_of_lives=10
print(Enemy.int_num_of_lives)