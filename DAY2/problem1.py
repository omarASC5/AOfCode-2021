data = []
with open('input.txt', 'r') as f:
  for line in f:
    move = line.strip().split(' ')
    move[-1] = int(move[-1])
    data.append(move)

def find_final_position(moves):
  horizontal_position = 0
  depth = 0

  for move in moves:
    direction, num = move
    if direction == 'forward':
      horizontal_position += num
    elif direction == 'down':
      depth += num
    elif direction == 'up':
      depth -= num

  return horizontal_position * depth

data2 = [
  ['forward', 5],
  ['down', 5],
  ['forward', 8],
  ['up', 3],
  ['down', 8],
  ['forward', 2]
]
if __name__ == '__main__':
  print(find_final_position(data))