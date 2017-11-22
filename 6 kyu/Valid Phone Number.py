def validPhoneNumber(phoneNumber):
  contador = 0
  for numero in phoneNumber:
    if numero.isdigit():
      contador += 1
    if numero.isalpha():
      return False
  if phoneNumber[0] == "(":
    contador += 1
  if phoneNumber[4] == ")":
    contador += 1
  if phoneNumber[5] == " ":
    contador += 1
  if phoneNumber[9] == "-":
    contador += 1
  if contador == 14:
    return True
  else: 
    return False