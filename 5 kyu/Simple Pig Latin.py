def pig_it(text):
  palabra = []
  frase = ""
  for letra in text:
    if letra != " ":
      palabra.append(letra)
    if letra == " ":
      palabra = palabra[1:] + list(palabra[0])
      frase += "".join(palabra) + "ay" + " "
      palabra = []
  if len(palabra) > 1:
      palabra = palabra[1:] + list(palabra[0])
      frase += "".join(palabra) + "ay"
  if len(palabra) == 1:
      palabra = palabra[1:] + list(palabra[0])
      frase += "".join(palabra)    
  return frase 