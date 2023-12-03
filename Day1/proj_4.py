number: list = [4, 54, 23, 1, 3, 43]
max_value = number[0]
min_value = number[0]

for num in number:
  if num < min_value:
    min_value = num

  if num > max_value:
    max_value = num

print(f'the min value is {min_value}')
print(f'the max value is {max_value}')
