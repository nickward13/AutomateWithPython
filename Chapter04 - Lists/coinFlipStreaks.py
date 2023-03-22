import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlip = []
    for i in range(100):
        if random.randint(0,1) == 0:
            coinFlip.append('H')
        else:
            coinFlip.append('T')

    for i in range(94):
        if coinFlip[i] == coinFlip[i+1] == coinFlip[i+2] == coinFlip[i+3] == coinFlip[i+4] == coinFlip[i+5]:
            numberOfStreaks += 1
            break
        else:
            continue

print(str(numberOfStreaks) + " found out of 10,000.  That is " + str(numberOfStreaks/100) + "%.")