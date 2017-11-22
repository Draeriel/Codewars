def camel_case(string):
  lista = []
  counter = 0
  for letra in string:
    if not letra.isalpha():
      counter += 1
    else:
      
      if counter == 0:
        if lista == []:
          lista += letra.capitalize()
        else:
          lista += letra.lower()
      if counter == 1:
        counter = 0
        lista += letra.capitalize()
  return "".join(lista)  