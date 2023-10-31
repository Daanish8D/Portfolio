upper_lower = input('Type a word to see how many upper and lowercase letters there are: ')

print('Uppercase Letters:', sum(1 for uppercase in upper_lower if uppercase.isupper()))
print('Lowercase Letters:', sum(1 for lowercase in upper_lower if lowercase.islower()))
