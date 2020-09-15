#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#Módulos
import os #Módulo de Comandos do Sistema Operacional
import time #Módulo de Tempo/delay
import socket #Módulo de Soquetes de Rede
import sys #Módulo de Interação por linhas de comandos
from shutil import which #Módulo para Verificar Requisitos do Programa

#Cores Utilizadas no Programa/Algoritmo
R = '\033[31m' # Vermelho
G = '\033[32m' # Verde
C = '\033[36m' # Ciano
W = '\033[0m'  # Branco
Y = '\33[33m'  # Amarelo
I = '\33[55m \33[6m' #Piscador
PORT = 1

def dependencies(): #Abstração que verifica Requisitos #{
   print (G + "[" + W + "+" + G + "]" + C + " Verificando Dependências..." + W)
   time.sleep(1)
   pkgs = ["python3", "bash", "curl"]
   inst = True
   for pkg in pkgs:
         present = which(pkg)
         if (present == None):
                 print (R + "[" + W + "-" + R + "]" + W + pkg + " não foi instalado.")
                 inst = False
         else:
                 pass
   if (inst == False):
         exit()
   else:
         __init__() #}

def __init__(): #Banner do Programa
   os.system("clear")
   print (G +
        r'''
    ,o888888o.     8 888888888o.            .8.            d888888o.    8 8888
 . 8888     `88.   8 8888    `88.          .888.         .`8888:' `88.  8 8888
,8 8888       `8b  8 8888     `88         :88888.        8.`8888.   Y8  8 8888
88 8888        `8b 8 8888     ,88        . `88888.       `8.`8888.      8 8888
88 8888         88 8 8888.   ,88'       .8. `88888.       `8.`8888.     8 8888
88 8888         88 8 888888888P'       .8`8. `88888.       `8.`8888.    8 8888
88 8888        ,8P 8 8888`8b          .8' `8. `88888.       `8.`8888.   8 8888
`8 8888       ,8P  8 8888 `8b.       .8'   `8. `88888.  8b   `8.`8888.  8 8888
 ` 8888     ,88'   8 8888   `8b.    .888888888. `88888. `8b.  ;8.`8888  8 8888
    `8888888P'     8 8888     `88. .8'       `8. `88888. `Y8888P ,88P'  8 8888 ''')
   print ("\t\t\t\t" + W + ".:. Diego333-ms .:.")

def Menu_Programa(): #Menu Principal do Programa/Algoritmo
   print ("\n" + G + "[" + W + "+" + G + "]" + C + " Escolha uma das opções:")
   print ("\n" + G + "[" + W + "01" + G + "]" + C + " Scanner de Portas usando TCP")
   print ("\n" + G + "[" + W + "02" + G + "]" + C + " Scanner de Portas usando UDP")
   OPTION = str(input("\n" + Y + "[" + W + "?" + Y + "]" + W + " Orasi " + C + "> " + G))
   if (OPTION == "01" or OPTION == "1"):
     Port_ScannerTCP()
   elif (OPTION == "02" or OPTION == "2"):
     Port_ScannerUDP()
   else:
     print ("\n" + R + "[" + W + "-" + R + "]" + W + " A opção escolhida é Inválida")
     time.sleep(2.5)
     __init__()
     Menu_Programa()

def Port_ScannerTCP():
   print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite o Domínio do Host Alvo:")
   HOST_TARGET = str(input("\n" + Y + "[" + W + "?" + Y + "]" + W + " Orasi " + C + "> " + G))
   time.sleep(1.5)
   try:
     HOST_IP = socket.gethostbyname(HOST_TARGET)
     Port_ScannerTCP_Scan(HOST_TARGET,HOST_IP,PORT)
   except socket.gaierror:
     print ("\n" + R + "[" + W + "-" + R + "]" + W + " O Domínio Alvo %s não foi localizado" %HOST_TARGET)
     time.sleep(2.5)
     __init__()
     Port_ScannerTCP()

def Port_ScannerTCP_Scan(HOST_TARGET,HOST_IP,PORT):
   print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite o Número de Portas a ser Analisada:")
   RANGE = int(input("\n" + Y + "[" + W + "?" + Y + "]" + W + " Orasi " + C + "> " + G))
   time.sleep(1.5)
   __init__()
   print ("\n" + C + "-----------------------------------------")
   print ("\n" + G + "[" + W + "+" + G + "]" + W + " Realizando Varredura no Alvo:" + G + " %s" %HOST_TARGET)
   print ("\n" + G + "[" + W + "+" + G + "]" + W + " Endereço IP do Alvo:" + G + " %s" %HOST_IP)
   print ("\n" + C + "-----------------------------------------")
   time.sleep(2)
   while (PORT < RANGE+1):
     TCP_CONNECT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     TCP_STATUS = TCP_CONNECT.connect_ex((HOST_TARGET,PORT))
     try:
       if (TCP_STATUS == 0):
         SERVICE = socket.getservbyport(PORT, "tcp")
         print ("\n" + G + "[" + W + "+" + G + "]" + G + " Porta: %i Status: Aberta Serviço: %s" %(PORT,SERVICE))
     except OSError:
         print ("\n" + G + "[" + W + "+" + G + "]" + G + " Porta: %i Status: Aberta Serviço: Filtrado" %PORT)
     else:
         print ("\n" + R + "[" + W + "-" + R + "]" + C + " Porta: %i Status: Fechada" %PORT)
     PORT += 1

def Port_ScannerUDP():
   print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite o Domínio do Host Alvo:")
   HOST_TARGET = str(input("\n" + Y + "[" + W + "?" + Y + "]" + W + " Orasi " + C + "> " + G))
   time.sleep(1.5)
   try:
     HOST_IP = socket.gethostbyname(HOST_TARGET)
     Port_ScannerUDP_Scan(HOST_TARGET,HOST_IP,PORT)
   except socket.gaierror:
     print ("\n" + R + "[" + W + "-" + R + "]" + W + " O Domínio Alvo %s não foi localizado" %HOST_TARGET)
     time.sleep(2.5)
     __init__()
     Port_ScannerUDP()

def Port_ScannerUDP_Scan(HOST_TARGET,HOST_IP,PORT):
   print ("\n" + G + "[" + W + "+" + G + "]" + C + " Digite o Número de Portas a ser Analisada:")
   RANGE = int(input("\n" + Y + "[" + W + "?" + Y + "]" + W + " Orasi " + C + "> " + G))
   time.sleep(1.5)
   __init__()
   print ("\n" + C + "-----------------------------------------")
   print ("\n" + G + "[" + W + "+" + G + "]" + W + " Realizando Varredura no Alvo:" + G + " %s" %HOST_TARGET)
   print ("\n" + G + "[" + W + "+" + G + "]" + W + " Endereço IP do Alvo:" + G + " %s" %HOST_IP)
   print ("\n" + C + "-----------------------------------------")
   time.sleep(2)
   while (PORT < RANGE+1):
     UDP_CONNECT = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     UDP_STATUS = UDP_CONNECT.connect_ex((HOST_TARGET,PORT))
     try:
       if (UDP_STATUS == 0):
         SERVICE = socket.getservbyport(PORT, "udp")
         print ("\n" + R + "[" + W + "-" + R + "]" + C + " Porta: %i Status: Fechada" %PORT)
     except OSError:
         print ("\n" + G + "[" + W + "+" + G + "]" + G + " Porta: %i Status: Aberta Serviço: Filtrado" %PORT)
     else:
         print ("\n" + G + "[" + W + "+" + G + "]" + G + " Porta: %i Status: Aberta Serviço: %s" %(PORT,SERVICE))
     PORT += 1

def stop():
   sys.exit(1)

try:
 dependencies()
 Menu_Programa()

except KeyboardInterrupt:
 stop()

finally:
 print ("\n" + G + "[" + W + "+" + G + "]" + C + " Obrigado por utilizar o Programa" + W)
