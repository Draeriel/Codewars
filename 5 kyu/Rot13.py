import string
from codecs import encode as _dont_use_this_

def rot13(message):
  print(message)
  resultado = ""
  for caracter in message:
    resto = 0
    if caracter.isalpha():
      if ord(caracter) >= 97 and ord(caracter) <= 122:
        if ord(caracter) - 13 < 97 :
          resto = 13 - (ord(caracter) - 96)
          print(resto)
          resultado += chr(122-resto)
        else:  
          resultado += chr(ord(caracter) -13)
      if ord(caracter) >= 65 and ord(caracter) <= 90:
        if ord(caracter) - 13 < 65:
          resto = 12 - (ord(caracter) - 65)
          resultado += chr(90-resto)
        else:  
          resultado += chr(ord(caracter) -13)    
    else:
      resultado += caracter
  return resultado