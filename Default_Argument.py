class Spirite:
    def __init__(self, character, x, y):
        self.character = character
        self._x = x
        self._y = y

    def move_forward(self, step =5, movement = 'vertical'):
        if movement == 'vertical':
            self._y +=step
        else:
            self._x += step

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x

s1=Spirite('good',10,20)
print(s1.x)
print(s1.y)
s1.move_forward()
print(s1.x)
print(s1.y)
s1.move_forward(30)
print(s1.y)
print(s1.x)
s1.move_forward(10,'horizontal')
print(s1.x)
print(s1.y)