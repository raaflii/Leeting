def longestCommonPrefix(strs):
    strs.sort()

    first = strs[0]
    last = strs[-1]

    limit = 0

    for i in range (min(len(first), len(last))):
        if first[i] != last [i]:
            break
        else:
            limit += 1
    
    if limit == 0:
        return ""
    
    return first[:limit]

# a = longestCommonPrefix(["flower","flow","flight"])
# a = longestCommonPrefix(["dog","racecar","car"])
a = longestCommonPrefix(["cir","car"])
print(a)