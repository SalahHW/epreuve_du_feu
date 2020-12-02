import sys, os

filename = os.path.basename(sys.argv[0])

if len(sys.argv) < 2:
  print(filename+' require a string as parameter.')
  quit()
elif len(sys.argv) > 2:
  print(filename+' require only one string as parameter.')
  quit()
  
def majuscule_minuscule(string):
  new_string = ''
  i = 0
  for letter_index in range(len(string)):
    if string[letter_index] == ' ':
      new_string += ' '
      continue
    
    if i % 2 == 0:
      new_string += string[letter_index].lower()
      i += 1
    else:
      new_string += string[letter_index].upper()
      i += 1
  return new_string
      
print(majuscule_minuscule(sys.argv[1]))