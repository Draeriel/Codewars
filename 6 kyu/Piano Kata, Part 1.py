def black_or_white_key(key_press_count):
  white = [1,3,4,6,8,9,11]
  black = [2,5,7,10,12]
  while key_press_count > 88:
    key_press_count -= 88
  while key_press_count > 12:
    key_press_count -= 12
  if key_press_count in white:
    return "white"
  else:
    return "black"