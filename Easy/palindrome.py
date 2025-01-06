def palindrome (x):
    reverse = str(x)[::-1]
    
    if str(x) == reverse:
        return True
    else:
        return False

palindrome(123)