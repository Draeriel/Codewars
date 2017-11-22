def elevator_distance(array):
  delay = array[0]
  counter = 0
  for i in array:
    if i == delay:
      delay += 0
    if i > delay:
      counter += i - delay
      delay = i
    if i < delay:
      counter += delay - i
      delay = i
  return counter