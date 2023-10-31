import statistics

temps = []
total_temps = int(input("Enter number of temperatures recorded in centigrade: "))

for x in range(1, total_temps + 1):
    temp = input("Enter temperature: ")
    temp = int(temp[:-1])
    temps.append(temp)

print("Highest temperature is:", max(temps))
print("Lowest temperature is:", min(temps))
print("The mean temperature is:", statistics.mean(temps))
