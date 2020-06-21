class Bus:
    def __init__(self,color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,new_color):
        if isinstance(new_color,str):
            self._color = new_color
        else:
            print('Enter the valid color')

b1=Bus('red')
print(b1.color)
b1.color='pink'
print(b1.color)