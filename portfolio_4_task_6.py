temp = input("Input the temperature you would like to convert in centigrade: ")
if scale.upper() == "C":
    degree = int(temp[:-1])
    result = int((degree * 1.8 + 32))
    print(result, 'F')
else:
    print('Temperature entered in wrong format.')
