class Rectangle:
    def __init__(self,length,width,color):
        self.length = length
        self.width = width
        self.color = color

class GUIElement:
    def click(self):
        print("Object is clicked")

class Button(Rectangle,GUIElement):
    def __init__(self,length,width,color,text):
        Rectangle.__init__(self,length,width,color)
        self.text = text

b1=Button(10,5,'red',"good morning")
b1.click()