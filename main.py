target = int(input()) # Enter a number between 0 and 1000

even = 0
for number in range(2, target+1, 2):
  even += number
  
print(even)