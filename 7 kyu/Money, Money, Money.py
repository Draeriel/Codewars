def calculate_years(principal, interest, tax, desired):
    total = principal
    years = 0
    while total < desired:
      inicial = int(total * interest)
      print(inicial)
      retencion = int(inicial * tax)
      print(retencion)
      total = total + inicial - retencion
      print(total)
      years +=1
    return years 