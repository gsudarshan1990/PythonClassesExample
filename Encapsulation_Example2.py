class Base:
    def __private(self):
        print('private from base case')
    def _protected(self):
        print('protected from base case')
    def public(self):
        print('public from the base case')
        self.__private()
        self._protected()

class Derived(Base):
    def __private(self):
        print('private from the derived class')
    def _protected(self):
        print('protected from derived class'        )

d=Derived()
d.public()