# CREATE TIC TAC TOE FOR 2 PLAYERS

def display_board(board):
	clear_output()
	print(board[1] + '|' +board[2] + '|' +board[3])
	print(board[4] + '|' +board[5] + '|' +board[6])
	print(board[7] + '|' +board[8] + '|' +board[9])

test_board = ['#', 'X','O','X','O','X','O','X','O','X']
display_board(test_board)


def player_input():
	
	marker = ''

	# KEEP ASKING PLAYER 1 to choose X or O

	while marker != 'X' and marker != 'O':
		marker = input('Player 1, choose X or O: ').upper()

	if marker == 'X':

		return ('X','O')
	else:
		return ('X','O')

	# ASSIGN PLAYER 2 , the opposite marker
	player1 = marker

	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'

	return(player1,player2)

import random

def choose_first():

	flip = random.randint(0,1)

	if flip == 0:
		return 'Player 1'
	else:
		return 'Player 2'

def place_marker(board, marker, position):

	board[position] = marker

def win_check(board, mark):

	# WIN TIC TAC TOE?

	# ALL ROWS, and check to see if they all share the same marker?
	(board[1] == mark and board[2] == mark and board[3] ) or
	(board[4] == mark and board[5] == mark and board[6] ) or
	(board[7] == mark and board[8] == mark and board[9] )
	# ALL COLUMNS, check to see if marker matches
	# 2 diagonals, check to see if they match

	win_check(test_board,'X')
	
# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic TAC TOE')

while True:
	
	# PLAY THE GAME
	
	## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
	the_board = [' ']
	player1_marker, player2_marker = player_input()
	
	turn = choose_first()
	print(turn + ' will go first'):
	
	play_game = input('Ready to play? y or n')
	
	if play_game == 'y'
		game_on = True
	else:
		game_on = False
		
	## GAME PLAY
	
	while game_on:
		
		if turn == 'Player 1':
			
			# Show the board
			display_board(the_board)
			# Choose a position
			position = player_choice(the_board)
			# Place the marker on the position
			place_marker(the_board, player1_marker, position)

			# Check if they won
			if win_check(the_board, player1_marker):
			    display_board(the_board)
			    print('PLAYER 1 HAS WON!!')
			    game_on = False
			 else:
			    if full_board_check(the_board):
			        display_board(the_board)
			        print("TIE GAME!")
			        game_on = False
			     else:
			        turn = 'Player 2'
		else:
			# Show the board
			display_board(the_board)
			# Choose a position
			position = player_choice(the_board)
			# Place the marker on the position
			place_marker(the_board, player2_marker, position)

			# Check if they won
			if win_check(the_board, player2_marker):
			    display_board(the_board)
			    print('PLAYER 2 HAS WON!!')
			    game_on = False
			 else:
			    if full_board_check(the_board):
			        display_board(the_board)
			        print("TIE GAME!")
			        game_on = False
			     else:
			        turn = 'Player 1'
			# Check if there is a tie
			
			# No ties and and no win? Then next player's turn
if not replay():
	break
# BREAK OUT THE WHILE LOOP on replay()

		
	
	
