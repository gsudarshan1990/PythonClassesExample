class Child:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def update_age(child_list):
    print("The details related to age")
    for child in child_list:
        print(f'child name {child.name} and child age {child.age}')

    for child in child_list:
        child.age+=1

    print('After updating the age')
    for child in child_list:
        print(f'child name {child.name} and child age {child.age}')

total_child=[Child('sonu',10),Child('Deepu',15),Child('Rahul',20)]
update_age(total_child)