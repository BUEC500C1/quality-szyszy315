import inttoroma

def test():
  if inttoroma.intToRoman(1) != 'I':
    return False
  if inttoroma.intToRoman(4) != 'IV':
    return False
  if inttoroma.intToRoman(10) != 'X':
    return False
  if inttoroma.intToRoman(40) != 'XL':
    return False
  if inttoroma.intToRoman(400) != 'CD':
    return False
  if inttoroma.intToRoman(500) != 'D':
    return False
  if inttoroma.intToRoman(900) != 'CM':
    return False
  if inttoroma.intToRoman(3000) != 'MMM':
    return False
  if inttoroma.intToRoman(3111) != 'MMMCXI':
    return False
  return True
