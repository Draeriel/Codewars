def alphabet_position(text):
    valor = ''
    for letra in text:
      letra = letra.lower()
      if letra.isalpha():
          valor  +=  str(ord(letra)-96)
          valor += ' '
    return valor[:-1]    