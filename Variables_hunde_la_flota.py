
import numpy as np
import time
import Funciones_hunde_la_flota as fun
import matplotlib.pyplot as plt

# Símbolos
simbolo_agua = "💧"
simbolo_barco = "⛵"
disparo_acertado= "💥"
disparo_fallido= "❌"

#Eliminamos las comillas al imprimir los tableros
def custom_formatter(x):
    return str(x)

np.set_printoptions(formatter={'all': custom_formatter})


#SALUDOS 
Saludo_inicio= "Para iniciar tienes que indicarnos como quieres establecer tu flota, \n\
    Selecciona una de las siguientes dos opciones: \n\
    1. Flota preestablecida \n\
    2. Quiero crear ubicar mi propia flota"


vidas_barco_jugador= 20
vidas_barco_pc= 20

Instrucciones_disparo= "Es momento de empezar a disparar. EMPIEZAS TU!\n\
Si aciertas, puedes seguir disparando, si fallas, tu turno se acaba. \n\
Como tu eres mas listo, la pc podra tener 3 fallos antes de que acabe su turno.\n\
\n\
░░░░░░░░◢▇▇▇▮◣\n\
░░░░░░░░███████ ]▄▄▄▄▄\n\
░░░░░░░░◥██████\n\
▂▄▅█████████████▅▄\n\
I███████████████████].\n\
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤..."

# URL de la imagen del juego

#def imagen_juego(URL):
#    URL= "./imagenes/imagen_juego.jpg"
#    imagen = imread (URL)
#    imagen_plot = plt.imshow(imagen)
#    plt.axis("off")
#    return imagen_plot
    

#Creamos los tableros
mi_tablero = np.full((10,10), simbolo_agua)
tablero_pc = np.full((10,10), simbolo_agua)
tablero_oculto = np.full((10,10), simbolo_agua)

# Concatena los tableros horizontalmente y Agrega una fila de separación entre tableros
separacion = np.full((10,1), " ")



#-------------------------------------------------------
#Barcos aleatorios de la pc
#-------------------------------------------------------
size_a= 1
size_b= 2
size_c= 3
size_d= 4

barcos_a= 0 #4
barcos_b= 0 #3
barcos_c= 0 #2
barcos_d= 0 #1


vidas_barco_jugador= np.sum(mi_tablero== simbolo_barco)
vidas_barco_pc= np.sum(tablero_pc== simbolo_barco)

