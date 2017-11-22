def openOrSenior(data):
  lista = []
  for i in data:
    if i[0]>=55 and i[1] > 7:
      lista.append('Senior')
    else:
      lista.append('Open')
  return lista 