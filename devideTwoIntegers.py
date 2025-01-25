def devideTwoIntegers (dividend, divisor):
    i = 0
    op = None
    
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        op = '-'

    while True:
        if abs(dividend) < abs(divisor):
            upLimit = 2**31 - 1
            botLimit = -2**31
            if op != None:
                i = int(op + str(i))

            if i > upLimit:
                return upLimit
            elif i < botLimit:
                return botLimit
            
            return i
        else:
            if divisor < 0:
                if dividend > 0:
                    dividend += divisor
                else:
                    dividend -= divisor
            else:
                if dividend > 0:
                    dividend -= divisor
                else:
                    dividend += divisor
            i += 1
    

    
        

a = devideTwoIntegers(7, -3)
print(a)