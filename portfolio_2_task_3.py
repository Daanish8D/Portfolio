students = int(input("How many students? "))
lab_group = int(input("Required group size? "))

groups = students // lab_group
remainder = students % lab_group

print("The will be", groups, "groups with", remainder, "students left over.")
