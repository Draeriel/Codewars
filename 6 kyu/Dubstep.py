def song_decoder(song):
  wub = ""
  cancion = ""
  contador = 0
  espacios = 0
  portero = 0
  for letra in song:
    portero += 1
    if letra == "W" and song[portero]== "U":
      if contador > 0:
        cancion += wub
        contador = 0
      contador += 1
      wub += letra
    elif letra == "U" and contador == 1:
          wub += "U"
          contador += 1
    elif letra == "B" and contador == 2:
          wub += "B"
          wub = ""
          contador = 0
          if espacios == 0:
            cancion += " "
            espacios += 1
    else:
        cancion += wub
        wub = ""
        cancion += letra
        contador = 0
        espacios = 0
  return cancion.strip()