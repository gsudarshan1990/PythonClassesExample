class Bus:
    def __init__(self,color):
        self.color = color

    def display_student(self,student_name):
        print(f'the student is {student_name} and color of bus is {self.color}')

bus=Bus('red')
Bus.display_student(bus,'sonu')