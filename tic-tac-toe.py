from IPython.display import clear_output

class TicTacToe():
    
    def __init__(self):
        self.board = ['#', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.player_1 = '❌'
        self.player_2 = '⭕️'
        self.turn_count = 0
        self.player_turn_number = 1
        self.we_have_a_winner = False
        
    def display_board(self):
        clear_output()
        print(f"{self.board[1]} | {self.board[2]} | {self.board[3]}")
        print("------------")
        print(f"{self.board[4]} | {self.board[5]} | {self.board[6]}")
        print("------------")
        print(f"{self.board[7]} | {self.board[8]} | {self.board[9]}")

    def next_turn(self):
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
        choice = int(input(f"\nPlayer {self.player_turn_number}, Enter a number: "))
        return choice
    
    def player_move(self):
        self.next_turn()
        
        if self.player_turn_number == 1:
            self.board[self.player_choice()] = self.player_1
        else:
            self.board[self.player_choice()] = self.player_2
            
    def win_check(self):
        player = self.who_turn()
        return ((self.board[1] == player and self.board[2] == player and self.board[3] == player) or 
        (self.board[4] == player and self.board[5] == player and self.board[6] == player) or
        (self.board[7] == player and self.board[8] == player and self.board[9] == player) or

        (self.board[1] == player and self.board[4] == player and self.board[7] == player) or
        (self.board[2] == player and self.board[5] == player and self.board[8] == player) or
        (self.board[3] == player and self.board[6] == player and self.board[9] == player) or

        (self.board[1] == player and self.board[5] == player and self.board[9] == player) or
        (self.board[3] == player and self.board[5] == player and self.board[7] == player))

    def play_game(self):
        while not self.we_have_a_winner:
            self.display_board()
            self.player_move()
            self.we_have_a_winner = self.win_check()

game = TicTacToe()
game.play_game()