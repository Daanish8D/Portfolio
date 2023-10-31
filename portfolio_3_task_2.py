bad_passwords = ['password', "letmein", "sesame", "hello", "justinbieber"]

passwd = input('Please enter a password: ')

if passwd in bad_passwords:
    print("Common password used")

while True:
    if len(passwd) < 8:
        print('Your password is not long enough!')
        passwd = input('Please enter a password: ')
    elif len(passwd) > 12:
        print('Your password is too long!')
        passwd = input('Please enter a password: ')
    else:
        print('Your password is long enough!')
        break
passwd2 = input('Confirm your password: ')
while True:
    if passwd2 != passwd:
        print('Passwords do not match.')
        passwd2 = input('Confirm your password: ')
    else:
        print('Congratulations, password set!')
        break
