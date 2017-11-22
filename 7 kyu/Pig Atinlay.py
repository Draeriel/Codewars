def pig_latin(word):
    if len(word) > 3:
        primera = word[0]
        lista = list(word)
        lista.pop(0)
        lista.append(primera)
        lista.append('ay')
        word =''.join(lista)
    return word