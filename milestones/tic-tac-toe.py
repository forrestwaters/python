def game_board():
	global board
        board = ['1','2','3','4','5','6','7','8','9']
def display_board():
	print board[0:3]
	print board[3:6]
	print board[6:9]

game_board()

display_board()
