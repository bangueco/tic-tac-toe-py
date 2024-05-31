from logic import Game
class Player:
  def __init__(self, name:str, marker:str):
    self.name = name
    self.marker = marker

  def place_marker(self, position):
    Game.gameboard[position] = self.marker
    return