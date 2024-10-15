""" Pedirá por teclado una palabra y hemos de decir si es un palíndromo o no  """

# Declaracion de variables 

palabra =  ""   #Cadena que contendra la palabara a analizar
longitudTexto=0 #contendra el tamaño
indice=0        #para recorrer la palabra




# programa

palabra = input("introduce la palabra: ")
longitudTexto = len(palabra) 
for indice in range(0,longitudTexto):

    
