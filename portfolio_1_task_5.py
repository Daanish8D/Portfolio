lab_group = int(input("Enter number of students in a group "))
students = int(input("Enter number of students "))

groups = students // lab_group
remainder = students & lab_group

print("The number of full groups is", groups, "and the smaller group is made up of", remainder)
