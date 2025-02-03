def happyNumber(n):
    validation = []
    while True:
        temp = 0
        for i in str(n):
            temp += int(i)**2

        n = temp

        if temp in validation:
            return False
        
        validation.append(temp)
        
        if temp == 1:
            return True
            
    

a = happyNumber(2)
print(a)
        
    

