import math
a = float(input('What is the acceleration?: '))
d = float(input('What is your displacment?: '))
t = float(input('What is your time?: '))
v1 = float(input('What is your initial velocity?: '))
v2 = float(input('What is your final velocity?: '))
def findAcc():
    step1 = v2 - v1
    step2 = step1 / t
    a = step2
    print(str(a) + 'm/s/s')
def findDis():
    if a == 0:
        step1 = .5 * t
        step2 = v2 + v1
        step3 = step1 * step2
        d = step3
        print(str(d) + 'm')
    if a != 0:
        step1 = v1 * t
        step2 = .5 * a
        time = t * t
        step3 = step2 * time
        step4 = step1 + step3
        d = step4
        print(str(d) + 'm')
def findTime():
    if v2 == 0:
        step1 = .5 * a
        time = t * t
        step2 = step1 * time
        step3 = d - step2
        step4 = step3 / v1
        t = step4
        print(str(t) + "s")
#def findInVel:
#def findFinVel:

whatToFind = input("What are you trying to find?: ").lower()
if whatToFind == 'a' or whatToFind == 'acceleration':
    findAcc()
if whatToFind == 'd' or whatToFind == 'distance' or whatToFind == 'displacment':
    findDis()
if whatToFind == 't' or whatToFind == 'time':
    findTime()
    
