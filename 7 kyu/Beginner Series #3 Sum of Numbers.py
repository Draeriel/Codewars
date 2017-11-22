def get_sum(a,b):
      if a > b:
          a,b = b,a
      suma = sum(range(a,b+1))
          
      return suma
print(get_sum(0, -1))