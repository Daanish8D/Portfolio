temp = input("Input the temperature you would like to convert with C or F after it: ")
scale = temp[-1]

if scale.upper() == "C":
    degree = int(temp[:-1])
    result = (degree * 1.8 + 32)
    scale = "Fahrenheit"

elif scale.upper() == "F":
    degree = int(temp[:-1])
    result = (degree - 32) * 5 / 9
    scale = "Celsius"

else:
    print("Input proper scale.")
    quit()

print("The temperature in", scale, "is", result, "degrees.")
