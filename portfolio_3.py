name = input('Enter your name: ')

if name:
    print('Hello', name)

else:
    print('Hello Stranger!')

bad_passwords = ['password', "letmein", "sesame", "hello", "justinbieber"]
passwd = input('Please enter a password between 8 to 12 characters: ')

while True:
    if passwd in bad_passwords:
        print("Common password used")
        passwd = input('Please enter a password between 8 to 12 characters: ')

    elif len(passwd) < 8:
        print('Your password is not long enough!')
        passwd = input('Please enter a password between 8 to 12 characters: ')

    elif len(passwd) > 12:
        print('Your password is too long!')
        passwd = input('Please enter a password between 8 to 12 characters: ')

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

number = int(input("Enter the number of the multiplication needed: "))
print("The Multiplication Table of: ", number)

if number >= 0:
    for count in range(0, 13):
        print(number, 'x', count, '=', number * count)

else:
    for count in reversed(range(0, 13)):
        print(number, 'x', count, '=', number * count)
