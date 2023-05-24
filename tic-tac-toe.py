import art

class TicTacToe():
    
    def __init__(self):
        self.board = ['#', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.player_1 = '❌'
        self.player_2 = '⭕️'
        self.turn_count = 0
        self.player_turn_number = 1
        self.play_game = True
        self.game_over = False
        self.logo = art.logo
        self.lost = art.lost
        self.tie = art.tie
        self.won = art.won
        
    def display_board(self):
        print(f"\n{self.board[1]} | {self.board[2]} | {self.board[3]}")
        print("------------")
        print(f"{self.board[4]} | {self.board[5]} | {self.board[6]}")
        print("------------")
        print(f"{self.board[7]} | {self.board[8]} | {self.board[9]}")

    def next_player_turn(self):
        self.turn_count += 1

        if self.turn_count % 2 == 0:
            self.player_turn_number = 2
        else:
            self.player_turn_number = 1
    
    def who_turn(self):
        if self.player_turn_number == 1:
            return self.player_1
        else:
            return self.player_2
        
    def player_choice(self):
        return int(input(f"\nPlayer {self.player_turn_number}, Choose a position: "))
        
    def rule_check(self):
        choice = self.player_choice()
        while choice < 1 or choice > 9:
            print("Invalid position. Try again.")
            choice = self.player_choice()
        while self.board[choice] != '  ':
            print("This position is already taken. Try again.")
            choice = self.player_choice()
        return choice
    
    def player_move(self):
        self.next_player_turn()
        
        if self.player_turn_number == 1:
            self.board[self.rule_check()] = self.player_1
        else:
            self.board[self.rule_check()] = self.player_2
            
    def win_check(self):
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
        if '  ' not in self.board:
            print(f"\n{self.tie}")
            return True
        
    def want_to_play(self):
        play_again = input("Do you want to play again? Type 'y' to continue, press anything else to exit: ").lower()
        return play_again == 'y'
    
    def game_intro(self):
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
        self.game_over = False
        self.board = ['#', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']

    def start_game(self):
        self.game_intro()
        while self.play_game:
            self.game_reset()
            while not self.game_over:
                self.player_move()
                self.display_board()
                self.game_over = self.win_check()
                if self.game_over:
                    break
                self.game_over = self.tie_check()
            self.play_game = self.want_to_play()
            

new_game = TicTacToe()
new_game.start_game()