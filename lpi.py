#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
          _  (`-')  _
   <-.    \-.(OO ) (_)
 ,--. )   _.'    \ ,-(`-')
 |  (`-')(_...--'' | ( OO)
 |  |OO )|  |_.' | |  |  )
(|  '__ ||  .___.'(|  |_/
 |     |'|  |      |  |'->
 `-----' `--'      `--'

*-------------------------------------*
* LINUX POST INSTALLER - Ver. 0.6 dev *
*-------------------------------------*

#===============================================================================
#title           :lpi.py
#description     :Linux Post-Installer script
#author          :Stefano Peris
#email           :techno.prometheus@gmail.com
#date            :21/01/2017
#version         :0.1
#usage           :python lpi.py
#notes           :Nothing
#python_version  :3.5
#===============================================================================
'''

## IMPORTANTE:

## Se necessario, dare i permessi di esecuzione al file con: chmod +x lpi.py
## Per generare il bytecode "*.pyc", da terminale scrivere il seguente comando:
## python -c "import lpi.py"

#===============================================================================

# Librerie e moduli
import os

# Pulisce lo schermo
def clear_screen():
    os.system('clear')

#===============================================================================

def menu():
    print("*---------------------------------*")
    print("* LINUX POST INSTALLER - Ver. 0.1 *")
    print("*---------------------------------*")
    print("")
    print("+------------------ ABOUT -------------------+")
    print("+ Autore: Stefano Peris <TechnoPrometheus>   +")
    print("+ eMail: technoprometheus@gmail.com          +")
    print("+--------------------------------------------+")
    print("")
    print("+------------------------+")
    print("+--------- MENU ---------+")
    print("+------------------------+")
    print("")
    print("")
    print("[1] Programmi CLI (Terminale)")
    print("[2] Utility")
    print("[3] Compilatori C/C++")
    print("[4] Librerie C/C++")
    print("[5] Tool di sviluppo")
    print("[6] Ambienti di sviluppo (IDE)")
    print("[7] Programmi di grafica 2D/3D")
    print("[8] Giochi")
    print("[i] Info")
    print("[x] Esci")

loop = 1

while loop:        ## Ciclo che prosegue fino a quando loop = 0 (false)
    
    menu()         ## Visualizza il menu nel terminale
    print("\n")
    print("\n")
    print("\n")
    
    opzione = input("Digita l'opzione desiderata > ")
	opzione = int(opzione)
     
    if opzione == 1:     
        print ("Menu 1 è stato selezionato")
        ## È possibile aggiungere il codice o funzioni qui
    elif opzione == 2:
        print ("Menu 2 è stato selezionato")
        ## È possibile aggiungere il codice o funzioni qui
    elif opzione == 3:
        print ("Menu 3 è stato selezionato")
        ## È possibile aggiungere il codice o funzioni qui
    elif opzione == 4:
        print ("Menu 4 è stato selezionato")
        ## È possibile aggiungere il codice o funzioni qui
    elif opzione == 5:
        print ("Menu 5 è stato selezionato")
        ## È possibile aggiungere il codice o funzioni qui
        loop = 0 # Ferma il ciclo
    else:
        # Valori diversi da 1-8 e i-x generano un messaggio di errore
        input("Errore. Premi un tasto per riprovare...")
        

