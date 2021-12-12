data = []
with open('input.txt', 'r') as f:
  for line in f:
    data.append(line.rstrip())

def build_rows(arr):

  rows = []
  for j in range(len(arr[0])):
    row = ""
    for i in range(len(arr)):
      row += arr[i][j]
    rows.append(row)

  return rows

def get_gamma_rate(arr):
  rows = build_rows(arr)
  gamma_binary = ''

  for row in rows:
    num_ones = row.count('1')
    if num_ones > len(row) // 2:
      gamma_binary += '1'
    else:
      gamma_binary += '0'

  return int(gamma_binary, 2)

def get_epsilon_rate(arr):
  rows = build_rows(arr)
  epsilon_binary = ''

  for row in rows:
    num_ones = row.count('1')
    if num_ones < len(row) // 2:
      epsilon_binary += '1'
    else:
      epsilon_binary += '0'

  return int(epsilon_binary, 2)

def get_power_consumption(arr):
  gamma_rate = get_gamma_rate(arr)
  epsilon_rate = get_epsilon_rate(arr)
  return gamma_rate * epsilon_rate

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
  print(get_power_consumption(data))
