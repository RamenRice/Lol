import random as rand
keepGoing = True
count = 0
whatNumber = int(input('What number would you like to find? 1-800 : '))
while keepGoing:
    randInt = rand.randint(1, 800)
    print(str(randInt)+ ' '+str(count))
    count = count + 1
    if randInt == whatNumber:
        keepGoing = False
        print('Found the number')
