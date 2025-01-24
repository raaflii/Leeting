def decToBinary(dec):
    binary = []

    if dec == 0:
        binary.append(0)
    
    while dec > 1:
        reminder = dec % 2
        binary.append(reminder)
        dec //= 2

    if dec == 1:
        binary.append(1)

    sum = 0
    for i in binary:
        sum += i
    return sum

def countingBits(n):
    ans = []
    for i in range (n + 1):
        ans.append(decToBinary(i))
    
    return ans
        


a = countingBits(5)
print(a)
        
