number = int(input("Enter the number of the multiplication needed: "))

print("The Multiplication Table of: ", number)
if number < 0:
    for count in range(-12, 0):
        print(number, 'x', count, '=', number * count)
else:
    for count in range(0, 13):
        print(number, 'x', count, '=', number * count)
