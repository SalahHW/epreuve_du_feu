import sys, os

filename = os.path.basename(sys.argv[0])

if len(sys.argv) < 2:
  print(filename+' require at least one parameter.')
  quit()
elif len(sys.argv) > 2:
  print(filename+' require only one parameter.')
  quit()

print(len(sys.argv))

number_of_steps = int(sys.argv[1])
print('Your stair will have '+ str(number_of_steps) + ' steps :')

line = 1
while line <= number_of_steps:
  number_of_space = number_of_steps - line
  for space in range(number_of_space):
    print(' ', end='')
  for sharp in range(line):
    print('#', end='')
  print('')
  line += 1