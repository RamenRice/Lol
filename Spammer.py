import keyboard
import time
import random
import sys
charList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','?','!','@','#','$','%','&']
randomTextList = []
howManyTimes = int(input('How many time would you like to spam? : '))
howManyChar = int(input('How many chars do you want? : '))
def spammer():
    for i in range(howManyTimes):
        for i in range(howManyChar):
            random_chars = random.choice(charList)
            randomTextList.append(random_chars)
        randomText = ''.join(randomTextList)
        keyboard.write(randomText)
        keyboard.press_and_release('enter')
        randomTextList.clear()
        time.sleep(0)
if howManyTimes >= 1:
    time.sleep(2)
    spammer()
else:
    sys.exit()