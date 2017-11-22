def solution(number):
  total = 0
  for i in range(0, number, 3):
    total += i
  for i in range(0, number, 5):
    if i % 3 != 0:
      total += i
  return total