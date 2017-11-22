def reverse_words(str):
  recolector = [""]
  palabra = [""]
  for i in str:
      if str != " ":
          palabra += i
      if i == " ":
          palabra = "".join(palabra[::-1])
          print(palabra)
          recolector += palabra
          palabra = [""]
  print(palabra)        
  if len(palabra) != 0:        
      palabra = "".join(palabra[::-1])
      print(palabra)
      recolector += " " +  palabra
      palabra = [""]   
  
  return "".join(recolector).lstrip()