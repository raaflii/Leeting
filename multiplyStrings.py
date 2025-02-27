def stringToInt(num):
    intNum = 0
    lenNum = len(num)

    for i in range(len(num)):
        intNum += (ord(num[i]) - 48)  * 10**(lenNum - (i + 1))

    return intNum

def multiply(num1, num2):
    a = stringToInt(num1)
    b = stringToInt(num2)

    return f"{a * b}"

a = multiply("4382", "3424")
print(a)




    