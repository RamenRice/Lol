import math
a = float(input('What is the acceleration?(m/s/s): '))
d = float(input('What is your displacment?(m): '))
t = float(input('What is your time?(s/sec): '))
v1 = float(input('What is your initial velocity?(m/s): '))
v2 = float(input('What is your final velocity?(m/s): '))
def findAcc():
    if d == 0:
        solution = (v2-v1)/t
        a = solution
        print(str(a) + 'm/s/s')
    if v2 == 0:
        p1 = d-(v1*t)
        solution = p1/(t*t*.5)
        a = solution
        print(str(a) + 'm/s/s')
    if t == 0:
        p1 = (v2*v2)-(v1*v1)
        solution = p1/(2*d)
        a = solution
        print(str(a) + 'm/s/s')
def findDis():
    if a == 0:
        solution = (.5*t)*(v2+v1)
        d = solution
        print(str(d) + 'm')
    if v2 == 0:
        solution = (.5*a)*(t*t)+(v1*t)
        d = solution
        print(str(d) + 'm')
    if t == 0:
        p1 = (v2*v2)-(v1*v1)
        solution = p1/(2*a)
        d = solution
        print(str(d) + 'm')
def findTime():
    if a == 0:
        solution = (v2+v1)*.5/d
        t = solution
        print(str(t) + "s")
    if d == 0:
        soltion = (v2-v1)/a
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
