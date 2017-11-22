def solve(s):
    print(s)
    numero = ""
    counter = 0
    recolector = []
    for valor in s:
        if valor.isdigit():
                numero = numero + valor
        if valor.isalpha() and len(numero) >= len(valor):
                recolector.append(int(numero))
                numero = ""
    if len(numero) >= 1:            
        recolector.append(int(numero))
    return max(recolector)