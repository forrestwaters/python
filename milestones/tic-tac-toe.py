import random

players = [1, 2]
players[0] = player_1_marker = 'X'
players[1] = player_2_marker = 'O'
game_finished = False


"""Defining main game board for the game"""
def game_board():
	global board
        board = ['1','2','3','4','5','6','7','8','9']

"""Function to display the current board"""
def display_board():
	print board[0:3]
	print board[3:6]
	print board[6:9]

"""Coin flip to choose which player goes first. Assigns that player a boolean of true and the other player False"""
def coin_flip():
	global player_1_turn
	global player_2_turn
	turn = random.randint(1,2)
	if turn == 1:
		player_1_turn = True
		player_2_turn = False
	else:
		player_1_turn = False
		player_2_turn = True


"""Section where we take players input and place their piece"""
def players_turn():
	if player_1_turn:
		current_player = players[0]
	else:
		current_player = players[1]
	global board
	global players_choice
	if current_player == 'X':
		print "Player 1's turn!"
	else:
		print "Player 2's turn!"
	players_choice = raw_input("Please select an open space: ")
	if players_choice.isdigit():
		if 0 < int(players_choice) < 10:
			for index in range(len(board)):
				board_spaces = board[index]
				if players_choice == board_spaces:
					board = [w.replace(players_choice, current_player) for w in board]

		else:
			try_again()
	else:
		try_again()

"""Starts over with players_turn if the wrong value is provided"""
def try_again():
	print "Oops, try again."
	players_turn()

"""Checks to see if someone has won or if the board is full"""
def status_check():
	l = [player_1_marker, player_2_marker]
	global player
	for player in l:
		global game_finished
		game_finished = True
		if board[0] == board[1] == board[2] == player:
			congrats()
			break
		elif board[3] == board[4] == board[5] == player:
			congrats()
			break
		elif board[6] == board[7] == board[8] == player:
			congrats()
			break
		elif board[0] == board[3] == board[6] == player:
			congrats()
			break
		elif board[1] == board[4] == board[7] == player:
			congrats()
			break
		elif board[2] == board[5] == board[8] == player:
			congrats()
			break
		elif board[0] == board[4] == board[8] == player:
			congrats()
			break
		elif board[2] == board[4] == board[6] == player:
			congrats()
			break
		else:
			game_finished = False

def congrats():
	display_board()
	print "Congrats!"
	if player_1_turn:
		print "Player 1 wins!"
	else:
		print "Player 2 wins!"


game_board()
coin_flip()
print "Welcome to Tic Tac Toe"
if player_1_turn:
	print "Player 1 will go first!"
else:
	print "Player 2 will go first!"

while game_finished == False:
	display_board()
	players_turn()
	status_check()
	player_1_turn = not player_1_turn
	player_2_turn = not player_2_turn
