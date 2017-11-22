def invert(lst):
    counter = 0
    lista = lst[:]
    for i in lista:    
          lista[counter]  = i  * -1  
          counter +=1
    return lista