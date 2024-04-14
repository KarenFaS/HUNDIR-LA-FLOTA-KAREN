
import numpy as np
import time
from Variables_hunde_la_flota import *


# Símbolos
simbolo_agua = "💧"
simbolo_barco = "⛵"
disparo_acertado= "💥"
disparo_fallido= "❌"

vidas_barco_jugador= 20
vidas_barco_pc= 20

#Eliminamos las comillas al imprimir los tableros
def custom_formatter(x):
    return str(x)

np.set_printoptions(formatter={'all': custom_formatter})


import warnings

# Desactivar todas las advertencias
warnings.filterwarnings("ignore")

# O desactivar solo las advertencias de sintaxis
warnings.filterwarnings("ignore", category=SyntaxWarning)

import pyfiglet
fig = pyfiglet.Figlet(width=100)

texto_estilizado = fig.renderText("Bienvenido  al  Juego  Hunde  la  Flota")

bienvenido= "\n\
       ▓▓╬▓                   ║ ▄  ▄  ▄\n\
      ▓▓▓║▓▓                  ║ ▓  ▓  ▓\n\
     ▓▓▓▓╬▓▓▓▓                ░░░░░░░░░░\n\
  ▄░▓▓▓▓▓║▓▓▓▓▓░░░░░      ▀███████████████▀\n\
░▀████████████████▀░░    ───────────────────"

#SALUDOS 
Saludo_inicio= "Para iniciar tienes que indicarnos como quieres establecer tu flota, \n\
    Selecciona una de las siguientes dos opciones: \n\
    1. Flota preestablecida \n\
    2. Quiero crear ubicar mi propia flota"


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





#def imagen_juego():
#    URL= "./imagenes/imagen_juego.jpg"
#    imagen = imread (URL)
#    imagen_plot = plt.imshow(imagen)
#    plt.axis("off")
#    return imagen_plot


#FUNCION PARA GENERAR TU PROPIA FLOTA
#Posiciona los barcos 
# 4 barcos de 1 posicion = barco1, barco2, barco3, barco4
# 3 barcos de 2 posiciones = barco5, barco6, barco7
# 2 barcos de 3 pocisiones = barco8, barco9
# 1 Barco de 4 posiciones = barco10

#Setup default para mi_tablero
def default ():
    barco1= [(1,1)] 
    barco2= [(7,2)]
    barco3= [(0,8)] 
    barco4= [(5,5)] 
    barco5= [(3,7),(3,8)]
    barco6= [(5,3),(6,3)]
    barco7= [(2,4),(2,5)]
    barco8= [(6,7),(6,8),(6,9)]
    barco9= [(3,0),(4,0),(5,0)]
    barco10=[(8,4),(8,5),(8,6),(8,7)]

    mi_flota= [barco1, barco2, barco3, barco4, barco5, barco6, barco7, barco8, barco9, barco10]
    
    for i in mi_flota:
        for j in i:
            mi_tablero[j]= simbolo_barco
    print(mi_tablero)


#def setup_manual():
def setup_manual():
    print("Las coodenadas que escojas deben de ser un numero entre 0 y 9")
    barco1= [(int(input("Proporciona una coordenada x: ")),int(input("Proporciona una coordenada y: ")))] 
    time.sleep(0.5)
    for b in barco1:
        mi_tablero[b]= simbolo_barco
    time.sleep(0.3)
    print(mi_tablero, "\n")

    barco2= [(int(input("Proporciona una coordenada x: ")),int(input("Proporciona una coordenada y: ")))] 
    time.sleep(0.5)
    for b in barco2:
        mi_tablero[b]= simbolo_barco
    time.sleep(0.3)
    print(mi_tablero, "\n")

    barco3= [(int(input("Proporciona una coordenada x: ")),int(input("Proporciona una coordenada y: ")))] 
    time.sleep(0.5)
    for b in barco3:
        mi_tablero[b]= simbolo_barco
    time.sleep(0.3)
    print(mi_tablero, "\n")

    barco4= [(int(input("Proporciona una coordenada x: ")),int(input("Proporciona una coordenada y: ")))] 
    time.sleep(0.5)
    for b in barco4:
        mi_tablero[b]= simbolo_barco
    time.sleep(0.3)
    print(mi_tablero, "\n")


        #Barco 5
    r= int(input("Barco dos pocisiones. Proporciona primera coordenada X: "))
    time.sleep(0.3)
    w= int(input("Barco dos pocisiones. Proporciona primera coordenada Y: "))
    time.sleep(0.3)
    sentido= (input("Escoge el sentido del barco. Coloca 'E' para horizontal y 'S' para vertical: "))
    time.sleep(0.3)
    if sentido== "E":
        barco5= [(r, w), (r, w+1)]
    elif sentido == "S":
        barco5= [(r,w), (r+1,w)] 
    else:
        print("Te quedas sin un barco por no seguir instrucciones")
    for bar in barco5:
        mi_tablero[bar]= simbolo_barco
    print(mi_tablero, "\n")
    time.sleep(0.3)

        #Barco 6
    r= int(input("Barco dos pocisiones. Proporciona primera coordenada X: "))
    time.sleep(0.3)
    w= int(input("Barco dos pocisiones. Proporciona primera coordenada Y: "))
    time.sleep(0.3)
    sentido= input("Escoge el sentido del barco. Coloca 'E' para horizontal y 'S' para vertical: ")
    time.sleep(0.3)
    if sentido== "E":
        barco6= [(r,w), (r,w+1)]
    elif sentido == "S":
        barco6= [(r,w), (r+1,w)]  
    else:
        print("Te quedas sin un barco por no seguir instrucciones")

    for bar in barco6:
        mi_tablero[bar]= simbolo_barco
    print(mi_tablero, "\n")
    time.sleep(0.3)



#BARCO 7
    r= int(input("Barco dos pocisiones. Proporciona primera coordenada X: "))
    time.sleep(0.3)
    w= int(input("Barco dos pocisiones. Proporciona primera coordenada Y: "))
    time.sleep(0.3)
    sentido= input("Escoge el sentido del barco. Coloca 'E' para horizontal y 'S' para vertical: ")
    time.sleep(0.3)
    if sentido== "E":
        barco7= [(r,w), (r,w+1)]
    elif sentido == "S":
        barco7= [(r,w), (r+1,w)]  
    else:
        print("Te quedas sin un barco por no seguir instrucciones")

    for bar in barco7:
        mi_tablero[bar]= simbolo_barco
    print(mi_tablero, "\n")
    time.sleep(0.3)


#BARCO 8
    r= int(input("Barco TRES pocisiones. Proporciona primera coordenada X: "))
    time.sleep(0.3)
    w= int(input("Barco TRES pocisiones. Proporciona primera coordenada Y: "))
    time.sleep(0.3)
    sentido= input("Escoge el sentido del barco. Coloca 'E' para horizontal y 'S' para vertical: ")
    time.sleep(0.3)

    if sentido== "E":
        barco8= [(r,w), (r,w+1), (r,w+2)]
    elif sentido == "S":
        barco8= [(r,w), (r+1,w), (r+2,w)]  
    else:
        print("Te quedas sin un barco por no seguir instrucciones: ")

    for bar in barco8:
        mi_tablero[bar]= simbolo_barco
    print(mi_tablero, "\n")
    time.sleep(0.3)



#BARCO 9
    r= int(input("Barco TRES pocisiones. Proporciona primera coordenada X: "))
    time.sleep(0.3)
    w= int(input("Barco TRES pocisiones. Proporciona primera coordenada Y: "))
    time.sleep(0.3)
    sentido= input("Escoge el sentido del barco. Coloca 'E' para horizontal y 'S' para vertical: ")
    time.sleep(0.3)

    if sentido== "E":
        barco9= [(r,w), (r,w+1), (r,w+2)]
    elif sentido == "S":
        barco9= [(r,w), (r+1,w), (r+2,w)]  
    else:
        print("Te quedas sin un barco por no seguir instrucciones")

    for bar in barco9:
        mi_tablero[bar]= simbolo_barco
    print(mi_tablero, "\n")
    time.sleep(0.3)



#BARCO 10
    r= int(input("Barco CUATRO pocisiones. Proporciona primera coordenada X: "))
    time.sleep(0.3)
    w= int(input("Barco CUATRO pocisiones. Proporciona primera coordenada Y: "))
    time.sleep(0.3)
    sentido= input("Escoge el sentido del barco. Coloca 'E' para horizontal y 'S' para vertical: ")
    time.sleep(0.3)

    if sentido== "E":
        barco10= [(r,w), (r,w+1), (r,w+2), (r,w+3)]
    elif sentido == "S":
        barco10= [(r,w), (r+1,w), (r+2,w), (r+3,w)]  
    else:
        print("Te quedas sin un barco por no seguir instrucciones")
    for bar in barco10:
        mi_tablero[bar]= simbolo_barco
    print(mi_tablero, "\n")
    time.sleep(0.3)


def setup_tus_barcos ():
    opcion= int(input("¿Que opcion escoges? "))
    if opcion == 2: 
        setup_manual()
    elif opcion== 1:
        default()
    else:
        None
    #juego= np.concatenate((mi_tablero,separacion, tablero_oculto), axis=1)
    time.sleep(1)
    #print(juego,"\n","TU TABLERO                             EL TABLERO DE LA PC")


#GENERAMOS LOS BARCOS ALEATORIOS DE LA PC

def flota_pc_aleatoria ():
    size_a= 1
    size_b= 2
    size_c= 3
    size_d= 4

    barcos_a= 0 #4
    barcos_b= 0 #3
    barcos_c= 0 #2
    barcos_d= 0 #1
    #Barcos de 1 posicion (barcos_a)
    while barcos_a < 4:
        x = np.random.randint(0,10)
        y= np.random.randint(0,10)
        
        if not np.any(tablero_pc[max(0, x-1):min(10, x+2), max(0, y-1):min(10, y+ size_a+1)] == simbolo_barco):
            tablero_pc[x,y]= simbolo_barco
            barcos_a += 1
            print("Barcos 1 posicion" , x,y)
        else:
            None

    #Barcos de 2 posiciones (barcos_b)
    while barcos_b < 3:
        
        orientacion = np.random.choice(["E", "S"])
        x = np.random.randint(0,10)
        y= np.random.randint(0,10)

        if orientacion == "E":
            if (y + size_b <= 10 and not np.any(tablero_pc[max(0, x-1):min(10, x+2), max(0, y-1):min(10, y+ size_b+2)] == simbolo_barco)):
                tablero_pc[x , y: y + size_b] = simbolo_barco
                barcos_b += 1
                print("Barco dos posiciones " ,x,y,", orientacion: ", orientacion)

        elif orientacion == "S":
            if (x + size_b <= 10 and not np.any(tablero_pc[max(0, x-1):min(10, x+size_b+1), max(0, y-1):min(10, y+2)]== simbolo_barco)):
                tablero_pc[x: x+ size_b, y] = simbolo_barco
                barcos_b += 1
                print("Barco dos posiciones " ,x,y,", orientacion: ", orientacion)

    #Barcos de 3 posiciones (barcos_c)
    while barcos_c < 2:
        
        orientacion = np.random.choice(["E", "S"])
        x = np.random.randint(0,10)
        y= np.random.randint(0,10)

        if orientacion == "E":
            if (y + size_c <= 10 and not np.any(tablero_pc[max(0, x-1):min(10, x+2), max(0, y-1):min(10, y+ size_c+1)] == simbolo_barco)):
                tablero_pc[x , y: y + size_c] = simbolo_barco
                barcos_c += 1
                print("Barco TRES posiciones " ,x,y,", orientacion: " ,orientacion)

        elif orientacion == "S":
            if (x + size_c <= 10 and not np.any(tablero_pc[max(0, x-1):min(10, x+size_c+1), max(0, y-1):min(10, y+2)]== simbolo_barco)):
                tablero_pc[x: x+ size_c, y] = simbolo_barco
                barcos_c += 1
                print("Barco TRES posiciones " ,x,y,", orientacion: " ,orientacion)


    #Barcos de 4 posiciones (barcos_d)
    while barcos_d == 0:
        
        orientacion = np.random.choice(["E", "S"])
        x = np.random.randint(0,10)
        y= np.random.randint(0,10)

        if orientacion == "E":
            if (y + size_d <= 10 and not np.any(tablero_pc[max(0, x-1):min(10, x+2), max(0, y-1):min(10, y+ size_d+1)] == simbolo_barco)):
                tablero_pc[x , y: y + size_d] = simbolo_barco
                barcos_d += 1
                print("BARCO MAYOR " ,x,y,", orientacion: " ,orientacion)

        elif orientacion == "S":
            if (x + size_d <= 10 and not np.any(tablero_pc[max(0, x-1):min(10, x+size_d+1), max(0, y-1):min(10, y+2)]== simbolo_barco)):
                tablero_pc[x: x+ size_d, y] = simbolo_barco
                barcos_d += 1
                print("BARCO MAYOR " ,x,y,", orientacion: " ,orientacion)



#juego= np.concatenate((mi_tablero,separacion, tablero_pc,separacion, tablero_oculto), axis=1)
#print(juego,"\n","TU TABLERO                             EL TABLERO DE LA PC,                 TABLERO OCULTO:")


#--------------------------------------------------------------------
#--------------------------------------------------------------------
vidas_barco_jugador= np.sum(mi_tablero== simbolo_barco)
vidas_barco_pc= np.sum(tablero_pc== simbolo_barco)

def accion_disparo ():
    respuesta= input("¿Listo para empezar a disparar? Responde SI o NO: ")
    if respuesta == "SI": 
        lucha()
    else:
        None
    


vidas_barco_jugador= np.sum(mi_tablero== simbolo_barco)
vidas_barco_pc= np.sum(tablero_pc== simbolo_barco)

def lucha():
    vidas_barco_jugador= np.sum(mi_tablero== simbolo_barco)
    vidas_barco_pc= np.sum(tablero_pc== simbolo_barco)
    while (vidas_barco_jugador != 0) and (vidas_barco_pc !=0):
        vidas_barco_jugador= np.sum(mi_tablero== simbolo_barco)
        vidas_barco_pc= np.sum(tablero_pc== simbolo_barco)
        turno_jugador = 1
        while turno_jugador == 1:
            disparo_x = int(input("ESCOGE UNA COORDENADA PARA X. DEBE DE SER UN NUMERO DE 0 A 9: "))
            time.sleep (0.5)
            disparo_y = int(input("ESCOGE UNA COORDENADA PARA Y. DEBE DE SER UN NUMERO DE 0 A 9: "))
            time.sleep (0.5)
            disparo = (disparo_x, disparo_y)

            if tablero_pc[disparo] == simbolo_barco:
                tablero_oculto[disparo] = disparo_acertado
                tablero_pc[disparo] = disparo_acertado
                print("Coordenada:", disparo_x, disparo_y, "Has acertado!! :D", "\n")
                vidas_barco_pc -= 1
            elif tablero_pc[disparo] == simbolo_agua:
                tablero_oculto[disparo] = disparo_fallido
                tablero_pc[disparo] = disparo_fallido
                turno_jugador -= 1
                print("Coordenada:", disparo_x, disparo_y, "No has dado a ningun barco!! :(" "\n")
            else:
                print("HAS REPETIDO COORDENADA. PIERDES UNA VIDA")
                turno_jugador -= 1

        time.sleep(0.3)
        juego= np.concatenate((mi_tablero,separacion, tablero_oculto), axis=1)
        print(juego,"\n","TU TABLERO                             EL TABLERO DE LA PC")
        time.sleep(0.3)

        turno_pc=3
        while turno_pc != 0:
            disparo_x = np.random.randint(0,10)
            time.sleep(0.5)
            disparo_y = np.random.randint(0,10)
            time.sleep(0.5)
            disparo = (disparo_x, disparo_y)

            if mi_tablero[disparo] == simbolo_barco:
                mi_tablero[disparo] = disparo_acertado
                print("Coordenada:", disparo_x, disparo_y, "PC ha acertado!! :D", "\n")
                vidas_barco_jugador -=1
            elif mi_tablero[disparo] == simbolo_agua:
                mi_tablero[disparo] = disparo_fallido
                turno_pc -= 1
                print("Coordenada:", disparo_x, disparo_y, "PC no ha acertado!! :(" "\n")
            else:
                print("PC HA REPETIDO COORDENADA. SIEMPRE PIERDES UNA VIDA :'( ")
                turno_pc -= 1

        time.sleep(0.3)
        juego= np.concatenate((mi_tablero,separacion, tablero_oculto), axis=1)
        print(juego,"\n","TU TABLERO                             EL TABLERO DE LA PC")
        time.sleep(0.3)

juegofinal= np.concatenate((mi_tablero,separacion, tablero_pc), axis=1)

def ganador ():
    if vidas_barco_pc== 0:
        mensaje = "🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆\n\
     ERES EL GANADOR!!!!\n\
🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆"
        return mensaje

    elif vidas_barco_jugador == 0:
        mensaje= "😩😩😩😩😩😩😩😩😩😩\n\
      HAS PERDIDO!!\n\
😩😩😩😩😩😩😩😩😩😩"
        return mensaje
    else:
        None