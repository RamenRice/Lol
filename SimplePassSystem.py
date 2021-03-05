import sys
start = input('Would you like to make an account? : ').lower()
username_and_password = []
if start == 'yes' or start == 'y':
    print('Now make a username and password')
    username = input('Username: ')
    password = input('Password: ')
    username_and_password.append(username)
    username_and_password.append(password)
else:
    print('Come back when you want to make an account.')
    sys.exit()
test_login = input('Would you like to login? : ').lower()
while start == 'yes' or start == 'y':
    if test_login == 'n' or test_login == 'no':
        sys.exit()
    if test_login == 'y' or test_login == 'yes':
        username_login = input('Type in your username : ')
        password_login = input('Type in your password: ')
        if username_login in username_and_password:
            if password_login in username_and_password:
                print('Succesfull login')
                sys.exit()
            if password_login not in username_and_password:
                print('Unsuccessfull login')
                test_login = input('Would you like to retry login? : ').lower()
        if username_login not in username_and_password:
            print('Unsuccessfull login')
            test_login = input('Would you like to retry login? : ').lower()
    else:
        sys.exit()
