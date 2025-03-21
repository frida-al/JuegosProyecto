"""Tic Tac Toe.

Exercises:
1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import (
    up, goto, down, circle, color, width, write, update, ontimer,
    setup, hideturtle, tracer, done, onscreenclick
)
from freegames import line

# Vector to keep track of occupied squares
squares = []

# Board to keep track of player moves
board = [[None, None, None], [None, None, None], [None, None, None]]


def occupied(x, y):
    """Return True if the square is occupied."""
    return (x, y) in squares


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('red')
    width(5)  # Set width for X
    line(x + 33, y + 33, x + 100, y + 100)
    line(x + 33, y + 100, x + 100, y + 33)


def drawo(x, y):
    """Draw O player."""
    color('blue')
    width(5)  # Set width for O
    up()
    goto(x + 67, y + 25)
    down()
    circle(40)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}  # 0 for X, 1 for O
players = [drawx, drawo]


def clear_message():
    """Clear any message."""
    up()
    goto(-50, 180)
    color('white')
    write("                ", font=("Arial", 12, "bold"))
    update()


def check_winner():
    """Verify if there is a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    # Check columns
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col] and
                board[0][col] is not None):
            return board[0][col]
    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] and
            board[0][0] is not None):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0] and
            board[0][2] is not None):
        return board[0][2]
    return None


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    col = int((x + 200) // 133)  # Calculate column index
    row = int((y + 200) // 133)  # Calculate row index

    # Check if the square is in use
    if occupied(x, y):
        up()
        goto(-50, 180)
        color('red')
        write("Square in use", font=("Arial", 12, "bold"))
        update()
        ontimer(clear_message, 1000)
        return

    # If it is empty, draw an X or O
    squares.append((x, y))
    player = state['player']
    board[row][col] = player
    draw = players[player]
    draw(x, y)
    update()

    # Check for a winner
    winner = check_winner()
    if winner is not None:
        up()
        goto(-50, 180)
        color('black')
        write(f"¡Player {'X' if winner == 0 else 'O'} has won!",
              font=("Arial", 12, "bold"))
        update()
        return

    # Switch players
    state['player'] = not player


# Set up the game window
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
