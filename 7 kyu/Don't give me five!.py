def dont_give_me_five(start,end):
    counter = 0
    for i in range(start,end+1):
        counter += 1
        i = str(i)
        if "5" in i:
          counter -= 1
    return counter