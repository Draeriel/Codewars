def summy(string_of_ints):
    suma = 0
    recolector = ''
    for i in string_of_ints:
      if i != ' ':
        recolector += i
      if i == ' ':
        recolector = int(recolector)
        suma += recolector
        recolector = ''
    suma += int(recolector)
    return suma 