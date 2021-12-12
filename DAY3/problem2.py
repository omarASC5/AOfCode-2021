from problem1 import build_rows

data = []
with open('input.txt', 'r') as f:
  for line in f:
    data.append(line.rstrip())

def get_oxygen_generator_rating(arr):
  result = arr[:]

  i = 0
  while i < len(arr[0]) and len(result) > 1:
    rows = build_rows(result)
    row = rows[i]
    num_ones = row.count('1')
    num_zeroes = row.count('0')

    if num_zeroes <= num_ones:
      # Keep the bit strings starting with ones
      result = list(filter(lambda r: r[i] == '1', result))
    else:
      # Keep the bit strings starting with zeroes
      result = list(filter(lambda r: r[i] == '0', result))
  
    i += 1

  return int(result[0], 2)

def get_co2_scrubber_rating(arr):
  result = arr[:]

  i = 0
  while i < len(arr[0]) and len(result) > 1:
    rows = build_rows(result)
    row = rows[i]
    num_ones = row.count('1')
    num_zeroes = row.count('0')

    if num_zeroes <= num_ones:
      # Keep the bit strings starting with zeroes
      result = list(filter(lambda r: r[i] == '0', result))
    else:
      # Keep the bit strings starting with ones
      result = list(filter(lambda r: r[i] == '1', result))
  
    i += 1

  return int(result[0], 2)

def get_life_support_rating(arr):
  oxygen_generator_rating = get_oxygen_generator_rating(arr)
  co2_scrubber_rating = get_co2_scrubber_rating(arr)
  return oxygen_generator_rating * co2_scrubber_rating

if __name__ == '__main__':
  data2 = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
  ]
  print(get_life_support_rating(data))