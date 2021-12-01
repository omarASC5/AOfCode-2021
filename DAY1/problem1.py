data = []
with open('input1.txt', 'r') as f:
  for line in f:
    data.append(int(line))

def find_num_increases(arr):
  if not arr or len(arr) == 0: return 0
  num_increases = 0

  for i in range(1, len(arr)):
    num = arr[i]
    prev_num = arr[i -1]
    if num > prev_num: num_increases += 1

  return num_increases

if __name__ == '__main__':
  print(find_num_increases(data))