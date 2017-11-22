def findSmallestInt(arr):
  menor = 9999
  for i in arr:
    if i < menor:
      menor = i
  return menor