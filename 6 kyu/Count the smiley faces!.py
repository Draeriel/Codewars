def count_smileys(arr):
    counter = 0
    for i in arr:
      if i[0] ==":" or i[0] ==";":
          if len(i) == 2:
            if i[1] ==  ")" or i[1] == "D":
                counter += 1
          if len(i) == 3:
            if i[1] == "-" or i[1] == "~" :
              if i[2] == ")" or i[2] == "D":
                counter  += 1
    return counter 