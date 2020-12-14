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
