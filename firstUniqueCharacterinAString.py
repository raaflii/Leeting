from collections import Counter

def firstUniqueCharacterinAtring(s):
    word = dict(Counter(s))
    
    for i in word.keys():
        if word[i] == 1:
            return s.index(i)
    
    return -1

a = firstUniqueCharacterinAtring('aabbccc')
print(a)