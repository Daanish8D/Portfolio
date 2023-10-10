print("Hello World")

print("Hello Daanish")

celsius = float(input("Enter a temperature in celsius "))

fahrenheit = celsius * 1.8 + 32

print(celsius, "in Celsius, is", fahrenheit, "in Fahrenheit.")

matches_played = int(input("Enter number of matches played "))
times_batted = int(input("Enter number of times batted "))
not_out = int(input("Enter number of times not out "))
runs_scored = int(input("Enter number of runs scored "))

batting_average = runs_scored/(times_batted-not_out)

print("Your batting average is", batting_average)

lab_group = int(input("Enter number of students in a group "))
students = int(input("Enter number of students "))

groups = students//lab_group
remainder = students&lab_group

print("The number of full groups is", groups, "and the smaller group is made up of", remainder)
