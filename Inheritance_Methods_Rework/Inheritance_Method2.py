class Teacher:
    def __init__(self,name,age,classcode):
        self.name = name
        self.age = age
        self.classcode = classcode

    def welcome_student(self):
        print("Dear students welcome")

class PhysicsTeacher(Teacher):
    def welcome(self):
        Teacher.welcome_student(self)
        print('Welcome to the physics class')

class BiologyTeacher(Teacher):
    def welcome(self):
        Teacher.welcome_student(self)
        print('Welcome to the Biology class')

pt=PhysicsTeacher('sonu',29,'PHY')
pt.welcome()
bt=BiologyTeacher('Deepu',29,'BIO')
bt.welcome()