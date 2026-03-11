# Ejercicio 3 Desafio Modulo 1
#---------------------------

#Definicion de Variables
pesoPA=112
pesoMu=75
cantPA = 0
cantaMU = 0
#Interaccion con el usuario
cantPA = int(input("  Ingrese la cantidad de Payasos de vender : ") )

cantaMU = int(input("  Ingrese la cantidad de Muñecas de vender : "))

#Definicion de Formula
pesoTotal = pesoPA*cantPA+pesoMu*cantaMU
#Print resultado
print(f"El peso total del paquete será {pesoTotal} grs.")