def display_board(board):
  """
  Display Game Board
  :param board: represents a board
  """
  print(" {} | {} | {} ".format(board['1'], board['2'], board['3']))
  print("-----------")
  print(" {} | {} | {} ".format(board['4'], board['5'], board['6']))
  print("-----------")
  print(" {} | {} | {} ".format(board['7'], board['8'], board['9']))