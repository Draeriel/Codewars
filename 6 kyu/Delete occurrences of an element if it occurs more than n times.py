def delete_nth(order,max_e):
  lista = []
  basura = {}
  for number in order:
      if number not in lista:
        lista.append(number)
        basura[number] = 1
      else:  
        if basura[number] >= max_e:
          pass
        if basura[number] < max_e:
          lista.append(number)
          basura[number] += 1
        
  return lista