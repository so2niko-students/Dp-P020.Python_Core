import time

class Human:
    def __init__(self, name = 'John Doe'):
        self.dob = 0
        self._name = name
        print('Human is created')

    #@property  
    #def name(self):
        # self._name.split(' ')[0]

    #@name.setter
    #def name(self, name):
        #self._name = name + ' ' + self._name.split(' ')[1]
        
    def print(self):
        print('Hello, my name is ' + self._name)

    def __getattr__(self, attr):
        if(attr == 'age'):
            return 2020 - 1970
        if(attr == 'name'):
            return 'from universal: ' + self._name.split(' ')[0]
    
class Monkey:
    def __init__(self, name):
        print(name + ' -- monkey')

    def drink(self, drink = 'water'):
        print('I love ' + drink)
        
class Genius(Human, Monkey):
    def __init__(self, name, iq = 100):
        #Monkey.__init__(self, name)
        #Human.__init__(self, name)
        super().__init__(name)
        self.iq = iq
    



#ivan = Human('Ivan Ivanov')
#print(ivan.name)
#print(ivan.dob)
#ivan.print()
#ivan.name = 'Petro'
#print(ivan.name)

gena = Genius('Gena Pupkin', 100)
gena.print()
print(gena.iq)
gena.drink()
#print(gena.age)

