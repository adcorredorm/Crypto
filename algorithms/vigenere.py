table = []
for i in range(26):
  table.append([chr(65+(i+j)%26) for j in range(26)])

def encrypt(text, key, t=5):
  result = ''
  for i in range(len(text)):
    if i%t == 0: result += ' '
    result += table[ord(text[i])-65][ord(key[i%len(key)])-65]
  return result[1:]

def decrypt(text, key, t=5):
  result = ''
  for i in range(len(text)):
    if i%t == 0: result += ' '
    index = table[ord(key[i%len(key)])-65].index(text[i])
    result += table[0][index]
  return result[1:] 

if __name__ == '__main__':
  key = 'CRYPTO'
  text = 'THERE IS A SECRET PASSAGE BEHIND THE PICTURE FRAME'
  result = encrypt(text.replace(' ', ''), key, 3)
  print(result)
  print(decrypt(result.replace(' ', ''), key, 3))