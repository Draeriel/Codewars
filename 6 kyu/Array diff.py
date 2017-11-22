def array_diff(a, b):
    for i in b:
      if i in a:
        a.remove(i)
    for i in b:
      if i in a:
        a.remove(i)    
    return a