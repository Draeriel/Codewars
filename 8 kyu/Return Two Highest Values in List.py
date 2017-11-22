def two_highest(list):
    print(list)
    if isinstance(list, str):
        return False
    if len(list) < 2:
        return list
    if len(list) >=2:
        n = 0
        for i in list:
            if i >= n :
                n = i     
        nn = 0
        for j in list:
            if j !=  n:
                if j > nn:
                    nn = j        
        lista = [n, nn]
        return lista