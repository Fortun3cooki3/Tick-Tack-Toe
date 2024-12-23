def user_choice ():
    """validating user input for TTT. input must be a number between 1 and 9"""
    choice = 'Wrong' # == False for number
    while not choice.isdigit() or choice not in ['1','2','3','4','5','6','7','8','9']: #checks if input == number and list
        choice = input('please choose a number between 1 and 9: ')
        if not choice.isdigit() or choice not in ['1','2','3','4','5','6','7','8','9']: #error message
            print('Sorry that is invalid')

    return int(choice) #returns number

def x_o ():
    """choosing between x or o in lower"""
    choice_x_or_y = ''
    while choice_x_or_y not in ['x','o']:
        choice_x_or_y = input('choose between x or o: ').lower()
        if choice_x_or_y not in ['x','o']:
            print('invalid choice')
    return choice_x_or_y #returns a x or o

def display_board(board):
    """displays the board of TTT, takes in argument the board list """
    return(f' {board[1]} | {board[2]} | {board[3]}\n'
          f'---|---|---\n'
          f' {board[4]} | {board[5]} | {board[6]}\n'
          f'---|---|--- \n'
          f' {board[7]} | {board[8]} | {board[9]}')

def new_board(board, place, x_y):
    """takes in board list and changes empty string into x or o"""
    board[place] = x_y
    return board

def board_full_check(board):
    """uses a set to check if the board is full or not"""
    if set(board) == {'not use','x','o'}:
        return True
    else:
        return False

def place_taken(board, place):
    """of place is already in use check"""
    if board[place] in ['x','o']:
        return True
    else:
        return False

def win_check(board):
    """win check by checking a list with possible wins. using a for in statement to check per sub list item."""
    win_combination = [
        [1,2,3], #top
        [4,5,6], #mid
        [7,8,9], #bot
        [1,4,7], #top left
        [2,5,8], #mid left
        [3,6,9], #bot left
        [1,5,9], #diagonal
        [3,5,7]  #counter diagonal

    ]
    for combo in win_combination:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

def restart():
    restart_yes_no = 'wrg'
    while restart_yes_no not in ['y','n']:
        restart_yes_no = (input('do you want to play again y/n ?: ').lower())
    if restart_yes_no not in ['y','n']:
        print('invalid choice')
    return restart_yes_no == 'y'



# player_choice = user_choice()
# x_or_o = x_o()
# change_board = new_board(nummer_board, player_choice, x_or_y)
# the_board = display_board(change_board)
# full_check = board_full_check(the_board)
# place_taken_check = place_taken(the_board, player_choice)
# who_won = win_check(the_board)

def tick_tack_toe():
    """ this is the main game loop"""
    win = False #when true game ends or restarts

    print('welcome to Tick_Tack_Toe \nplayer 1 choose your weapon')

    # gives x and o to player 1 and 2
    player1 = x_o()
    player2 = 'o' if player1 == 'x' else 'x'
    print(f'player 1 is {player1} and player 2 is {player2}')

    while not win:
        nummer_board = ['not use', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print(display_board(nummer_board))  # shows an empty starting board

        current_player = 1 # player 1 turn
        while not win:
            print(f"it's player {current_player} turn")
            choices = user_choice()

            while place_taken(nummer_board, choices): #checks if a place is already taken or not
                print('place is taken')
                choices = user_choice()

            marker = player1 if current_player == 1 else player2 # changes marker between player 1 and 2
            new_board(nummer_board, choices, marker)
            print(display_board(nummer_board))  # calls all the functions in order

            if win_check(nummer_board): #checks who win
                print (f'{marker} wins the game!')
                break


            elif board_full_check(nummer_board): #checks if it is a draw
                print("it's a draw!")
                break

            current_player = 2 if current_player == 1 else 1 #changes to player 2

        if not restart():
            print('thanks for playing')
            win = True


(tick_tack_toe())