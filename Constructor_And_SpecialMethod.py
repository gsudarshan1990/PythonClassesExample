class Apple:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor

janagold=Apple('red','sweet')
print(janagold.color)

class Apple2:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor
    def __str__(self):
        return '{} {}'.format(self.color,self.flavor)

janagold=Apple2("red","sour")
print(janagold)


