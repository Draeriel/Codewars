def solution(n):
   unidades = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8: 'VIII', 9:'IX'}
   decenas = {10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70: 'LXX', 80:'LXXX',           90:'XC'}
   centenas = {100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600: 'DC', 700:'DCC', 800:'DCCC', 900:'CM'}
   miles = {1000:'M', 2000:'MM', 3000:'MMM'}
   if n in miles:
     return miles[n]
   if len(str(n)) == 1:
     return unidades[n]
   if n in range(10,100):
     n = str(n)
     deca = int(n[0]) * 10
     return decenas[deca] + unidades[int(n[1])]
   if n in range(100,1000):
     n = str(n)
     cent = int(n[0]) * 100
     deca = int(n[1]) * 10
     return centenas[cent] + decenas[deca] + unidades[int(n[2])]
   if range(1000,3000):
     n = str(n)
     mil = int(n[0]) * 1000
     cent = int(n[1]) * 100
     deca = int(n[2]) * 10
     return miles[mil] + centenas[cent] + decenas[deca] + unidades[int(n[3])]