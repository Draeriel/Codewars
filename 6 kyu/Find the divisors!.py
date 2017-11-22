def divisors(integer):
    lista = []
    for i in range(2, integer):
        if integer % i == 0:
            lista.append(i)
    if len(lista) == 0:
        solucion = str(integer) + " is prime"
        return solucion
    return lista