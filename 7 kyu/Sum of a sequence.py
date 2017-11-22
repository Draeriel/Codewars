def sequence_sum(begin_number, end_number, step):
  total = begin_number
  incremento = begin_number
  if begin_number > end_number:
    return 0
  for i in range(begin_number, end_number, step):
    incremento += step
    if incremento <= end_number:
      print(total)
      
      total += incremento
  return total