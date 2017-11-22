def sum_two_smallest_numbers(numbers):
  counter1 = numbers[0]
  counter2 = numbers[1]
  for i in numbers:
    if i < counter1 or i < counter2:
      if counter1 < counter2 and i < counter2 and counter1 != i:
        counter2 = i
      if counter2 < counter1 and i < counter1 and counter2 != i:
        counter1 = i
  total = counter1 + counter2
  return total