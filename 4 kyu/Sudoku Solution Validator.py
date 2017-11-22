def validSolution(board):
    cuadrante1 = []
    cuadrante2 = []
    cuadrante3 = []
    cuadrante4 = []
    cuadrante5 = []
    cuadrante6 = []
    cuadrante7 = []
    cuadrante8 = []
    cuadrante9 = []
    listaOrdenada = [1,2,3,4,5,6,7,8,9]
    for orden in range(len(board)):
        comprobadorColumna = []
        for columna in board:
          if columna[orden] in comprobadorColumna:
              return False
              comprobadorColumna = []
          if columna[orden] not in comprobadorColumna:
              comprobadorColumna.append(columna[orden])
        if orden < 3 :
          cuadrante1.append(board[0][int(orden)])
          cuadrante1.append(board[1][int(orden)])
          cuadrante1.append(board[2][int(orden)])
          cuadrante4.append(board[3][int(orden)])
          cuadrante4.append(board[4][int(orden)])
          cuadrante4.append(board[5][int(orden)])
          cuadrante7.append(board[6][int(orden)])
          cuadrante7.append(board[7][int(orden)])
          cuadrante7.append(board[8][int(orden)])
        if orden >=3 and orden < 6:
          cuadrante2.append(board[0][int(orden)])
          cuadrante2.append(board[1][int(orden)])
          cuadrante2.append(board[2][int(orden)])
          cuadrante5.append(board[3][int(orden)])
          cuadrante5.append(board[4][int(orden)])
          cuadrante5.append(board[5][int(orden)])
          cuadrante8.append(board[6][int(orden)])
          cuadrante8.append(board[7][int(orden)])
          cuadrante8.append(board[8][int(orden)])
        if orden >= 6:
          cuadrante3.append(board[0][int(orden)])
          cuadrante3.append(board[1][int(orden)])
          cuadrante3.append(board[2][int(orden)])
          cuadrante6.append(board[3][int(orden)])
          cuadrante6.append(board[4][int(orden)])
          cuadrante6.append(board[5][int(orden)])
          cuadrante9.append(board[6][int(orden)])
          cuadrante9.append(board[7][int(orden)])
          cuadrante9.append(board[8][int(orden)])
    if listaOrdenada != sorted(cuadrante1) or listaOrdenada != sorted(cuadrante2) or listaOrdenada != sorted(cuadrante3) or listaOrdenada != sorted(cuadrante4) or listaOrdenada != sorted(cuadrante5) or listaOrdenada != sorted(cuadrante6) or listaOrdenada != sorted(cuadrante7) or listaOrdenada != sorted(cuadrante8) or listaOrdenada != sorted(cuadrante9) :
      return False
    for fila in board:
        comprobadorFila = []
        for numero in fila:
          if numero in comprobadorFila:
            return False
          if numero not in comprobadorFila:
            comprobadorFila.append(numero)
    return True 