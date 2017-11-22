def capitalize(s,ind):
    lista = []
    for i in range(len(s)):
      if i in ind:
        lista.append(s[i].upper())
      else: 
        lista.append(s[i])    
    return "".join(lista)