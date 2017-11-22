def cube_odd(arr):
  odd = 0
  for i in arr:
    if i not in range(-9999, 9999):
      return None
    i = i**3
    if i % 2 != 0:
        odd += i
        
  
  return odd