def min(arr):
    minimo = 99999
    for i in arr:
        if i < minimo:
            minimo = i
    return minimo

def max(arr):
    maximo = -99999
    for i in arr:
        if i > maximo:
            maximo = i
    return maximo