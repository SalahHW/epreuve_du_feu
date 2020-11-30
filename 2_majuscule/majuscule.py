import sys, os

filename = os.path.basename(sys.argv[0])

if len(sys.argv) < 2:
  print(filename+' require a string as parameter.')
  quit()
elif len(sys.argv) > 2:
  print(filename+' require only one string as parameter.')
  quit()