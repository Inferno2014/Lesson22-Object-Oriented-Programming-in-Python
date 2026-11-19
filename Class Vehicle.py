class Vehicle():
    def __init__(self,mileage,age):
        self.mileage = mileage
        self.age = age
    def display(self):
        print('Mileage:',self.mileage,':','Age:',self.age)
#creating a new object
s1 = Vehicle('280','13')
s2 = Vehicle('260','12')
s3 = Vehicle('310','8')
s1.display()
s2.display()
s3.display()