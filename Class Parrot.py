class Birds():
    species = "Birds"
    def __init__(self,name,age,type_bird):
        self.name = name
        self.age = age
        self.type_bird = type_bird
    def display(self):
        print('Name:',self.name,':','Age:',self.age,':','Bird Type:',self.type_bird,':','Species:',Birds.species)
bird1 = Birds('Rocky','6','Eagle')
bird2 = Birds('Oliver','7','Sparrow')
bird3 = Birds('Stella','3','Peacock')
bird4 = Birds('Ben','4','Ostrich')
bird5 = Birds('Mala','2','Sparrow')
bird1.display()
bird2.display()
bird3.display()
bird4.display()
bird5.display()