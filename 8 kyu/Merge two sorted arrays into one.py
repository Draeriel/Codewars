def merge_arrays(arr1, arr2):
  lista = []
  for numero in arr1:
    if numero not in arr2:
      arr2.append(numero)
  for numero in arr2:
    if numero not in lista:
      lista.append(numero)    
  lista.sort()    
  return lista