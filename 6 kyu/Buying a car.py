def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    diferenciaPrecioCoches = startPriceNew - startPriceOld
    meses = ahorro = 0
    while diferenciaPrecioCoches > ahorro:
      meses += 1
      ahorro += savingperMonth
      if meses % 2 == 0:
          percentLossByMonth += 0.5
      oldCarDevaluation = (startPriceOld * percentLossByMonth)/100
      startPriceOld -= oldCarDevaluation
      newCarDevaluation = (startPriceNew * percentLossByMonth)/100
      startPriceNew -= newCarDevaluation
      diferenciaPrecioCoches = startPriceNew - startPriceOld
      
    sobras = round(ahorro - diferenciaPrecioCoches, 0)
    return [meses, sobras]