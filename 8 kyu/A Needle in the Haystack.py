def find_needle(haystack):
     counter = 0
     for i in haystack:
         if i != 'needle':
             counter += 1
         if i == 'needle':
             resultado = 'found the needle at position ' + str(counter)
             return resultado