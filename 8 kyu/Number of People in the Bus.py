def number(bus_stops):
    subida = 0
    bajada = 0
    for i in  bus_stops:
        subida += i[0]
        bajada += i[1]
    return subida - bajada