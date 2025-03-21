# TIC TAC TOE
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
