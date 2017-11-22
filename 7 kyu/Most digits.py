def find_longest(arr):
    counter = 0
    elMasLargo = 0
    for numero in arr:
        numero = str(numero)
        print(numero)
        if len(numero) > counter:
            counter = len(numero)
            elMasLargo = int(numero)
    return elMasLargo