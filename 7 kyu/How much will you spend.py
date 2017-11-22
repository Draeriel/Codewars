def getTotal(costs, items, tax):
    print(costs, items, tax)
    total = 0
    for i in costs:
        if i in items:
            total += costs[i]
    incremento = tax * total
    total += incremento
    return round(total, 2)