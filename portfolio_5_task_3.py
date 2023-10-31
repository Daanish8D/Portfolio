import sys

def shortest(e):
  return len(e)

list = sys.argv

list.sort(key=shortest)

print(list[1:])
