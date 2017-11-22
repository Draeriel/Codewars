def factorial(n):
    if  n >= 0:
        total = 1
        for i in range(2,n+1):
            total *= i
        return total