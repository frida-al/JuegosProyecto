"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(50)) * 2 # Changing tile number
state = {'mark': None}
hide = [True] * 100
pairsFound = 0 # Initializa count of uncovered pairs


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 250) // 45 + ((y + 250) // 45) * 10) #Adjusting coordinates on new number of tiles


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 10) * 45 - 250, (count // 10) * 45 - 250 #Adjusting coordinates on new number of tiles



def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global pairsFound # Use global variable
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        pairsFound += 1 # Increment count of uncovered pairs
        state['mark'] = None
    if all(not h for h in hide): # Verification, if all tiles have been uncovered
        up()
        goto(-200, 0)
        color('green')
        write("All pairs uncovered! Game over!", font = ('Roboto', 20, 'normal'))
        return


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(100):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    up()
    goto(-200, 200)
    color('green')
    write(f'Pairs found: {pairsFound}', font = ('Roboto', 20, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
Logo
