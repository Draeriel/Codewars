def order(sentence):
   counter = 0
   ordenador = 1
   lista = sentence.split()
   orden = []
   while counter < len(lista):
     for palabra in lista:
       for letra in palabra:
         if letra == str(ordenador):
           orden.append(palabra)
           counter +=1
           ordenador +=1
   orden = " ".join(orden)       
   return orden