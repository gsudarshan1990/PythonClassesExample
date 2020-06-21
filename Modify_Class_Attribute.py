class Enemy:
    speed =8
    def __init__(self,x,y,difficulty):
        self.x = x
        self.y = y
        self.difficulty = difficulty

print(Enemy.speed)
Enemy.speed=10
print(Enemy.speed)
