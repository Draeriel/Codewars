def find_uniq(arr):
    diccionario = {}
    for number in arr:
        if number in diccionario:
            diccionario[number] += 1
        if number not in diccionario:
            diccionario[number] = 1
    for numero in diccionario:
            if diccionario.get(numero) == 1:
                return numero