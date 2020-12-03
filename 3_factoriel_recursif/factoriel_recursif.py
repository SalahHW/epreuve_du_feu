import sys, os

filename = os.path.basename(sys.argv[0])

if len(sys.argv) < 2:
  print(filename+' require at least one parameter.')
  quit()
elif len(sys.argv) > 2:
  print(filename+' require only one parameter.')
  quit()

def factoriel(nombre):
  factoriel = 1
  for n in range(1, nombre + 1):
    factoriel = n * factoriel
  return factoriel

print(factoriel(int(sys.argv[1])))