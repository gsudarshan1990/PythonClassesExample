class Base:
    def __init__(self, name, protected_name):
        self.name = name
        self._protected_name = protected_name
    def _protected_print(self):
        print("This is protected print")

b1=Base('sonu','shashank')
print(b1.name)
print(b1._protected_name)
b1._protected_name = 'good name'
b1._protected_print()
print(b1._protected_name)

