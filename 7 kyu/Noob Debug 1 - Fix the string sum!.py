def add(s1, s2):
    print(s1, s2)
    primero = 0
    for i in s1:
      primero += ord(i)
    segundo = 0  
    for j in s2:
      segundo += ord(j)
    return primero + segundo