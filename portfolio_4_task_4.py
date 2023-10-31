word = input('Enter a word and see the magic: ')
if len(word) > 1:
    new_word = word[:-1]
    print(new_word)
else:
    print(word)
