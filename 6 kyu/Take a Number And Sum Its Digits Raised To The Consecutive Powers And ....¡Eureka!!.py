def solution(roman):
  delay = roman[0]
  resultado = 0 
  numeros = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  for i in roman:
    if numeros[i] == numeros[delay]:
      resultado += numeros[i]
    if numeros[i] > numeros[delay]:
      resultado += numeros[i] - numeros[delay] -numeros[delay]
      delay = i
    if numeros[i] < numeros[delay]:
      resultado += numeros[i]
      delay = i
  return resultado