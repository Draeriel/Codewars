def productFib(prod):
  fibonacci1 = 1 
  fibonacci2 = 1
  delay = 0
  counter = 0
  while fibonacci1 < prod:
    delay = fibonacci1
    fibonacci2 += fibonacci1
    fibonacci1 += fibonacci2
    counter += 1
    if fibonacci2 * fibonacci1 == prod:
      return [fibonacci2, fibonacci1, True]
    if fibonacci2 * delay == prod:  
      return [delay, fibonacci2, True]
    if fibonacci2 * fibonacci1 > prod:
        if fibonacci2 * delay > prod:
            return [delay, fibonacci2, False]
        if fibonacci2 < fibonacci1:
          return [fibonacci2, fibonacci1, False]
        if fibonacci2 > finonacci1:
          return [fibonacci1, fibonacci2, False] 