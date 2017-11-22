def remove_exclamation_marks(s):
  lista = []
  for value in s:
      if value != '!':
        lista.append(value)
  lista = ''.join(lista)      
  return lista