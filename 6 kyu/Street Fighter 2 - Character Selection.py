def street_fighter_selection(fighters, initial_position, moves):
    print(moves)
    recolector = []
    vertical = initial_position[0]
    horizontal = initial_position[1]
    for direccion in moves:
      if direccion == "up": 
        if vertical == 1:
          vertical -= 1
        recolector.append(fighters[vertical][horizontal])
      if direccion == "down":
        if vertical == 0:
          vertical += 1
        recolector.append(fighters[vertical][horizontal])
      if direccion == "right":
        if horizontal == 5:
          horizontal = 0
        else:
          horizontal += 1
        recolector.append(fighters[vertical][horizontal])
      if direccion == "left":
          if horizontal == 0:
            horizontal = 5
          else:
            horizontal -= 1
          recolector.append(fighters[vertical][horizontal])
    return recolector