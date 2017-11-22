def to_camel_case(text):
  if text != '':
    lista = list(text)
    for i in lista:
        if i == '_' or i == '-':
            position = lista.index(i)
            
            mayuscula = lista[position +1] 
            lista[position +1] = mayuscula.upper()
            lista.remove(i)
            
    return ''.join(lista)
  return text  