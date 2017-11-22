def fibonacci(n):
    fib0 = 0
    fib1 = 1
    for numero in range(n):
      fib0, fib1 = fib1, fib0 + fib1
    return fib0