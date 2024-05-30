from os import system, name
from classes import Player
from validation_message import *
from logic import display_board

gameboard = {'1': '', '2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}

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
      display_invalid_input_msg()

def startMenu():
  markers = {'x', 'o'}
  print('-------------- Tic Tac Toe --------------')
  print('--------------  Start Menu  --------------')
  
  while True:
    player1Name = input('Enter player1 name: ').strip()

    if player1Name:
      break
    else:
      display_name_validation_msg()

  while True:
    player1Marker = input('Enter player1 marker: ').strip().lower()

    if player1Marker not in markers:
      display_marker_validation_msg()
    else:
      break

  while True:
    player2Name = input('Enter player2 name: ').strip()

    if player2Name:
      break
    elif player2Name == player1Name:
      display_name_taken_msg()
    else:
      display_name_validation_msg()
  
  while True:
    player2Marker = input('Enter player2 marker: ').strip().lower()

    if player2Marker not in markers:
      display_marker_validation_msg()
    elif player2Marker == player1Marker:
      display_marker_taken_msg()
    else:
      break
    
  clear()
  display_board(gameboard)
  

mainMenu()