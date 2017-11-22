def square_digits(num):
    lista = []
    string = str(num)
    for i in string:
        i = int(i)
        i *= i
        i = str(i)
        lista.append(i)
    lista = ''.join(lista)    
    return int(lista)