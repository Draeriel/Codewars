def queue_time(customers, n):
    if not customers :
        return 0
        
    clientes = len(customers) 
    if clientes <= n:
        total = 0
        for i in customers:
            if total < i:
                total = i
        return total
                
    if n == 1:
        return sum(customers)
    time = 0
    suma = []
    cajasLlenas = 0
    
    if clientes > n:
            for i in customers:
                if cajasLlenas < n:
                    suma.append(i)
                    cajasLlenas += 1
                    clientes -=1
                    print(suma)
                if cajasLlenas == n:
                    resta = suma[0]
                    for j in suma:
                        if j < resta and clientes >= 1:
                            resta = j
                            
                        if j > resta and clientes == 0: 
                            resta = j
                            
                    for k in range(n):
                          suma[k] -= resta
                    
                    
                    
                    time += resta
                    print(suma)
                    print(resta)
                    print(time)
                    suma.remove(0)
                    cajasLlenas -= 1 
                    resta = suma[0]
                            
    return(time)