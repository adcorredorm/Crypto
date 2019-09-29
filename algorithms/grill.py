import numpy as np

def make_grill(size, holes):
  grill = np.zeros((size, size), dtype=bool)
  for hole in holes:
    grill[hole] = True
  return grill

def rotate(grill, rot):
  return np.rot90(grill, rot)

def encrypt(text, size, holes, reverse=False):
  grill = make_grill(size, holes)
  box = [['' for _ in range(size)] for _ in range(size)]
  text = text.replace(' ', '')

  if reverse: rotations = range(4, 0, -1)
  else: rotations = range(4)

  counter = 0
  for k in rotations:
    rotation = rotate(grill, k)
    for i in range(size):
      for j in range(size):
        if rotation[i][j] and box[i][j] == '':
          box[i][j] = text[counter]
          counter += 1
  
  result = ''
  for i in range(size):
      for j in range(size):
        result += box[i][j]
      result += ' '
  return result

def decrypt(text, size, holes, reverse=False):
  grill = make_grill(size, holes)
  box = [['' for _ in range(size)] for _ in range(size)]
  text = text.replace(' ', '')

  counter = 0
  for i in range(size):
    for j in range(size):
      box[i][j] = text[counter]
      counter += 1

  if reverse: rotations = range(4, 0, -1)
  else: rotations = range(4)

  result = ''
  for k in rotations:
    rotation = rotate(grill, k)
    for i in range(size):
      for j in range(size):
        if rotation[i][j] and box[i][j] != '':
          result += box[i][j]
          box[i][j] = ''
    result += ' '
  return result


if __name__ == '__main__':
  grille_size = 4
  text = 'JIM ATTACKS AT DAWN'
  holes = [(0,0), (2,1), (2,3), (3,2)]
  
  result = encrypt(text, grille_size, holes)
  print(result)
  print(decrypt(result, grille_size, holes))
  