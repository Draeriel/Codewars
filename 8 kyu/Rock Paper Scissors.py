player1 = 'Player 1 won!'
player2 = 'Player 2 won!'
def rps(p1, p2):
    while p1 == p2:
      return 'Draw!'
      break
    while p1 == 'rock' and p2 == 'scissors':
      return player1
      break
    while p1 == 'scissors' and p2 == 'paper':
      return player1
      break
    while p1 == 'paper' and p2 == 'rock':
      return player1
      break
    while p2 == 'rock' and p1 == 'scissors':
      return player2
      break
    while p2 == 'scissors' and p1 == 'paper':
      return player2
      break
    while p2 == 'paper' and p1 == 'rock':
      return player2
      break