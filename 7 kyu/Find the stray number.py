def stray(arr):
    contador = arr[0]
    delay = 0
    counter = 0
    for i in arr:
        if i == contador:
            counter += 1
        if i != contador:
            delay = i
    if counter <= 1:
        return contador
    else:
        return delay
