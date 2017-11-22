def goodVsEvil(good, evil):
  poderDelBien = 0
  contadorHeroe=0
  ejercito = ""
  reclutasDelBien=[]
  for bueno in good:
    if bueno.isdigit():
      ejercito += bueno
    else:
      reclutasDelBien.append(ejercito)
      ejercito = ""
  reclutasDelBien.append(ejercito)    
  for heroe in reclutasDelBien:
      heroe = int(heroe)
      contadorHeroe +=1
      if contadorHeroe == 1:
        poderDelBien += heroe
      if contadorHeroe == 2:
        poderDelBien += heroe*2
      if contadorHeroe == 3 or contadorHeroe ==4:
        poderDelBien += heroe*3
      if contadorHeroe == 5:
        poderDelBien +=heroe*4
      if contadorHeroe ==6:
        poderDelBien += heroe*10
  poderDelMal = 0          
  contadorVillano = 0
  horda = ""
  esbirrosDelMal=[]
  for malo in evil:
    if malo.isdigit():
        horda += malo
    else:
      esbirrosDelMal.append(horda)
      horda = ""
  esbirrosDelMal.append(horda)    
  for villano in esbirrosDelMal:
      villano = int(villano)
      contadorVillano += 1
      if contadorVillano == 1:
        poderDelMal += villano
      if contadorVillano > 1 and contadorVillano < 5:
        poderDelMal += villano*2
      if contadorVillano ==5:
        poderDelMal += villano*3
      if contadorVillano ==6:
        poderDelMal += villano*5
      if contadorVillano ==7:
        poderDelMal += villano*10
  if poderDelMal > poderDelBien:
    return "Battle Result: Evil eradicates all trace of Good"
  if poderDelBien > poderDelMal:
    return "Battle Result: Good triumphs over Evil"
  if poderDelMal == poderDelBien:
    return "Battle Result: No victor on this battle field"