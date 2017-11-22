def balance(left, right):
  pesoLeft = 0
  for i in left:
    if i == '!':
      pesoLeft += 2
    if i == '?':
      pesoLeft +=3
  pesoRight = 0    
  for j in right:
    if j == '!':
      pesoRight += 2
    if j == '?':
      pesoRight +=3   
  if pesoRight == pesoLeft:
      return 'Balance'
  if pesoLeft > pesoRight:
      return 'Left'
  if pesoLeft < pesoRight:
      return 'Right'