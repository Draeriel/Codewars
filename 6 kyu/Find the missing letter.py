def find_missing_letter(chars):
    delay = 0
    for i in chars:
      if i == chars[0]:
        delay = int(ord(i))
      else:
        if int(ord(i)) - delay != 1:
          return chr(delay + 1)
        else:
          delay = int(ord(i))