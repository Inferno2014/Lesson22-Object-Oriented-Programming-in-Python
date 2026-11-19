class Animals():
    def __init__(self,name,age,type_animal,species):
        self.name = name
        self.age = age
        self.type_animal = type_animal
        self.species = species
    def display(self):
        print('Name:',self.name,':','Age:',self.age,':','Animal Type:',self.type_animal,':','Animal:',self.species)
animal1 = Animals('Rana','6','Labrador','Dog')
animal2 = Animals('Bella','7','Bull','Cow')
animal3 = Animals('Ron','3','Asian Tiger','Tiger')
animal4 = Animals('Nbuemo','4','African Lion','Lion')
animal5 = Animals('Gerald','2','Southern Giraffe','Giraffe')
animal1.display()
animal2.display()
animal3.display()
animal4.display()
animal5.display()