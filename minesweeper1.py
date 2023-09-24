
import random
import logging


class MinesweeperGame:
    def __init__(self):
        self.board_size = 8
        self.num_mines = 10
        self.board = [[' ' for _ in range (self.board_size)] for _ in range (self.board_size)]
        self.mine_locations = []

        # Configure logging
        self.configure_logging ()

    def configure_logging(self):
        logging.basicConfig (
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler ('minesweeper.log'),
                logging.StreamHandler ()
            ]
        )
        self.logger = logging.getLogger ('minesweeper')

    def initialize_board(self):
        try:
            # Place mines randomly on the board
            self.mine_locations = random.sample (
                [(r, c) for r in range (self.board_size) for c in range (self.board_size)],
                self.num_mines)
            self.logger.info ("Board has been initialized successfully")
        except ValueError as e:
            self.logger.error (f"Error initializing the board: {e}")

    def new_game(self):
        try:
            # Create a new game board
            self.board = [[' ' for _ in range (self.board_size)] for _ in range (self.board_size)]
            self.logger.info ("New game opened")
            # Place mines on the board
            self.initialize_board ()
            # Initialize other game-related data, e.g., flags, revealed squares, etc.
        except Exception as e:
            self.logger.error (f"Error starting a new game: {e}")

    def display_board(self):
        self.logger.info ("Minesweeper Board:")
        self.logger.info ("   0 1 2 3 4 5 6 7")
        print ("    0 1 2 3 4 5 6 7")
        for r in range (self.board_size):
            #self.logger.info (f"{r} | {' '.join (self.board[r])} |")
            print (f"{r} | {' '.join (self.board[r])} |")



    def reveal_square(self, row, col):
        try:
            if not (0 <= row < self.board_size) or not (0 <= col < self.board_size):
                raise ValueError ("Invalid row or column")

            if (row, col) in self.mine_locations:
                self.board[row][col] = 'X'
                self.logger.error ("You hit a mine!")  # Log error when a mine is revealed
                raise ValueError ("You hit a mine!")  # Raise ValueError when a mine is revealed
            else:
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < self.board_size and 0 <= nc < self.board_size and (nr, nc) in self.mine_locations:
                            count += 1
                self.board[row][col] = str (count)
        except ValueError as e:
            self.logger.error (f"Invalid move: {e}")
        except Exception as e:
            self.logger.error (f"Error while revealing square: {e}")

    def is_game_over(self):
        return any (self.board[r][c] == 'X' for r, c in self.mine_locations)

    def is_game_won(self):
        return all (self.board[r][c] != ' ' for r in range (self.board_size) for c in range (self.board_size)) \
               and not self.is_game_over ()


if __name__ == "__main__":
    logging.info ("Welcome to Minesweeper!")
    game = MinesweeperGame ()
    game.initialize_board ()

    while not game.is_game_over () and not game.is_game_won ():
        game.display_board ()
        try:
            row = int (input ("Enter row (0-7): "))
            col = int (input ("Enter column (0-7): "))
            if 0 <= row < 8 and 0 <= col < 8 and game.board[row][col] == ' ':
                game.reveal_square (row, col)
            else:
                game.logger.error (
                    "Invalid input. Row and column must be between 0 and 7, and the square must not be revealed.")
        except ValueError:
            game.logger.error ("Invalid input. Row and column must be integers between 0 and 7.")
        except IndexError:
            game.logger.error ("Invalid input. Row and column must be between 0 and 7.")

    game.display_board ()  # Display the final game board

    if game.is_game_won ():
        print ("Congratulations! You won!")
        game.logger.info ("Congratulations! You won!")
    else:
        game.logger.info ("Game over. You hit a mine!")
        print ("Game over. You hit a mine!")


