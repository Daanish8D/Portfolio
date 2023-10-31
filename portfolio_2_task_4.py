sweets = int(input("How many sweets are there? "))

pupils = int(input("Number of pupils? "))

sweets_given = sweets // pupils
remainder_sweets = sweets % pupils

print("The will be", sweets_given, "sweets per pupil with", remainder_sweets, "sweets left over.")
