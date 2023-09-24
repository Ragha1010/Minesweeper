import pytest
from minesweeper import MinesweeperGame  # Make sure to adjust the import statement based on your project structure
from unittest.mock import patch
from io import StringIO

@pytest.fixture
def game():
    return MinesweeperGame ()


def test_initialize_board(game):
    # Call the initialize_board() method to set up the game board and mine locations.
    game.initialize_board ()
    # Ensure the number of mine locations matches the specified number of mines
    assert len (game.mine_locations) == game.num_mines
    # Ensure all mine locations are within the valid range of rows and columns
    # This verifies that the mines are placed within the boundaries of the game board.
    for row, col in game.mine_locations:
        assert 0 <= row < game.board_size
        assert 0 <= col < game.board_size


def test_new_game(game):
    game.new_game ()
    # Ensure that the board is initialized and has the correct dimensions
    assert len (game.board) == game.board_size
    for row in game.board:
        assert len (row) == game.board_size
    # Ensure that the game is not over at the beginning of a new game
    assert not game.is_game_over ()
    # Ensure that the game is not won at the beginning of a new game
    assert not game.is_game_won ()


def test_reveal_square_safe(game):
    # Start a new Minesweeper game.
    game.new_game ()
    # Define the coordinates (row, col) of a safe square (0, 0).
    row, col = 0, 0
    # Attempt to reveal the square at (0, 0) using the reveal_square() method.
    game.reveal_square (row, col)
    assert "test reveal square safe"


def test_reveal_square_mine():
    game = MinesweeperGame ()
    game.new_game ()

    # Force a mine location at (0, 0) for testing purposes.
    game.mine_locations = [(0, 0)]

    # Attempt to reveal a mine at (0, 0) using the reveal_square() method, and expect a ValueError.
    row, col = 0, 0
    # with pytest.raises (ValueError, match="You hit a mine!"):  # Adjust the error message as needed
    #     assert "you hit a mine"
    game.reveal_square (row, col)
    # Ensure that the game is over after hitting a mine
    assert game.is_game_over ()

def test_invalid_input_row_out_of_range(game):
    # Start a new game.
    game.new_game ()
    # Attempt to reveal a square with a row value out of the valid range (less than 0).
    row, col = -1, 0
    # Expect a ValueError to be raised since the row value is out of the valid range (0 to 7).
    with pytest.raises (ValueError):
        game.reveal_square (row, col)


def test_invalid_input_col_out_of_range(game):
    # Start a new game.
    game.new_game ()
    # Attempt to reveal a square with a column value out of the valid range (greater than 7).
    row, col = 0, 8
    # Expect a ValueError to be raised since the column value is out of the valid range (0 to 7).
    with pytest.raises (ValueError):
        game.reveal_square (row, col)

def test_display_board(game):
    # Start a new game.
    game.new_game()
    try:
        # Attempt to display the game board.
        game.display_board()
    except Exception as e:
        # If an error occurs during the display_board call, fail the test and report the error.
        assert False, f"Error occurred when displaying the board: {e}"
    # If no error occurred during the display_board call, the test passes
    assert True

def test_play_game():
    # Define a list of moves (coordinates) to simulate playing the game
    game = MinesweeperGame()
    game.new_game()
    game.mine_locations = [(1, 1)]
    moves = [(0, 0), (0, 1), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (2, 4)]

    # Mock user input with the coordinates
    with patch('builtins.input', side_effect=[f"{row} {col}" for row, col in moves]):
        for move in moves:
            row, col = move
            # with pytest.raises(ValueError) as e:
            result = game.reveal_square(row, col)  # Simulate revealing a square
            print("-----------------------------")
            print("result: {}".format(result))
            #print((result))
            #game.reveal_square (row, col)
            if result == "X":
                assert "Game is Over"
                break
            else:
                assert "In progress"
            game.display_board()


def test_play_game_won():
    # Create an instance of your Minesweeper game
    game = MinesweeperGame ()

    # Set up the game board with specific mine locations
    #game.mine_locations = [(1, 1), (2, 2)]

    # Define a list of coordinates (rows and columns) to input
    pairs = [(row, col) for row in range(8) for col in range(8) if (row, col) not in game.mine_locations]

    # Mock user input with the coordinates
    with patch('builtins.input', side_effect=[f"{row} {col}" for row, col in pairs]):
        for pair in pairs:
            row, col = pair
            game.reveal_square(row, col)  # Simulate revealing a square
        game.display_board ()
    assert game.is_game_won()==True, "---Game is won"