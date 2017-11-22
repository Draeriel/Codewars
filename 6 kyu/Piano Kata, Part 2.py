def which_note(key_press_count):
  notas = ["X","A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
  while key_press_count > 88:
    key_press_count -= 88
  while key_press_count > 12:
    key_press_count -= 12
  return notas[key_press_count]