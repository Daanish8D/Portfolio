import sys
import statistics

def shortest(e):
  return len(e)

temps = sys.argv

temps.sort(key=shortest)

print(list[:-1])

print("Highest temperature is:", max(temps))
print("Lowest temperature is:", min(temps))
print("The mean temperature is:", statistics.mean(temps))