def disemvowel(string):
    vowels = 'aeiouAEIOU'
    for i in vowels:
          string = string.replace(i, "")
          print(string)
    return string
    