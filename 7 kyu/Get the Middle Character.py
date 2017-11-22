def get_middle(s):
    largo = len(s)
    if largo <= 2:
      return s
    if largo > 2:
      return get_middle(s[1:-1])