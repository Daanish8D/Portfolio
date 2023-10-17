import statistics

number = int(input('Enter a number from 0-100: '))

if 0 <= number <= 100:
    print('True')

else:
    print('False')

upper_lower = input('Type a word to see how many upper and lowercase letters there are: ')

print('Uppercase Letters:', sum(1 for uppercase in upper_lower if uppercase.isupper()))
print('Lowercase Letters:', sum(1 for lowercase in upper_lower if lowercase.islower()))

name = input('Enter your name: ')
print('Hello', name.capitalize())

word = input('Enter a word and see the magic: ')
if len(word) > 1:
    new_word = word[:-1]
    print(new_word)
else:
    print(word)

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

temp = input("Input the temperature you would like to convert in centigrade: ")
if scale.upper() == "C":
    degree = int(temp[:-1])
    result = int((degree * 1.8 + 32))
    print(result, 'F')
else:
    print('Temperature entered in wrong format.')

temps = []
total_temps = int(input("Enter number of temperatures recorded in centigrade: "))

for x in range(1, total_temps + 1):
    temp = input("Enter temperature: ")
    temp = int(temp[:-1])
    temps.append(temp)

print("Highest temperature is:", max(temps))
print("Lowest temperature is:", min(temps))
print("The mean temperature is:", statistics.mean(temps))
