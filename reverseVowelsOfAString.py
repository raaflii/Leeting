def reverseVowels(s):
    vowels = 'aiueoAIUEO'

    s = list(s)
    left = 0
    right = len(s) - 1

    tempLeft = None
    tempRight = None

    while left < right:
        if s[left] in vowels and tempLeft == None:
            tempLeft = s[left]
        elif tempLeft == None:
            left += 1
            continue

        if s[right] in vowels and tempRight == None:
            tempRight = s[right]
        elif tempRight == None:
            right -= 1
            continue

        if tempLeft != None and tempRight != None:
            s[left] = tempRight
            s[right] = tempLeft
            left += 1
            right -= 1
            tempLeft = None
            tempRight = None
    
    s = ''.join(s)
    return s

a = reverseVowels('abcdefghijklmnopqrstuvwxyz')
print(a)