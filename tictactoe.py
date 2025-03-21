"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line

# vector to keep track of occupied squares
squares= []

# returns if a square is occupied
def occupied(x, y):
	return (x, y) in squares

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    # changes the color
    color('red')
    # centers the X
    line(x + 33, y + 33, x + 100, y + 100)
    line(x + 33, y + 100 , x + 100, y + 33)


def drawo(x, y):
    """Draw O player."""
    # changes the color
    color('blue')
    up()
    # centers the circle
    goto(x + 67, y + 25)
    down()
    circle(40)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    # checks if the square is in use
    if occupied(x, y):
        up()
        goto(-50, 180)
        color('red')
        write("Square in use", font=("Arial", 12, "bold"))
    # if it is empty draws an X or O
    else:
        squares.append((x, y))
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
  
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()

