class Teacher:
    def __init__(self,name,age,code):
        self.name = name
        self.age = age
        self.code = code

    def welcome_students(self):
        print('Welcome to the class')

class PhysicsTeacher(Teacher):
    def welcome_students(self):
        super().welcome_students()
        print('Welcome to the physics class')

class BiologyTeacher(Teacher):
    def welcome_students(self):
        super().welcome_students()
        print('Welcome to the Biology Class')

pt=PhysicsTeacher('sonu',29,'PHY')
pt.welcome_students()
bt=BiologyTeacher('deepu',29,'BIO')

bt.welcome_students()