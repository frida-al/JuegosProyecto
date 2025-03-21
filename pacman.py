"""Pacman, classic arcade game.

Exercises

1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.
"""

# Importacion de funciones necesarias
from random import choice
from turtle import Turtle, bgcolor, clear, up, goto
from turtle import tracer, listen, onkey, done
from turtle import dot, update, ontimer, setup, hideturtle
from freegames import floor, vector

# Diccionario donde se guarda el estado del juego (puntaje)
state = {'score': 0}
# Objetos invisibles que dibujan el mapa y muestran el puntaje
path = Turtle(visible=False)
writer = Turtle(visible=False)
# Direccion Inicial de pacman (en esta caso hacia la drecha)
aim = vector(5, 0)
# Posicion inicial de pacman
pacman = vector(-40, -80)
# Lista con los fantasmas con posicion inicial y direccion respectivamente
ghosts = [
    [vector(-180, 160), vector(15, 0)],
    [vector(-180, -160), vector(0, 15)],
    [vector(100, 160), vector(0, -15)],
    [vector(100, -160), vector(-15, 0)],
]
# Mapa del juego en una cuadricula de 20x20 (0= pared, 1=punto)
# Cambiar esta lista cambia el diseño del laberinto
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# fmt: on


def square(x, y):
    """Draw blue square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Convierte un punto (x,y) en un indice de la lista tiles"""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Devuelve True si no choca con una pared"""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Dibuja el laberiton y los puntos"""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.down()
                path.dot(9, 'green')  # color del alimento

            # mini pacmans como alimento
            path.begin_fill()  # rellenar cualquier forma que se dibuje
            for _ in range(4):  # bucle que se repite cuatro veces
                path.forward(4)  # mueve 4 pixeles hacia adelante
                path.left(90)  # gira 90 grados
            path.end_fill()


"""=======
Una vez que terimine el bucle de 4 veces se esperaba un cuadrado pero
Salieron unos minipacmans
=========="""


def move():
    """Movimiento de pacman y fantasmas"""
    writer.undo()  # borra texto anterior
    writer.write(state['score'])  # escribe el puntaje actualizado

    clear()  # Borra la pantalla antes de volver a dibujar
    if valid(pacman + aim):  # si el siguiente moviemiento de pacman es valido lo mueve
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:  # si hay un punto en dicha posicion de pacman
        tiles[index] = 2  # lo marca como adquirido
        state['score'] += 1  # el puntaje aumenta en uno
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)  # borra dicho punto

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')  # dibuja a pacman

# mueve y dibuja a los fantasmas
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            # si chocan con una pared se mueven hacia una direccion aleatoria
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')  # Dibuja el fantasma

    update()  # Actualiza el dibujo en pantalla

# verifica si algun fantasma ha atrapado a pacman
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return  # fin del juego en ese caso y ya no se llama a la funcion move

    ontimer(move, 50)  # llama a la funcion despues de 100ms


def change(x, y):
    """Cambia la direccion de pacman si no choca con pared"""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y


# Configuaracion de la ventana de juego
setup(420, 420, 370, 0)  # tamanio de la ventana
hideturtle()  # oculta tortuga incial?
tracer(False)  # Apaga la animacion automatica para tener mas control
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])  # Muestra el puntaje inicial
# Configuracion de las teclas de movimiento
listen()
onkey(lambda: change(5, 0), 'Right')  # Flecha derecha
onkey(lambda: change(-5, 0), 'Left')  # Flecha izquierda
onkey(lambda: change(0, 5), 'Up')  # Flecha arriba
onkey(lambda: change(0, -5), 'Down')  # Flecha abajo

# Inicia el juego
world()  # dibuja el mapa
move()  # Comienza a mover a pacman y los fantasmas
done()  # finaliza la configuacion para iniciar el bucle principal
