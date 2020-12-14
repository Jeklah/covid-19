from scipy.stats import norm
import random
import time

# simulation of a single person
class Person():
    def __init__(self, startingImmunity):
        if random.randint(0, 100) < startingImmunity:
            self.immunity = True
        else:
            self.immunity = False

        self.contagiousness = 0
        self.mask = False
        self.contagiousDays = 0

        # use gaussian distribution for number of friends, average is 5 friends.
        self.friends = int((norm.rvs(size=1, loc=0.5, scale=0.15)[0]*10).round(0))

        def wearMask(self):
            self.contagiousness /= 2

def initiateSim():
    numPeople = int(input("Population: "))
    startingImmunity = int(input("Percentage of people with natural immunity: "))
    startingInfecters = int(input("How many people will be infectious at t=0: "))

    for x in range(0, numPeople):
        peopleDictionary.append(Person(startingImmunity))

    for x in range(0, startingInfecters):
        peopleDictionary[random.randint(0, len(peopleDictionary)-1)].contagiousness = int((norm.rvs(size=1, loc=0.5, scale=0.15)[0]*10).round(0)*10)

    daysContagious = int(input("How many days contagious: "))
    lockdownDay = int(input("Day for lockdown to be enforced: "))
    maskDay = int(input("Day for masks to be used: "))

    return daysContagious, lockdownDay, maskDay
