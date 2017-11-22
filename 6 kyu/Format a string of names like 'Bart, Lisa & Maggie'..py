def namelist(names):
  lista = []
  contador = 1
  if len(names) == 0:
      return ""
  for diccionario in names:
      for nombre in diccionario.values():
        if len(names) == 1:
          return nombre
        if contador == len(names):
          return ", ".join(lista) + " & " + nombre
        else:
          contador += 1
          lista.append(nombre)