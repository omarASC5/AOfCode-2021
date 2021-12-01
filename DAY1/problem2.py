from problem1 import find_num_increases

data = []
with open('input1.txt', 'r') as f:
  for line in f:
    data.append(int(line))

def find_num_increases_threes(arr):
  if not arr or len(arr) == 0: return 0
  curr_window_sum = 0
  curr_window_size = 0
  MAX_WINDOW_SIZE = 3
  window_start = 0
  sums = []

  for window_end in range(len(arr)):
    num = arr[window_end]
    curr_window_sum += num
    curr_window_size += 1
    
    if curr_window_size >= MAX_WINDOW_SIZE:
      sums.append(curr_window_sum)
      curr_window_sum -= arr[window_start]
      window_start += 1

  return find_num_increases(sums)

if __name__ == '__main__':
  print(find_num_increases_threes(data))