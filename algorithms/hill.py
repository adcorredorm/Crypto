import numpy as np

#Only works for 2x2 matrix

def eea(a,b):
  if b == 0: return (a,1,0)
  q = int(a/b)
  (da, xa, ya) = eea(b, a%b)
  return (da, ya, xa - q*ya)

def inv_mod(M, mod=26):
  det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
  euc = eea(det, mod)
  assert det != 0 and euc[0] == 1, 'Matrix is not invertible'
  inv = euc[1]
  return [
    [(M[1][1]*inv)%mod, -(M[0][1]*inv)%mod],
    [-(M[1][0]*inv)%mod, (M[0][0]*inv)%mod] 
  ]

def encrypt(text, key):
  if len(text)%2 != 0: text += 'X'
  key = np.array(key)
  result = ''
  for i in range(0, len(text), 2):
    nums = [ord(text[i])-65, ord(text[i+1])-65]
    for r in (np.array(nums)@key)%26:
      result += chr(r+65)
  return result

def decrypt(text, key):
  inv = np.array(inv_mod(key))
  result = ''
  for i in range(0, len(text), 2):
    nums = [ord(text[i])-65, ord(text[i+1])-65]
    for r in (np.array(nums)@inv)%26:
      result += chr(r+65)
  return result

if __name__ == '__main__':
  text = 'CRYPTOGRAPHY'
  key  = [[11,8],[3,7]]
  result = encrypt(text, key)
  print(result)
  print(decrypt(result, key))