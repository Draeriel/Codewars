def is_zero_balanced(arr):
    if not arr:
      return False
    for i in arr:
      
          suma = sum(arr)
          
          if suma == 0:
              for i in range(0, len(arr)):
                rastreator = i
                rastreator = rastreator * -1
                for i in arr:
                  arr = str(arr)
                  rastreator = str(rastreator)
                  alfa = arr.find(rastreator)
                  if alfa == 1:
                      return True
                  else:
                      return False
              return True
          if suma != 0:
              return False 