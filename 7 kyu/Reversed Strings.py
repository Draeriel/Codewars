def solution(string):
  invert = ''
  for i in string:
    invert = i + invert
  return invert  