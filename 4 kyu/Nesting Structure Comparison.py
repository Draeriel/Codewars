def same_structure_as(original,other):
  principal = ''
  secundario = ''
  if isinstance(other, int) or isinstance(other, dict):
    return False
  if len(original) != len(other):
    return False
  for i in range(0,len(original)):
      principal = str(original[i])
      secundario = str(other[i])
      if len(principal) != len(secundario):
        return False
  return True   