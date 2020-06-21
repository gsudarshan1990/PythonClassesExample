class Patient:
    def __init__(self,name,age,diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def display_data(self):
        print(f'name {self.name} age {self.age} and diagnosis {self.diagnosis}')

p1=Patient('sonu',30,'lungs')
p1.display_data()