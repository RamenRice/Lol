import random
import sys
def pass_gen():
    make_more = True
    while make_more == True:
        if length == 'yes' or length == 'y':
            how_many_pass = int(input('How many passwords would you like? : '))
            for i in range(how_many_pass):
                for i in range(random.randint(3,35)):
                    random_chars = random.choice(char)
                    password.append(random_chars)
                final_pass = ''.join(password)
                print(final_pass)
                password.clear()
            wanna_make_more = input('Would you like to make more password? : ').lower()
            if wanna_make_more == 'y' or wanna_make_more == 'yes':
                make_more = True
            else:
                print('Thank you for using PassGen')
                make_more = False
        elif length == 'no' or length == 'n':
            how_many_char = int(input('How many charactures would you like to be in the password(s)? : '))
            how_many_pass = int(input('How many passwords would you like? : '))
            for i in range(how_many_pass):
                for i in range(how_many_char):
                    random_chars = random.choice(char)
                    password.append(random_chars)
                final_pass = ''.join(password)
                print(final_pass)
                password.clear()
            wanna_make_more = input('Would you like to make more password? : ').lower()
            if wanna_make_more == 'y' or wanna_make_more == 'yes':
                make_more = True
            else:
                print('Thank you for using PassGen')
                make_more = False
        else:
            print('Error! Try Again')
char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','?','!','@','#','$','%','&']
password = []
print("""
  ____                ____            
 |  _ \ __ _ ___ ___ / ___| ___ _ __  
 | |_) / _` / __/ __| |  _ / _ \ '_ \ 
 |  __/ (_| \__ \__ \ |_| |  __/ | | |
 |_|   \__,_|___/___/\____|\___|_| |_|

Password Generator
Created By Ramen
________________________________________________________
""")
start = input('Would you like to use the password Generator? : ').lower()
if start == 'y' or start == 'yes':
    length = input('Would you like a random lenth password? : ').lower()
    pass_gen()
else:
    print('Restart the program when you want to generate passwords')
    sys.exit()
