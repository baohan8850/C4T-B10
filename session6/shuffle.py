import random
word = "cat"
shuffled = list(word)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
letter = list(shuffled)
for s in letter:
    print(s.upper())