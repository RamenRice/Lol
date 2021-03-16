import keyboard
import time
keepGoing = True
time.sleep(5)
def stop(event):
    global keepGoing
    print(event)
    if keyboard.is_pressed('Esc'):
        keepGoing = False
keyboard.hook_key('Esc', stop)
while keepGoing:
    keyboard.write('test')
    keyboard.press_and_release('enter')
    time.sleep(1)
