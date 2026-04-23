# IMPORTO LAS LIBRERÍAS NECESARIAS

import random # librería para los barcos aleatorios y los disparos aleatorios
import clases # librería con las clases de barcos
import numpy as np # librería para gestionar matrices y arrays

# FUNCIÓN PARA CREAR TABLEROS DE 10X10 CON " " EN CADA CASILLA

def crear_tablero(tamaño:tuple = (10,10)): 
   tablero = np.full(tamaño, " ") 
   return tablero 

# FUNCIÓN PARA MOSTRAR LOS TABLEROS EN TERMINAL

def mostrar_tableros(mi_tablero, tablero_rival):  
   header = "     " + " ".join(str(i) for i in range(10)) 
   
   print("\n" + " " * 10 + "MI TABLERO")
   print(header)
   for i, fila in enumerate(mi_tablero):
      print(f"{i:2} | {' '.join(fila)} |") 
   
   print("\n" + " " * 8 + "TABLERO RIVAL")
   print(header)
   for i, fila in enumerate(tablero_rival):
      print(f"{i:2} | {' '.join(fila)} |")
   print()

# FUNCIÓN PARA COLOCAR LOS BARCOS EN MI TABLERO (aleatoriamente)

def colocar_barcos(mi_tablero):

   esloras = [2, 2, 2, 3, 3, 4] 
   flota = [] 

   for i in esloras: 
      barco = clases.Barco(i) 
      colocado = False 

      while not colocado: 
         f = np.random.randint(0, 10) 
         c = np.random.randint(0, 10) 
         orientacion = random.choice(["H", "V"]) 
         provisionales = []

         if orientacion == "H" and c + i <= 10: #
            provisionales = [(f, col) for col in range(c, c + i)]
         elif orientacion == "V" and f + i <= 10: 
            provisionales = [(fil, c) for fil in range(f, f + i)]

         if provisionales and all(mi_tablero[pos] == " " for pos in provisionales): 
            for pos in provisionales:
               mi_tablero[pos] = "O" 
               barco.coordenadas.append(pos) 
            flota.append(barco)
            colocado = True

   return flota 

# FUNCIÓN PARA COLOCAR LOS BARCOS ALEATORIOS DEL RIVAL

def colocar_barcos_rival(tablero_rival):
   esloras = [2, 2, 2, 3, 3, 4] 
   flota_rival = []  

   for i in esloras: 
      barco = clases.Barco(i) 
      colocado = False 
   
      while not colocado: 
         f = np.random.randint(0,10) 
         c = np.random.randint(0,10) 
         orientacion = random.choice(["H", "V"])
         provisionales = []

         if orientacion == "H" and c + i <= 10:
            provisionales = [(f, col) for col in range(c, c + i)]
         elif orientacion == "V" and f+i <= 10:
            provisionales = [(fil, c) for fil in range(f, f+i)]
         
         if provisionales and all(tablero_rival[pos] == " " for pos in provisionales):
            for pos in provisionales:
               tablero_rival[pos] = "O"
               barco.coordenadas.append(pos)
            flota_rival.append(barco)
            colocado = True
   return flota_rival   

# FUNCIÓN PARA DISPARAR
    
def disparar(casilla, tablero, flota):
   f, c = casilla 
   if tablero[f,c] == "O": 
      tablero[f,c] = "X" 

      for barco in flota: 
         if casilla in barco.coordenadas: 
            barco.recibir_impacto() 

            if barco.hundido(): 
               print(f" 🏴‍☠️ ¡La {barco.nombre} está hundida! 🏴‍☠️ ") 
            else:
               print("¡Tocado!") 

      return "tocado" 
   
   elif tablero[f,c] == " ": 
      tablero[f,c] = "A" 
      print(" 🌀 ¡Agua! 🌀 ") 
      return "agua" 
   
   else:
      print(" 🙄 ¡Inútil! Ya has malgastado pólvora en esa zona. ¿Acaso intentas pescar? 🙄 ") 
      return "repetido" 