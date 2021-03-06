from scipy.stats import norm
import random
import time

peopleDictionary = []
# simulation of a single person
class Person():
    def __init__(self, startingImmunity):
        if random.randint(0, 100) < startingImmunity:
            self.immunity = True
        else:
            self.immunity = False

        self.contagiousness = 0
        self.contagiousDays = 0
        self.maskChance = 0
        self.maskCounted = False
        self.mask = False

        # use gaussian distribution for number of friends, average is 5 friends.
        self.friends = int((norm.rvs(size=1, loc=0.5, scale=0.15)[0]*10).round(0))

    def wearMask(self):
        #print(self.maskChance)
        if self.maskChance > 50:
            self.contagiousness /= 2
            self.mask = True
        else:
            self.mask = False

def initiateSim():
    numPeople = int(input('Population: '))
    startingImmunity = int(input('Percentage of people with natural immunity: '))
    startingInfecters = int(input('How many people will be infectious at t=0: '))

    for x in range(0, numPeople):
        peopleDictionary.append(Person(startingImmunity))

    for x in range(0, startingInfecters):
        peopleDictionary[random.randint(0, len(peopleDictionary)-1)].contagiousness = int((norm.rvs(size=1, loc=0.5, scale=0.15)[0]*10).round(0)*10)

    daysContagious = int(input('How many days contagious: '))
    lockdownDay = int(input('Day for lockdown to be enforced: '))
    maskDay = int(input('Day for masks to be used: '))

    return daysContagious, lockdownDay, maskDay

def runDay(daysContagious, lockdown):
    # this section simulates the spread, so it only operates on contagious people, thus:
    for person in peopleDictionary:
        person.maskChance = random.randint(1, 100)

    for person in [person for person in peopleDictionary if person.contagiousness > 0 and person.friends > 0]:
        peopleCouldMeetToday = int(person.friends / 2)
        if peopleCouldMeetToday > 0:
            peopleMetToday = random.randint(0, peopleCouldMeetToday)
        else:
            peopleMetToday = 0

        if lockdown == True:
            peopleMetToday = 0

        for x in range(0, peopleMetToday):
            friendInQuestion = peopleDictionary[random.randint(0, len(peopleDictionary)-1)]
            if random.randint(0, 100) < person.contagiousness and friendInQuestion.contagiousness == 0 and friendInQuestion.immunity == False:
                friendInQuestion.contagiousness = int((norm.rvs(size=1, loc=0.5, scale=0.15)[0]*10).round(0)*10)
                print(peopleDictionary.index(person), ' >>> ', peopleDictionary.index(friendInQuestion))

    for person in [person for person in peopleDictionary if person.contagiousness > 0]:
        person.contagiousDays += 1
        if person.contagiousDays > daysContagious:
            person.immunity = True
            person.contagiousness = 0
            print('|||', peopleDictionary.index(person), ' is immune. |||')
    time.sleep(1.5)

lockdown = False
maskCount = 0
daysContagious, lockdownDay, maskDay = initiateSim()
saveFile = open('pandemicSave.txt', 'a')
for x in range(0, 100):
    print('Day ', x)
    if x == lockdownDay:
        lockdown = True

    if x >= maskDay:
        for person in peopleDictionary:
            person.wearMask()

    for person in peopleDictionary:
        if person.mask == True and person.maskCounted == False:
            person.maskCounted = True
            maskCount += 1
        elif person.mask == False and person.maskCounted == True:
            person.maskCounted = False
            maskCount -= 1

    runDay(daysContagious, lockdown)
    write = str(len([person for person in peopleDictionary if person.contagiousness > 0])) + '\n'
    saveFile.write(write)
    print(len([person for person in peopleDictionary if person.contagiousness > 0]), 'people are contagious on this day.')
    print(maskCount, 'people are wearing masks on this day.', '\n')
    time.sleep(2)

saveFile.close()
