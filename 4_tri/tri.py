import sys, os

filename = os.path.basename(sys.argv[0])

if len(sys.argv) < 3:
  print(filename+' require at list two integer as argument.')
  quit()

sys.argv.pop(0)
user_number_list = [int(number) for number in sys.argv]

def tri_decroissant(number_list):
  decroissant = False
  while decroissant == False:
    decroissant = True
    for number_index in range(len(number_list) - 1):
      if number_list[number_index] < number_list[number_index + 1]:
        temp_number = number_list[number_index + 1]
        number_list[number_index + 1] = number_list[number_index]
        number_list[number_index] = temp_number
        decroissant = False
  return number_list      
        
for number in tri_decroissant(user_number_list):
  print(number, end=' ')
print()
