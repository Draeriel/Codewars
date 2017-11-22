def presses(phrase):
  phrase = phrase.upper()
  counter = 0
  if phrase.isdigit(): 
    for i in phrase:
      if i == '1' or i == '2' or i =='3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        counter += 1
      if i == '0':
        counter += 2
  else:
    for i in phrase:
      if i =='A'or i =='D' or i == 'G' or i == 'J' or i == 'M' or i == 'P' or i == 'T' or i == 'W' or i == ' ' or i == '1' :
        counter += 1
      if i == 'B'or i =='E'or i == 'H'or i == 'K' or i == 'N' or i == 'Q' or i == 'U'or i == 'X' or i == '0':
        counter += 2
      if i == 'C'or i == 'F' or i == 'I' or i == 'L' or i == 'O'or i == 'R' or i == 'Y' or i == 'V':
        counter += 3
      if i == 'S' or i == 'Z':
        counter += 4
      if i == '8' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6':
        counter += 4
      if i == '7' or i == '9':
        counter += 5
      if i == '#' or i == '*':
        counter += 1
  return counter