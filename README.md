
==========///PROYECTO INTEGRADOR PARTE & ///========


Este proyecto representa un juego de laberinto en Python. El objetivo del juego es mover al jugador desde la posición de inicio hasta la posición de destino en un laberinto. Las teclas 'w', 's', 'a' y 'd' se utilizan para mover al jugador hacia arriba, abajo, izquierda y derecha, respectivamente.

Modificaciones Realizadas
En este proyecto, se realizaron las siguientes modificaciones:

Uso de función map para convertir laberinto de cadena a matriz: La función convertir_laberinto_a_matriz() fue reescrita para utilizar la función map en lugar de un bucle. La función convertir_laberinto_a_matriz() toma la cadena del laberinto como entrada y devuelve una matriz representando el laberinto en forma de lista de listas.

Uso de función reduce para leer el mapa desde un archivo: La función leer_mapa_desde_archivo() fue reescrita para utilizar la función reduce en lugar de un bucle. La función leer_mapa_desde_archivo() toma el nombre del archivo como entrada, lee todo el contenido en una sola operación y lo concatena en una cadena para representar el laberinto.

Corrección de la ruta del archivo: Se corrigió la ruta del archivo del laberinto para que el programa pueda leer correctamente el contenido del archivo mapas.txt. Ahora se utiliza la función os.path.join() para obtener la ruta completa del archivo, y se asegura de que el archivo mapas.txt esté en la misma ubicación que el archivo main.py.

Estas modificaciones permiten una mejor eficiencia y organización del código, y facilitan la carga de laberintos desde archivos externos en lugar de proporcionarlos directamente en el código.

Ejecución del Juego
Para ejecutar el juego, simplemente ejecute el archivo main.py. Asegúrese de tener Python instalado en su sistema.

css
Copy code
python main.py
El juego le pedirá que presione las teclas 'w', 's', 'a' o 'd' para mover al jugador en diferentes direcciones y llegar al final del laberinto.

Notas
Asegúrese de que el archivo mapas.txt esté presente en la misma ubicación que el archivo main.py antes de ejecutar el juego.

Puede modificar el contenido del archivo mapas.txt para crear nuevos laberintos y probar diferentes configuraciones en el juego. Asegúrese de seguir el mismo formato utilizado en los mapas definidos en el archivo mapas.py.

Espero que esta documentación te sea útil. ¡Disfruta del juego de laberinto!