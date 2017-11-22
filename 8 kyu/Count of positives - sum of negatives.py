def count_positives_sum_negatives(arr):
    if arr == []:
        return arr
    max =len(arr)
    contpos= 0
    contneg= 0
    position =0
    while position < max:
        if arr[position] > 0:
            position = position + 1
            contpos =contpos + 1
        
        elif arr[position] < 0:
            contneg = contneg + arr[position]
            position = position +1
        
        elif arr[position] == 0:
            position = position + 1
    return [contpos, contneg] 