import random
import logging

print("Logging...")
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.FileHandler('mine.log')],
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging = logging.getLogger(__name__)

class MinesweeperGame:
    def __init__(self):
        self.board_size = 8
        self.num_mines = 10
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.mine_locations = []


    def initialize_board(self):
        try:
            # Place mines randomly on the board
            self.mine_locations = random.sample([(r, c) for r in range(self.board_size) for c in range(self.board_size)],
                                                self.num_mines)
            logging.info("Board has been initialized successfully")
            print ("Board has been initialized successfully")
        except ValueError as e:
            logging.error(f"Error during board initialization: {e}")

    def new_game(self):
        logging.info("New game logging....")
        try:
            # Create a new game board
            self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
            logging.info("New game opened")
            print ("New game opened")
            # Place mines on the board
            self.initialize_board()
            # Initialize other game-related data, e.g., flags, revealed squares, etc.
        except Exception as e:
            logging.error(f"Error starting a new game: {e}")

    def display_board(self):
        try:
            print("Minesweeper Board:")
            print("    0 1 2 3 4 5 6 7")
            for r in range(self.board_size):
                print(f"{r} | {' '.join(self.board[r])} |")
        except Exception as e:
            logging.error(f"Error displaying the board: {e}")

    def reveal_square(self, row, col):
            if not (0 <= row < self.board_size) or not (0 <= col < self.board_size):
                logging.error("Invalid row or column")
                print ("Invalid row or column")
                raise ValueError("Invalid row or column")

            if (row, col) in self.mine_locations:
                self.board[row][col] = 'X'
                logging.error ("You hit a mine!")
                print ("Found Mine at this location... Game is Over")
                # raise ValueError ("You hit a mine!")
                return 'X'
            else:
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < self.board_size and 0 <= nc < self.board_size and (nr, nc) in self.mine_locations:
                            count += 1
                self.board[row][col] = str(count)
                return "Y"

    def is_game_over(self):
        logging.info("Game is over")
        return any (self.board[r][c] == 'X' for r, c in self.mine_locations)

    def is_game_won(self):
        try:
            if (all(self.board[r][c] != ' ' for r in range(self.board_size) for c in range(self.board_size)) \
                and not self.is_game_over()) == True:
                print("Game is won")
            else:
                print("Lost Game")
            return all(self.board[r][c] != ' ' for r in range(self.board_size) for c in range(self.board_size)) \
                and not self.is_game_over()
        except Exception as e:
            logging.error(f"Error checking if the game is won: {e}")

# if __name__ == "__main__":
#     # Configure logging
#     logging.info("test")
#     a = MinesweeperGame()
#     a.is_game_over()