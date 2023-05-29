import art

class TicTacToe():
    
    def __init__(self):
        self.board = ['#', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.possible_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.player_1 = '❌'
        self.player_2 = '⭕️'
        self.turn_count = 0
        self.player_turn_number = 1
        self.start_game = True
        self.game_over = False
        self.logo = art.logo
        self.lost = art.lost
        self.tie = art.tie
        self.won = art.won
        
    def display_board(self):
        '''Displays gameboard.'''
        print(f"\n{self.board[1]} | {self.board[2]} | {self.board[3]}")
        print("------------")
        print(f"{self.board[4]} | {self.board[5]} | {self.board[6]}")
        print("------------")
        print(f"{self.board[7]} | {self.board[8]} | {self.board[9]}")

    def next_player_turn(self):
        '''Updates turn_count and player_turn_number.'''
        self.turn_count += 1

        if self.turn_count % 2 == 0:
            self.player_turn_number = 2
        else:
            self.player_turn_number = 1
    
    def who_turn(self):
        '''Returns player/mark who's turn it is.'''
        if self.player_turn_number == 1:
            return self.player_1
        else:
            return self.player_2
        
    def player_choose_position(self):
        '''Returns player's chosen position, when valid.'''
        player_choice = (input(f"\nPlayer {self.player_turn_number}, Choose a position: ")).replace(" ", "")
        
        while player_choice not in self.possible_positions:
            print("Invalid position. Try again.")
            player_choice = self.player_choose_position()
        
        player_choice = int(player_choice)

        while self.board[player_choice] != '  ':
            print("This position is already taken. Try again.")
            player_choice = self.player_choose_position()
        
        return player_choice

    def player_move(self):
        '''Fills in player's mark at chosen position.'''
        self.next_player_turn()
        
        if self.player_turn_number == 1:
            self.board[self.player_choose_position()] = self.player_1
        else:
            self.board[self.player_choose_position()] = self.player_2
            
    def win_check(self):
        '''Returns True if there's 3 marks in a row.'''
        player = self.who_turn()
        if ((self.board[1] == player and self.board[2] == player and self.board[3] == player) or 
        (self.board[4] == player and self.board[5] == player and self.board[6] == player) or
        (self.board[7] == player and self.board[8] == player and self.board[9] == player) or

        (self.board[1] == player and self.board[4] == player and self.board[7] == player) or
        (self.board[2] == player and self.board[5] == player and self.board[8] == player) or
        (self.board[3] == player and self.board[6] == player and self.board[9] == player) or

        (self.board[1] == player and self.board[5] == player and self.board[9] == player) or
        (self.board[3] == player and self.board[5] == player and self.board[7] == player)):
            print(f"\n{self.won}")
            return True
        
    def tie_check(self):
        '''Returns True if it's a tie / no available positions to play.'''
        if '  ' not in self.board:
            print(f"\n{self.tie}")
            return True
        
    def want_to_play(self):
        '''Returns True if player wants to play again.'''
        play_again = input("Do you want to play again? Type 'y' to continue, press anything else to exit: ").lower()
        return play_again == 'y'
    
    def game_intro(self):
        '''Prints introduction to the game.'''
        print(self.logo)
        print("Welcome to Tic Tac Toe.")
        print("The first player to get 3 of her marks in a row is the winner.")
        print("Choose a position between 1 - 9.\n")
        print('''
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9\n
        ''')

    def game_reset(self):
        '''Resets the game'''
        self.game_over = False
        self.board = ['#', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']

    def play_game(self):
        '''Starts/ends the game.'''
        self.game_intro()
        while self.start_game:
            self.game_reset()
            while not self.game_over:
                self.player_move()
                self.display_board()
                self.game_over = self.win_check()
                if self.game_over:
                    break
                self.game_over = self.tie_check()
            self.start_game = self.want_to_play()
        print("Thanks for playing. 👋")
            
new_game = TicTacToe()
new_game.play_game()