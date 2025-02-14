def decToBinary(dec):
    binary = []

    if dec == 0:
        binary.append(0)
    
    while dec > 0:
        reminder = dec % 2
        binary.insert(0, reminder)
        dec //= 2

    return binary

def binaryToDec(bin):
    dec = 0
    length = len(bin) - 1

    for i, bin in enumerate(bin):
        i = abs(i - length)
        dec += bin * 2**i

    return dec

def numberComplement(num):
    numBinary = decToBinary(num)
    for i, bin in enumerate(numBinary):
        numBinary[i] = 1 if bin == 0 else 0
    
    decComplement = binaryToDec(numBinary)
    return decComplement


a = numberComplement(424)
print(a)