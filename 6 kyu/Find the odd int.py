def find_it(seq):
  diccionario = {}
  for numero in seq:
    if numero not in diccionario:
      diccionario[numero] = 1
    if numero in diccionario:  
      diccionario[numero] += 1
  for valor in diccionario.keys():
    if diccionario[valor] % 2 == 0:
      return valor