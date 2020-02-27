import inttoroma
import pytest

def test_romaint():
  assert inttoroma.intToRoman(1) == 'I'
  assert inttoroma.intToRoman(4) == 'IV'
  assert inttoroma.intToRoman(10) == 'X'
  assert inttoroma.intToRoman(40) == 'XL'
  assert inttoroma.intToRoman(400) == 'CD'
  assert inttoroma.intToRoman(500) == 'D'
  assert inttoroma.intToRoman(900) == 'CM'
  assert inttoroma.intToRoman(3000) == 'MMM'
  assert inttoroma.intToRoman(3111) == 'MMMCXI'
  assert inttoroma.intToRoman("abc") == "not supported input"
  assert inttoroma.intToRoman(2.2) == "not supported input"
