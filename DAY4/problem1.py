from functional import seq

numbers = []
bingo_board = []
bingo_boards = []
with open('input.txt', 'r') as f:
  for line in f:
    if ',' in line:
      numbers = [int(l) for l in line.split(',')]
    elif line.strip():
      # read a bingo board
      if len(bingo_board) == 5:
        bingo_boards.append(bingo_board)
        row = (
          seq(line.strip().split(' '))
            .filter(lambda l: l)
            .map(lambda l: int(l))
        ).to_list()
        bingo_board = []
        bingo_board.append(row)
    
      else:

        row = (
          seq(line.strip().split(' '))
            .filter(lambda l: l)
            .map(lambda l: int(l))
        ).to_list()
        bingo_board.append(row)

  bingo_boards.append(bingo_board)

def mark_position(bingo_board, current_bingo_board, number):
  for i in range(len(bingo_board)):
    for j in range(len(bingo_board[i])):
      if bingo_board[i][j] == number:
        current_bingo_board[i][j] = True
        # Check if there is a win here
        if all(current_bingo_board[i]) or all(current_bingo_board[j]):
          return number, bingo_board, current_bingo_board

def mark_positions(bingo_boards, current_bingo_boards, number):
  for i, bingo_board in enumerate(bingo_boards):
    current_bingo_board = current_bingo_boards[i]
    marked_data = mark_position(bingo_board, current_bingo_board, number)
    if marked_data:
      return marked_data

def mark_all_positions(bingo_boards, current_bingo_boards, numbers):
  for number in numbers:
    marked_data = mark_positions(bingo_boards, current_bingo_boards, number)
    if marked_data:
      return marked_data

def sum_unmarked_positions(bingo_board, marked_bingo_board):
  result = 0

  for i in range(len(marked_bingo_board)):
    for j in range(len(marked_bingo_board[i])):
      if not marked_bingo_board[i][j]:
        result += bingo_board[i][j]

  return result

def get_final_score(bingo_boards, current_bingo_boards, numbers):
  marked_number, winning_bingo_board, winning_marked_bingo_board = mark_all_positions(bingo_boards, current_bingo_boards, numbers)
  unmarked_sum = sum_unmarked_positions(winning_bingo_board, winning_marked_bingo_board)
  return marked_number * unmarked_sum

if __name__ == '__main__':
  current_bingo_boards = (
    seq(bingo_boards)
      .map(
        lambda b:
          seq(b)
            .map(lambda r: list(map(lambda _: False, r)))
            .to_list()
        )
      .to_list()
  )
  # print(numbers)
  # print(current_bingo_boards)
  # print(bingo_boards)
  # print(bingo_boards[2])
  # print(mark_positions(bingo_boards, current_bingo_boards, 7))
  print(get_final_score(bingo_boards, current_bingo_boards, numbers))
  