# JuegosProyecto
Evidencia proyecto


# PACMAN :V
## Por Cesar Augusto Ramirez Davila A01712439
Este proyecto es una implementación del clásico juego **Pac-Man** en Python usando la librería `turtle` y `freegames`.

## Cambios realizados al código original

- **Nuevo Laberinto**  
  - Se modificó la estructura del tablero (`tiles`) para generar un diseño diferente al orignal.  

- **Aumento de Velocidad de los Fantasmas y PacMan**  
  - Se incrementó la velocidad base de los fantasmas aumentando el valor de sus vectores de movimiento.  
  - Se redujo el tiempo entre actualizaciones de 100 a 50ms (Lo que también afecto a la velocidad de PacMan).  

- **Modificación del Alimento**  
  - Se cambió la forma del alimento de un punto circular a un mini PacMan.  
  - Se ajustó el tamaño y color del alimento.  
------------------------------------
# Memorama
## por Frida Arcadia Luna A01711615
Se agregó la funcionalidad de contar y desplegar las parejas ya descubiertas, detectar cuando todos los cuadros han sido destapados y cambiar el número de casillas en el tablero.

### Contador de parejas descubiertas

Para esta parte, se agregó un contador que va aumentando de uno en uno cada vez que se descubre una pareja.

### Tablero completado

Agregar un verificador que marque cuando todo el tablero esté completado, además de agregar una leyenda que indique que el juego ha terminado.

### Cambiar número de casillas en el tablero

Se cambiaron las medidas y coordenadas del tablero para acomodar el nuevo número de tableros
------------------------------------
# TIC TAC TOE
## por Adrián Márquez Núñez A01707721
Este proyecto utliza las librerias turle y freegames para un juego de gato
## Cambios al código
### Tamaño y color
Se modifico el tamaño y color de X y O a la hora de jugar cada turno.
Con la función color de la libreria turle.
### Casilla ocupada
Se añadio una función para evitar que se coloqué una figura en una casilla ocupada.
Estó con un vector para checar las casillas usadas y una validación booleana.
### Ganador
Se añadio una función para determinar un ganador.
Se lleva un registro del tablero y si se muestra cualquiera de las configuraciones ganadoras
se muestra el mensaje.
