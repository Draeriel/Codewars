def createDict(keys, values):
    diccionario = {}
    k = len(keys)
    v = len(values)
    for i in range(k):
  
        diccionario[keys[i]] = values[i] if i < v else None
        
    return diccionario