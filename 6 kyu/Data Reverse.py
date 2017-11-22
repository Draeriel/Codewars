def data_reverse(data):
    counter = 0
    recolector = []
    lista2 = []
    resultado = []
    for number in data:
        recolector.append(number)
        counter +=1
        if counter == 8:
            counter = 0
            lista2 = recolector + lista2
            recolector = []
    return lista2  