class Teacher:
    def __init__(self,name,age,code):
        self.name = name
        self.age = age
        self.code = code

    def welcome_students(self):
        print('Welcome students')

class PhysicsTeacher(Teacher):
    def welcome_students(self):
        Teacher.welcome_students(self)
        print('This is physics class')

class BiologyTeacher(Teacher):
    def welcome_students(self):
        Teacher.welcome_students(self)
        print('This is biology class')

pt=PhysicsTeacher('sonu',29,'PHY')
bt=BiologyTeacher('deepu',29,'BIO')
pt.welcome_students()
bt.welcome_students()