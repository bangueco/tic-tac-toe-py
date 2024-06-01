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
  def check_for_winner():
    for row in Game.gameBoardWinningConditions:
      if Game.gameboard[str(row[0])] != '' and Game.gameboard[str(row[0])] == Game.gameboard[str(row[1])] == Game.gameboard[str(row[2])]:
        return True