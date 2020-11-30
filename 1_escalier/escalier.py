import sys

if len(sys.argv) < 1:
  print(__file__+' require at least one parameter.')
  exit
elif len(sys.argv) > 1:
  print(__file__+' require only one parameter.')
  exit

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