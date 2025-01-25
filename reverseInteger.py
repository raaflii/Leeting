def reverseInteger(x):
    if str(int(x)) == str(0):
        return 0
    
    op = None 

    if x < 0:
        op = '-'
        x = abs(x)

    rev = ''.join(reversed(str(x)))
    
    i = 0
    while rev[i] == str(0):
         i += 1

    rev = rev[i:]
    
    if op != None:
        rev = op + rev
    
    rev = int(rev)
    if rev < -(2**31) or rev > (2**31 - 1):
        return 0
    
    return rev

a = reverseInteger(1534236469)
print(a)
        
