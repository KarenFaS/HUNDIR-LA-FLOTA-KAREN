
import numpy as np
import time
from Variables_hunde_la_flota import *
from Funciones_hunde_la_flota import *
import pandas as pd
import pyfiglet

print(texto_estilizado)
print(bienvenido)
print("\n")
time.sleep(0.5)
print(Saludo_inicio)
time.sleep(0.3)
print("\n")

setup_tus_barcos()
time.sleep(0.1)
print("\n")

flota_pc_aleatoria()
time.sleep(0.3)
print("\n")
print("Tu contrincante tambien ha pocisionado su flota")
print("\n")
print(tablero_pc)
print("\n")

print(Instrucciones_disparo)
print("\n")
time.sleep(0.5)
accion_disparo()
time.sleep(0.5)
print("\n")
print("\n")

print(ganador())
time.sleep(45)