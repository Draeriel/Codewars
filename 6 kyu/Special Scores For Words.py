def find_word(num_let, max_ssw):
  buscador = {}
  resultado = ""
  for palabra in WORD_LIST:
    sww = 0
    if len(palabra) == num_let:
      letras = {}
      for letra in palabra:
        if letra not in letras:
          letras[letra] = 1
        else:
          letras[letra] += 1
        
      for valor in letras.keys():
          sww += letras[valor]*ord(valor)
      buscador[palabra] = sww
      if buscador[palabra] == max_ssw:
        resultado = palabra
  segundoIntento = 0      
  if not resultado:
      for numero in buscador.values():
          
          if numero >= segundoIntento and numero < max_ssw:
            segundoIntento = numero
      lista = []      
      for elemento in buscador.keys():
              if buscador[elemento] == segundoIntento and segundoIntento < max_ssw:
                lista.append(elemento)
      if len(lista) > 0:          
              lista.sort()
              lista = lista[::-1]
              return lista[0]
            
  return resultado or None