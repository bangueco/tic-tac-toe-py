class Game:
  gameboard = {'0': '', '1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': ''}
  gameBoardWinningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  
  @staticmethod
  def check_for_winner(winningCondition):
    for x in winningCondition:
      print(x)