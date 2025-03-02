def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    f0 = 0
    f1 = 1

    for i in range(2, n+1):
        fi = f0 + f1
        f0, f1 = f1, fi
    
    return fi

a = fib(4)
print(a)