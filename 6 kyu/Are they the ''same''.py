def comp(array1, array2):
    if None in (array1,array2):
        return False
    for numero in array1:
        numero = numero**2
        if numero in array2:
            array2.remove(numero)
        else:
            return False
    return True