import math
a = float(input('What is the acceleration?: '))
d = float(input('What is your displacment?: '))
t = float(input('What is your time?: '))
v1 = float(input('What is your initial velocity?: '))
v2 = float(input('What is your final velocity?: '))
def findAcc():
    solution = (v2-v1)/t
    a = solution
    print(str(a) + 'm/s/s')
def findDis():
    if a == 0:
        solution = (.5*t)*(v2+v1)
        d = solution
        print(str(d) + 'm')
    if a != 0:
        solution = (.5*a)*(t*t)+(v1*t)
        d = solution
        print(str(d) + 'm')
def findTime():
    if v2 == 0:
        solution = (v2+v1)*.5/d
        t = solution
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
    
