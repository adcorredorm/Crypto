table = {}
for i in range(26):
  table[chr(i+65)] = i
  table[i] = chr(i+65)

def cifrate(text, key):
  result = ''
  for i in range(len(text)):
    result += table[(table[text[i]] + table[key[i]])%26]
  return result

def decifrate(text, key):
  result = ''
  for i in range(len(text)):
    result += table[(table[text[i]] - table[key[i]])%26]
  return result

number_table = {
   '0':'A', '1':'T',          '3':'O', '4':'N', '5':'E',          '7':'S', '8':'I', '9':'R',
  '20':'B','21':'C','22':'D','23':'F','24':'G','25':'H','26':'J','27':'K','28':'L','29':'M',
  '60':'P','61':'Q','62':'U','63':'V','64':'W','65':'X','66':'Y','67':'Z','68':'.','69':' '
}

for k,v in number_table.copy().items():
  number_table[v] = k

def to_number(source):
  text = ''
  for c in source:
    text += number_table[c]
  return text

def to_text(source):
  cummulate = ''
  text = ''
  for c in source:
    cummulate += c
    if cummulate in number_table:
      text += number_table[cummulate]
      cummulate = ''
  return text

def cifrate_mod10(source, key):
  result = ''
  for i in range(len(source)):
    if source[i] != " ":
      result += str( (int(source[i]) - int(key[i]))%10 )
  return result

def decifrate_mod10(source, key):
  result = ""
  for i in range(len(source)):
    if source[i] != " ":
      result += str( (int(source[i]) + int(key[i]))%10 )
  return result


if __name__ == '__main__':
  text = 'CRYPTOGRAPHY'
  key  = 'YHPARGOTPYRC'
  result = cifrate(text, key)
  print(result)
  print(decifrate(result, key))

  print()

  num = to_number(text)
  num_key = to_number(key)
  num_result = cifrate_mod10(num, num_key)
  print(to_text(num_result))
  print(to_text(decifrate_mod10(num_result, num_key)))