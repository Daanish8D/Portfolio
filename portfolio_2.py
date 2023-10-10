name = input("What is your name? ")

print("Hello", name)

celsius = float(input("Enter a temperature in celsius: "))
fahrenheit = celsius * 1.8 + 32

print(celsius, "C is equivalent to", fahrenheit, "F.")

students = int(input("How many students? "))
lab_group = int(input("Required group size? "))

groups = students // lab_group
remainder = students % lab_group

print("The will be", groups, "groups with", remainder, "students left over.")

sweets = int(input("How many sweets are there? "))

pupils = int(input("Number of pupils? "))

sweets_given = sweets // pupils
remainder_sweets = sweets % pupils

print("The will be", sweets_given, "sweets per pupil with", remainder_sweets, "sweets left over.")
