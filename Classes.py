def func(word, add=5, freq=1):
    print(word*(freq+add))

call = func('hello')


class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showall=True):
        if showall:
            print("This car is a %s %s from %s, it is %s and has %s kms. " % (self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s" %(self.make, self.model, self.year))

whip = car('Ford', 'Fusion', 2012)
whip.display(False)

'''
-------------
-------------
'''

#Static and class methods
class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >=18

    def display(self):
        print(self.name, 'is', self.age, 'year old')

newPerson = person ('tim',18)

print (person.getPopulation())
print (person.isAdult(21))

'''
-----------
----------
'''







