import random
import matplotlib.pyplot as plt

rolls = []
rolllist = [1,2,3,4,5,6,7,8,9,10,11,12]

dev_x = rolllist
dev_y = []


def diceroll():
    dice1 = 0
    dice2 = 0
    dicetotal = 0
    for i in range(1000):
        dice1 = random.randint(0, 6)
        dice2 = random.randint(0, 6)
    dicetotal = dice1 + dice2
    return dicetotal

for i in range(1000):
    rolls.insert(1,diceroll())



for i in range(12):
    text = "Rolled %d %d times, or %.2f%% " % (rolllist[i], rolls.count(i), (rolls.count(i)/100) * 100)
    print(text)

def getYAxis():
    for i in range(12):
        dev_y.insert(1,rolls.count(i))


getYAxis()
plt.plot(dev_x,dev_y)
plt.suptitle("Kyle Lemons: 1000 Dice Rolls")
plt.ylabel('Times the number is rolled')
plt.xlabel("Number rolled")
plt.show()

