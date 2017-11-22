def high_and_low(numbers):
    minimo = 99999
    maximo = -99999
    lista = []
    recolector = ''
    for numero in numbers:
      if numero != ' ':
        recolector += numero
      if numero == ' ':
        lista.append(int(recolector))
        recolector = ''
    lista.append(int(recolector))    
    for i in lista:
        if i < minimo:
            minimo = i
        if i > maximo:
            maximo = i
    return str(maximo) +' '+ str(minimo)