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
#description     :Linux Post-Installer script.
#author          :Stefano Peris
#email           :technoprometheus@gmail.com
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

# Variabili globali
opzione = 0

# Pulisce lo schermo
def clear_screen():
    os.system('clear')

#===============================================================================

