def numberofSegmentsinAString(s):
    s = s.strip()
    
    if len(s) == 0:
        return 0

    count = 1
    for i in range (len(s) - 1):
        if s[i] == ' ' and s[i+1] != ' ':
            count += 1

    return count

# a = numberofSegmentsinAString("Hello, my name is John")
a = numberofSegmentsinAString("&&*** .,,, !!@#")
print(a)