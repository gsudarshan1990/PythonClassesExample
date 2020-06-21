class piglet:
    years = 0
    def speak(self):
        return self.years*18
hamlet=piglet()
print(hamlet.speak())
hamlet.years=2
print(hamlet.speak())

