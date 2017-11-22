def sum_pow_dig_seq(start, n, k):
  diccionario = {}
  lista =[]
  excluidos = []
  cyc_patt_arr = []
    

    
  def resultado(start, n, k):
    start = str(start)
    elevado = 0
    h = 1
    if k == 1:
      for numero in start:
        elevado += int(numero)**n
      diccionario[k] = elevado
      for valor in diccionario.values():
        if valor not in lista:
          lista.append(valor)
        else:
          excluidos.append(valor)
      lista.reverse()    
      excluidos.reverse()    
      for elemento in excluidos:
        if elemento not in cyc_patt_arr:
          cyc_patt_arr.append(elemento)          
      for i in range(len(lista)):
          if lista[i] in cyc_patt_arr:             
              h += i
              return [h, cyc_patt_arr, len(cyc_patt_arr), diccionario[1]]          
    else: 
      for numero in start:
        elevado += int(numero)**n
      diccionario[k] = elevado
      return resultado(elevado, n, k-1)



  solucion = resultado(start, n, k)  
  return solucion