from os import system, name
from classes import Player
from logic import Game
from validation_message import *
import random

player1 = ''
player2 = ''

def display_board(board):
  """
  Display Game Board
  :param board: represents a board
  """
  print(" {} | {} | {} ".format(board['0'], board['1'], board['2']))
  print("-----------")
  print(" {} | {} | {} ".format(board['3'], board['4'], board['5']))
  print("-----------")
  print(" {} | {} | {} ".format(board['6'], board['7'], board['8']))

def clear():
    
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def mainMenu():
  while True:
    print('-------------- Tic Tac Toe --------------')
    print('--------------  Main Menu  --------------')
    print(' 1. Start')
    print(' 2. Exit')
    choice = input('>>> ')

    if choice == '1':
      clear()
      startMenu()
    elif choice == '2':
      break
    else:
      ValidationMessages.display_invalid_input_msg()

def startMenu():
  markers = {'x', 'o'}
  print('-------------- Tic Tac Toe --------------')
  print('--------------  Start Menu  --------------')
  
  while True:
    player1Name = input('Enter player1 name: ').strip()

    if player1Name:
      break
    else:
      ValidationMessages.display_name_validation_msg()

  while True:
    player1Marker = input('Enter player1 marker: ').strip().lower()

    if player1Marker not in markers:
      ValidationMessages.display_marker_validation_msg()
    else:
      break

  while True:
    player2Name = input('Enter player2 name: ').strip()

    if not player2Name:
      ValidationMessages.display_name_validation_msg()
    elif player2Name == player1Name:
      ValidationMessages.display_name_taken_msg()
    else:
      break
  
  while True:
    player2Marker = input('Enter player2 marker: ').strip().lower()

    if player2Marker not in markers:
      ValidationMessages.display_marker_validation_msg()
    elif player2Marker == player1Marker:
      ValidationMessages.display_marker_taken_msg()
    else:
      break
  
  # Set player infos
  global player1, player2
  player1 = Player(player1Name, player1Marker)
  player2 = Player(player2Name, player2Marker)

  clear()
  gameMenu()

def gameMenu():
  # random turns between 1 and 2
  turns = random.randint(1, 2)
  roundWin = False
  while roundWin == False:
    display_board(Game.gameboard)
    if turns == 1:
      print('It\'s player 1 turns')
      print('pick a move between 0-8')
      while True:
        player1Move = input('>>> ')

        if Game.gameboard.get(player1Move):
          ValidationMessages.display_board_taken_msg()
        else:
          player1.place_marker(player1Move)
          turns = 2
          break

    else:
      print('It\'s player 2 turns')
      print('pick a move between 0-8')

      while True:
        player2Move = input('>>> ')

        if Game.gameboard.get(player2Move):
          ValidationMessages.display_board_taken_msg()
        else:
          player2.place_marker(player2Move)
          turns = 1
          break

mainMenu()