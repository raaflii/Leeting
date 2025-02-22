def uniqueMorseRepresentations(words):
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    morseRes = []

    for i in words:
        morseWord = ''
        for j in i:
            morseWord += morse[alphabet.index(j)]
        morseRes.append(morseWord)

    res = len(set(morseRes))
    return res

a = ["abcdefghijk" for _ in range(100)]
uniqueMorseRepresentations(a)