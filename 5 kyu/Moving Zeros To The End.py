def move_zeros(array):
  lista = []
  for i in array:
    if i != 0 or i is False:
      lista.append(i)
  for zero in array:
    if zero == 0 and zero is not False:
      lista.append(zero)
  return lista