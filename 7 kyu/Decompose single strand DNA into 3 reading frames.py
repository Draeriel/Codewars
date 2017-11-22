def decompose_single_strand(single_strand):
  frame1 = ""
  counter = 0
  for letra in single_strand:
    if counter < 3:
      frame1 += letra
      counter +=1
    if counter == 3:
      frame1 += " "
      counter = 0
  frame1 = frame1.rstrip()     
  frame1.rstrip(" ")
  frame2 = ""
  counter = 0
  for letra in single_strand:
    if counter > 0 and counter < 4:
      frame2 += letra
      counter +=1
    if counter == 4:
      frame2 += " "
      counter = 1
    if counter == 0:
      frame2 = letra + " "
      counter += 1  
  frame3 = ""
  counter = 0
  for letra in single_strand:
    if counter >1 and counter <5:
      frame3 += letra
      counter +=1
    if counter == 5:
      frame3 += " "
      counter =2
    if counter ==1:
      frame3 += letra + " "
      counter += 1    
    if counter == 0:
      frame3 += letra
      counter = 1
    
  return "Frame 1: " + frame1 + "\nFrame 2: " + frame2 + "\nFrame 3: " + frame3  
    return True 