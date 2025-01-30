from collections import Counter

def findTheDifference(s, t):
    sCount = dict(Counter(s))
    tCount = dict(Counter(t))

    for i, j in tCount.items():
        if i not in s:
            return i
        
        if j != sCount[i]:
            return i


a = findTheDifference("", "y")
print(a)